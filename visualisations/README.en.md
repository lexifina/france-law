# French law in 20 charts

[Français](README.md)

Charts on every country's law, from the whole of global-law: [global-law visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations). These are the charts on France alone.

Twenty charts on French law, drawn only from the data in this repository: the history of LEGI, the database behind Légifrance, one article version at a time. The Constitution, 77 codes and 118,773 other texts in force on 28 October 2026 (lois, ordonnances, décrets and arrêtés: laws, government ordinances, decrees and ministerial orders), and for each of the 1,528,182 article versions, the day it took effect and the text that wrote it.

Open [`le-droit-francais-en-20-graphiques.html`](le-droit-francais-en-20-graphiques.html) in a browser. The page is one file with all its data inside; it loads only the d3 library and its fonts from the web. The controls at the top right switch the language (French or English) and the theme (light or dark). Each chart names its data path in the repository, its record count and its limits, and has a table of every number under it. Hover over a mark for the exact values.

The charts are descriptive: they show what the sources record, not why.

## The charts

### I. The law in force

#### 1. The law in force

The 692,977 articles in force on 28 October 2026, by kind of text: 45% in ministerial orders, 24% in the 77 codes; and the longest texts outside the codes.

![The law in force](stills/en/01.png)

#### 2. More and more articles

The articles in force on 1 January of each year since 1990 (298,214 in 2000, 692,977 in October 2026), and those that come into force or cease to be in force each year.

![More and more articles](stills/en/02.png)

#### 3. The 77 codes

The codes and their parts, read from the letter of the article numbers: 58% R, D or A articles; the Public Health Code holds 13,667.

![The 77 codes](stills/en/03.png)

#### 4. How old the wording in force is

The year each article's current wording took effect, by kind of text: half in 2015 or later.

![How old the wording in force is](stills/en/04.png)

#### 5. The Civil Code article by article

The Civil Code's 2,899 articles in order, coloured by the period of their wording: 596 with no version later than 1803–1804, 949 rewritten since 2016.

![The Civil Code article by article](stills/en/05.png)

### II. How the law changes

#### 6. Who writes the law

Article versions by year and by the text that wrote them (since 2000: 42% decrees, 38% orders, 11% laws), and who writes the 12 codes changed most.

![Who writes the law](stills/en/06.png)

#### 7. 1 January

The days of entry into force on a calendar: 11.6% of the article versions of 2000–2025 on 1 January; the day of publication in the Journal officiel and the day of entry into force.

![1 January](stills/en/07.png)

#### 8. From signature to entry into force

The time between a text's signature and the entry into force of what it writes: a median of 2 days for a law, more than six months for 21% of the versions written by ordinance.

![From signature to entry into force](stills/en/08.png)

#### 9. From signature to the Journal officiel

The time between a text's date and its publication, 1990–2026: from 12 to 5 days at the median for an order, one day for a law.

![From signature to the Journal officiel](stills/en/09.png)

#### 10. The biggest laws

The 15 laws that wrote the most article versions in the codes, and in which codes: 1,091 for Law No. 2013-672.

![The biggest laws](stills/en/10.png)

### III. The codes

#### 11. How the codes grew

The number of articles in eight codes since 1950: the Public Health Code went from 1,383 articles in 1990 to 13,667.

![How the codes grew](stills/en/11.png)

#### 12. Codes written in a day

The 30 days since 1985 on which at least 1,000 articles of one code took effect together: 9,944 for the Labour Code on 1 May 2008.

![Codes written in a day](stills/en/12.png)

#### 13. The codes year by year

Article versions by year for the 25 codes changed most since 1990: 43,350 for the Public Health Code.

![The codes year by year](stills/en/13.png)

#### 14. The most rewritten articles

The 20 code articles with the most versions: 97 for article R. 251 of the Code of Criminal Procedure, which says in which wording the code applies overseas.

![The most rewritten articles](stills/en/14.png)

#### 15. Finance laws

Who writes the General Tax Code and the Social Security Code: 57% of the first one's versions since 2000 come from finance laws.

![Finance laws](stills/en/15.png)

### IV. Parliament, the Government and the courts

#### 16. Laws and ordinances

Laws and ordinances by year of signature since 1980: 125 ordinances in 2020, 25 of them on 25 March.

