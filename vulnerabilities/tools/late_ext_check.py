"""Hand-check helper: for each empty period that survived the review, whether the extending commit replaced the old date
with the new one in the same place, the extending text's signing date, and the lines of the extending text (where this
repository holds it) that set when it takes effect.

    python -X utf8 late_ext_check.py [--all] > late_ext_check.txt      (--all: every reviewed flag, not only survivors)
    -> one block per flag, then a JSON line per flag in late_ext_check.json
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "gl", "vulnerabilities", "scripts")
PIN = json.load(open(os.path.join(S, "pins.json"), encoding="utf-8"))["corpora"][0]
G = os.path.join(S, "sources", "corpus", PIN["repo"] + ".git")
SHA = PIN["sha"]
MON = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()
EFFECT = re.compile(r"(?i)(entre(?:nt)? en vigueur|prend(?:ent)? effet|prendront effet|à compter du|a compter du|s'appliquent? (?:à|aux|au|à compter)|"
                    r"sont applicables|est applicable|rétroacti|produit(?:sent)? (?:ses|leurs) effets)")


def git(*a):
    return subprocess.run(["git", "-C", G, *a], capture_output=True).stdout.decode("utf-8", "replace")


def forms(d):
    y, m, dd = d.split("-"); m, dd = int(m), int(dd)
    day = "1er" if dd == 1 else str(dd)
    return [f"{day} {MON[m-1]} {y}", f"{dd} {MON[m-1]} {y}", f"{dd:02d}/{m:02d}/{y}", f"{dd}/{m}/{y}", d]


def act_folder(law, text_url):
    """the extending text's own folder in textes/, found by its JORF identifier"""
    jorf = (re.search(r"JORFTEXT\d+", text_url or "") or [None])[0]
    m = re.match(r"(?i)(décret|loi organique|loi|ordonnance|arrêté|décision|délibération)\b.*?(?:n°\s*([\d-]+))?\s+du\s+(\d+)(?:er)?\s+(\w+)\s+(\d{4})", law)
    if not m or not jorf:
        return None
    nat = {"décret": "decret", "loi": "loi", "loi organique": "loi-organique", "ordonnance": "ordonnance", "arrêté": "arrete",
           "décision": "decision", "délibération": "deliberation"}[m.group(1).lower()]
    year = m.group(5)
    cands = [l for l in git("ls-tree", "-d", "--name-only", f"{SHA}:textes/{nat}/{year}/").splitlines()]
    if m.group(2):
        cands = [c for c in cands if c == f"{nat}-{m.group(2)}"]
    else:
        mo = MON.index(m.group(4).lower()) + 1 if m.group(4).lower() in MON else 0
        cands = [c for c in cands if c.startswith(f"{nat}-{year}-{mo:02d}-{int(m.group(3)):02d}")]
    for c in cands:
        if jorf in git("show", f"{SHA}:textes/{nat}/{year}/{c}/index.md"):
            return f"textes/{nat}/{year}/{c}"
    return None


def effect_lines(folder):
    out = []
    for f in git("ls-tree", "--name-only", f"{SHA}:{folder}/").splitlines():
        if f == "index.md":
            continue
        for line in git("show", f"{SHA}:{folder}/{f}").splitlines():
            if EFFECT.search(line):
                out.append(f"{f}: {line.strip()[:300]}")
    return out


every = "--all" in sys.argv
recs = [json.loads(l) for l in open(os.path.join(S, "findings", "run", "late_extension_triage.jsonl"), encoding="utf-8")]
res, seen = [], set()
for x in recs:
    if not every and not (x.get("rebut") or {}).get("survives"):
        continue
    r = x["row"]; k = (r["path"], r["old_until"], r["new_until"], r["law"])
    if k in seen:
        continue
    seen.add(k)
    log = [l.split("|") for l in git("log", "--format=%h|%an|%(trailers:key=In-force,valueonly,separator=)|%(trailers:key=Signed,valueonly,separator=)|%(trailers:key=Text,valueonly,separator=)", SHA, "--", r["path"]).splitlines()]
    cs = [l for l in log if l[1] == r["law"] and l[2] == r["extended_in_force"]] or [l for l in log if l[1] == r["law"]]
    same, near, signed, text = False, [], "", ""
    fo, fn = forms(r["old_until"]), forms(r["new_until"])
    for c in cs:
        signed, text = c[3], c[4]
        d = git("diff", "-U0", "--word-diff=plain", f"{c[0]}^", c[0], "--", r["path"])
        for line in d.splitlines():
            if not ("{+" in line or "[-" in line):
                continue
            # the line before and after the change (word-diff marks only the words that changed: "31 décembre [-2025-]{+2027+}")
            before = re.sub(r"\[-(.*?)-\]", r"\1", re.sub(r"\{\+.*?\+\}", "", line))
            after = re.sub(r"\{\+(.*?)\+\}", r"\1", re.sub(r"\[-.*?-\]", "", line))
            if any(f in before for f in fo) and any(f in after for f in fn) and not any(f in after for f in fo):
                same = True; near.append(line.strip()[:400])
            elif any(f in line for f in fo + fn):
                near.append(line.strip()[:400])
    folder = act_folder(r["law"], text)
    eff = effect_lines(folder) if folder else []
    rec = dict(path=r["path"], old=r["old_until"], new=r["new_until"], law=r["law"], in_force=r["extended_in_force"],
               gap=r["gap_days"], signed=signed, replaced_in_place=same, act=folder, effect=eff[:6], diff=near[:3],
               survives=bool((x.get("rebut") or {}).get("survives")))
    res.append(rec)
    print(f"## {r['path']}\n   {r['old_until']} -> {r['new_until']} by {r['law']} (signed {signed or '?'}), in force {r['extended_in_force']} ({r['gap_days']} d)"
          f"\n   replaced in place: {same}; act in repo: {folder or '-'}")
    for h in near[:2]:
        print("     diff:", h)
    for e in eff[:4]:
        print("     act:", e)
json.dump(res, open(os.path.join(HERE, "late_ext_check.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
