# Billeaford Hall garage review site

Static adaptation of the existing family review pack. The original design, models and documents are preserved. No third-party runtime dependencies are needed.

Run `python3 build.py` to create and validate `dist/`. Run `python3 serve.py` for local preview. The Sites manifest identifies this site's existing registration; reuse it.

The online viewer loads geometry separately so its page and fallback picture can appear immediately. The full-pack download joins same-origin parts into the original ZIP and checks their sizes and hashes. Each static asset stays below 25 MiB.

Content originates in the parent project's packaging and site-preparation scripts. The checked-in `source/` snapshot is sufficient to rebuild this standalone site.
