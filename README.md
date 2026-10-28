# France: law history

This repository will hold the legislation of France (FR) as a history: one file per provision and one commit per law taking effect, dated by the day it took force, with the law that made each change as the commit author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `fr/` in the world tree.

**Status:** no law yet. This first commit records where the law of France can be read and what a build would need.

**Can it be built?** Ready to build: an official source has past versions by date and an API or bulk download.

**This commit is a placeholder.** The first real build must replace this history from scratch and force-push. It must never append law commits on top of it: they are dated by when each law took effect, often decades earlier, so dates in `main` would run backwards and break every on-date lookup. Builders should refuse to append when the root commit is this placeholder (its subject ends "sources, before any law").

**Official sources**

- [Légifrance](https://www.legifrance.gouv.fr): Article-level versions with in-force ranges. Bulk LEGI dumps at echanges.dila.gouv.fr/OPENDATA (full plus daily). The PISTE API needs free registration and OAuth.

**Existing open projects to check first**

- [Archéo Lex](https://github.com/Legilibre/Archeo-Lex): Rebuilds the git history of French codes. 106 stars, dormant since 2019.
- [La Fabrique de la Loi](https://www.lafabriquedelaloi.fr): How each French bill changed through Parliament. Parser dormant since 2022.

These are volunteer projects. Reconcile any of them against the official text before relying on it: a transcription is not the law (c3e/grundgesetz, for example, differs from the official gazette in 43 article texts on 20 July 2017).

All sources, with their status, are in [SOURCES.md](SOURCES.md). How these files were made is in [REPRODUCE.md](REPRODUCE.md).

This repository describes sources; it is not legal advice and holds no legal text yet.