![Laws and ordinances](stills/en/16.png)

#### 17. "A law aiming to"

The words that open the titles of laws: "visant à" or "tendant à" (aiming to) in 45% of titles since 2020, 6% in the 2000s.

!["A law aiming to"](stills/en/17.png)

#### 18. Implementing decrees

The time between a law and its first implementing decree: within six months for 55% of the laws of 2018–2024, 38% of those of 2000–2009.

![Implementing decrees](stills/en/18.png)

#### 19. The 1958 Constitution

The 25 revisions and the articles revised most often: 48 articles for the constitutional law of 23 July 2008, five revisions of article 34.

![The 1958 Constitution](stills/en/19.png)

#### 20. The courts in the text

The articles that decisions of the Conseil constitutionnel and the Conseil d'État rewrote or repealed: 218 for 176 decisions of the Conseil constitutionnel since 2010.

![The courts in the text](stills/en/20.png)

## Data

As of commit `1c0156f6d6`; LEGI's data was read up to 28 October 2026.

| Dataset | Where in the repository | Records | Coverage |
| --- | --- | ---: | --- |
| Git history | branch `main` | 187,161 law commits; 1,528,182 article versions, 402,230 ends of force | each version on the day it took effect (`In-force:`), from 25 August 1539 to 28 October 2026; LEGI's history is fullest from the 1990s |
| Tree | `constitution/`, `codes/<code>/`, `textes/<nature>/<year>/<text>/` | 692,977 articles in force | 3 Constitutions, 77 codes and 118,773 other texts on 28 October 2026 |
| Text records | `<text>/index.md` | 118,853 records | title, nature, number, date of the text, publication in the JORF, NOR; only for texts that still have an article in force |
| Corrections | `Redates:` trailers of documentation commits | 41 days of entry into force, 39 signing dates | applied to the commits they name |

## Limits

- **LEGI is not the whole Journal officiel.** The repository holds the texts LEGI consolidates; a text never consolidated, or repealed before it was, is missing. The early years of charts 2, 4 and 11 therefore count fewer.
- **Records exist only for texts still in force.** Titles, publication dates and numbers (charts 9, 15, 17 and 18) do not cover fully repealed texts.
- **Categories are read from names and titles.** The kind of text (the commit author's name), finance laws, the opening words of a title, implementing decrees and the court of a decision follow the rules in `src/prep.py`. Whatever no rule recognises counts as "other".
- **A version is one article file written.** Versions LEGI records without a change of text (about 27,000) make no commit and do not count.
- **LEGI credits each version to the text it names**, or to "Légifrance (DILA), version consolidée" when it names none ("unattributed"); a court decision is the author only of the changes it makes itself.
- **2026 is partial** (to 28 October) and drawn lighter.

## Rebuilding

```sh
python visualisations/src/make.py            # history, tree and records -> src/.build/ -> le-droit-francais-en-20-graphiques.html
node visualisations/src/stills.cjs           # images for these READMEs (needs Playwright; PLAYWRIGHT=<path> if not global)
```

`make.py` reads everything from git objects, so it also works in a blobless (`--filter=blob:none`) or `--no-checkout` clone, where it downloads only the `index.md` records, the articles of the Constitution and the text of the 60 code articles with the most versions (about 120,000 small files). It reads `origin/main` (or `HEAD`) by default; `--ref` picks another branch or commit. It writes nothing into the repository except the page and the `src/.build/` folder (which git ignores).

| File | What it does |
| --- | --- |
| `src/make.py` | extracts the history, the tree and the records into `src/.build/`, then runs `prep.py` and `build.py` |
| `src/prep.py` | computes every number for the 20 charts and the data profile into `src/.build/data.json` |
| `src/page.tpl.html` | the page: text in both languages, the charts (d3), the tables |
| `src/build.py` | puts `data.json` into the template and writes the page |
| `src/stills.cjs` | draws each chart as a PNG into `stills/fr/` and `stills/en/` |

## Source and licence

The legal text and its history are LEGI's, the database published by the Direction de l'information légale et administrative (DILA), reused under the Licence Ouverte 2.0 (Etalab), which asks that the source (DILA) and the date of its last update be cited: 28 October 2026. See [`LICENSE`](../LICENSE).
