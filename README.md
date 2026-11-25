# One Line, No Deadline Met

[![make.fun](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/thanhvu261090/makefun-no-deadline-met/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![Reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/thanhvu261090/makefun-no-deadline-met/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)

Entry for the [make.fun bounty "One Line, No Deadline Met"](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce): one single-line joke giving an excuse for missing a deadline, capped at 200 characters. The entry is that line and nothing else — no picture, no link, no second line to set it up.

## The entry

> My calendar reminded me about the deadline the same way I remind myself to floss — right after it was already too late.

**Character count: 119** (limit: 200, single line).

## Why this line

The joke turns the one tool that is supposed to save you from missing a deadline — the calendar reminder — into the thing that failed. It blames the miss on the reminder showing up late, and it does it through the most relatable procrastinated chore there is: flossing. Everyone knows the "I'll floss tomorrow" loop, so the excuse lands as something a real person would actually say, while the twist is fresh — the reminder itself was late, not you. One line, one image, no setup.

## Run it

```sh
python3 main.py
```

Prints the entry line exactly as above. It also writes the same single line to `/output/entry.txt` when that directory can be created.

## Files

- `main.py` — prints the entry line (and writes it to `/output/entry.txt`).
- `entry.txt` — the entry line, and nothing else.

## Checks

- Entry is a single line, 119 characters, under the 200-character cap.
- `python3 main.py` output matches `entry.txt` exactly (verified locally).

## License

MIT — see [LICENSE](LICENSE).
