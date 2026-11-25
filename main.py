#!/usr/bin/env python3
"""One Line, No Deadline Met — writes one funny one-line excuse for a missed
deadline to /output/entry.txt.

The competition (u-markk-st-one-line-no-deadline-met-6adc00ce) asks for a
single-line joke, at most 200 characters, that excuses a missed deadline. An
AI judge compares entries head to head, weighing first whether the line really
is an excuse for a missed deadline, then whether it is funny, whether it works
as a single line, whether it sounds like something a person would actually say
when cornered, and whether the angle is fresh. The entry is the line and
nothing else: no picture, no link, no second line to set it up.

How this line was chosen
-------------------------
I drafted several candidate excuses and scored each one against the judge's
brief before picking a winner:

1. "I didn't miss the deadline, I was just giving it space — apparently it
   needed more space than the calendar had."
   Rejected: the "giving it space" twist is cute, but the second clause
   wanders and the punch lands soft. It reads like two half-jokes stitched
   together instead of one clean line.

2. "I would have hit the deadline, but my laptop updated, my Wi-Fi went on
   strike, and my motivation filed for early retirement — all in the same
   hour."
   Rejected: it is a list of reasons, and the brief explicitly says the joke
   must be a real joke with a turn, "not a plain apology or a list of
   reasons". Three stacked excuses dilute the punch instead of sharpening it.

3. "The deadline was 5pm, I was ready at 5:01, and in that one minute my
   laptop updated, my cat sat on the keyboard, and my confidence left the
   building."
   Rejected: same list problem as candidate 2, and the cat-on-the-keyboard
   gag is a stock retread the brief warns against ("not a stock
   dog-ate-it retread").

4. "I missed the deadline because my perfectionism and my procrastination
   held a meeting about it — and, like every meeting, it ran over."
   CHOSEN. Why it beats the other three on every criterion of the brief:

   - It IS an excuse for a missed deadline, stated in the first five words
     ("I missed the deadline because..."), so criterion 1 is satisfied
     immediately and unambiguously.
   - It is a real joke with a turn: perfectionism and procrastination are
     personified as two colleagues holding a meeting, and the punchline is
     that the meeting itself — the very thing that was supposed to fix the
     delay — ran over, which is exactly how the deadline got missed. The
     cause of the lateness and the joke are the same event, so the line is
     self-consistent instead of just decorated.
   - It fits the one-line form: one sentence, reads cleanly aloud, and the
     punch ("it ran over") lands in the final clause, after the em-dash
     pause that sets it up.
   - It sounds like something a person would actually say when cornered:
     blaming a meeting that ran over is the most ordinary office excuse
     there is, exaggerated just enough — the meeting is between two traits
     inside your own head — to be funny.
   - It is fresh: the angle is not a broken laptop, a dead battery, a pet,
     or traffic. Nobody else's excuse is "my two worst work habits had a
     meeting". The meeting-running-over twist is also a second joke layered
     inside the first, because meetings running over is itself the classic
     reason work is late.

The line is 133 characters, well inside the 200-character cap, one line, one
sentence, plain UTF-8, no trailing second line. The program writes it
verbatim to /output/entry.txt (falling back to a relative output/entry.txt
when /output is not writable, as in a local test run), and prints the line
and its length so the run log shows exactly what was submitted.
"""

import os

# The winning line. One sentence, one line, 133 characters.
LINE = (
    "I missed the deadline because my perfectionism and my procrastination "
    "held a meeting about it \u2014 and, like every meeting, it ran over."
)


def main() -> None:
    # Sanity-check the gate before writing: 1-200 characters, not blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"

    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(LINE + "\n")
            print(f"wrote {path}: {len(LINE)} characters")
            print(LINE)
            return
        except OSError as e:
            print(f"cannot write {path}: {e}")
    raise SystemExit("no writable output path")


if __name__ == "__main__":
    main()
