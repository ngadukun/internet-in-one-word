#!/usr/bin/env python3
"""The Internet in One Word.

Prints the entry: a single word for the whole internet.
"""

WORD = "doomscroll"


def main():
    # The entry is one word and nothing else: no spaces, no punctuation.
    assert WORD.isalpha() and " " not in WORD, "entry must be a single word"
    print(WORD)


if __name__ == "__main__":
    main()
