# The World, 27 November 2026

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Barkie303/news-image-20261127-v2/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Barkie303/news-image-20261127-v2/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A newspaper front page summing up the world's news of **Friday, 27 November 2026** in one image: the drone attack on Kuwait that killed two Italian technicians, Zelenskyy's warning of a new Russian mass strike, Thanksgiving storms cutting power to nearly a million Americans, New Zealand's coalition falling one seat short, the ECB's new president, Ebola passing 12,000 cases in DR Congo, Amazon's Black Friday strikes in 20+ countries, and a Thanksgiving NFL night of three last-second thrillers — 54 sourced stories in all, with a UTC timeline of the day.

## How it was made

The image (`entry.png`, 1024×1024, ~117 KB) was drawn with PIL from the 54 verified stories listed in `SOURCES.md`, each checked against live reporting published on 27 November 2026 up to 09:00 UTC. `build/entry-image.py` is the drawing script; `main.ts` copies the finished image to `/output/entry.png`.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
