# Tools

The scripts behind this France-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/france-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only france-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `late_ext_check.py` sit two folders above
the scripts, next to `config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in French and English, light and dark |
| `config.json` | The repository, the French category names, the top-level folders that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `redo.py` | Runs `patch_detectors.py`, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews]`; `EMBED_FONTS` names the script that embeds the chart's fonts) |
| `late_ext_check.py` | Hand-check helper: for each empty period that survived the review, whether the extending commit replaced the old date with the new one in the same sentence, the extending text's signing date, and the articles of the extending text, where this repository holds them, that say when it takes effect |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(textes/(avis|circulaire|decision)|data|tools)/'`.

The detectors already carried the fixes in `patch_detectors.py` when they were run; `redo.py` was not needed. Changes made for
this repository:

- `config.json` counts as not law only the notices (`textes/avis/`), circulars (`textes/circulaire/`) and decisions
  (`textes/decision/`, among them a few of the Conseil d'État and the Conseil constitutionnel), with `data/` and `tools/`.
  Of the commits with an `In-force` trailer, all but five corrections carry no `Kind` trailer, so `add_root.py`, unchanged,
  counts 187,161 commits as law.
- `build_vulns.py` gives each retroactive-date flag the path of the first file the text's commit wrote that day, in its own
  folder under `textes/` where it has one (global-law's detector names only the text), so that notices and circulars count
  as not law. It also carries the kit's fix that matches lapsed-limit reviews on 400 characters of context, not 80.
- `late_ext_select.py` takes every empty period whose old and new date open the same sentence, and fills up to 40 with the
  shortest gaps only when there are fewer; here 372 shared a sentence, so all 372 were reviewed.
- After the sixth round of `patch_detectors.py` (currency names), `detectors/currency_scan.py` was run again: dead
  currencies went from 600 to 587.
