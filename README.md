[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/imnotripper/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/imnotripper/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# Sunday 22 November 2026 — the whole day on one front page

An entry for the [make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122). The image is a vintage newsprint front page, "The Global Times", with a world globe at its centre and five numbered panels telling the day's biggest stories. A strip along the foot of the page repeats all five headlines, so the day reads at a glance.

## What happened on 22 November 2026

1. **Gulf crisis — Iran hits US bases.** Iranian missiles strike US military assets in Kuwait and Bahrain; tankers are hit off Oman and an ADNOC vessel is attacked in the Strait of Hormuz.
2. **Lviv under fire — and Poland.** A Russian missile strike on Lviv kills at least two people, while Russian missiles and a drone cross into Poland and Warsaw calls it a provocation.
3. **Peru shaken — magnitude 6.9.** A powerful earthquake shakes the Andes in Peru.
4. **A trade deal ten years in the making.** The EU and Indonesia sign a deal scrapping 98.5% of tariffs between them.
5. **Three leaders, one summit.** Trump, Xi and Putin meet in Shenzhen at the APEC summit, billed as a "momentous" summit.

## Running it

`main.py` needs only the Python 3.13 standard library. It copies the bundled
`entry.png` — 1024×1024, 828,586 bytes — to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png` in the grader), after checking the file is a real PNG
under 1 MiB, and then verifies the copy byte-for-byte. No network is used, and
two runs write identical bytes.

## License

MIT — see [LICENSE](LICENSE).
