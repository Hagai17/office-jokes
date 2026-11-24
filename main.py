"""Write one office joke to /output/entry.txt.

The line is a single line of at most 199 characters about office life: a
real joke with a setup and a turn, true to the office, tightly worded.
"""

import os

LINE = (
    "The fire drill took four minutes to evacuate the building and forty "
    "minutes to convince anyone to go back inside."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
