import argparse
from collections import Counter
from collections.abc import Iterator
from typing import Optional


def load_words() -> Iterator[str]:
    with open('words_alpha.txt') as word_file:
        for line in word_file:
            yield line.strip()


def matches_pattern(word: str, pattern: str, length: int) -> bool:
    for i, ch in enumerate(pattern[:length]):
        if ch != '_' and word[i] != ch:
            return False
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('letters')
    parser.add_argument('filters', nargs='*')
    args = parser.parse_args()

    letters: str = args.letters
    pattern: Optional[str] = None
    length: Optional[int] = None

    if len(args.filters) == 1:
        if args.filters[0].isdigit():
            length = int(args.filters[0])
        else:
            pattern = args.filters[0]
    elif len(args.filters) == 2:
        pattern = args.filters[0]
        if args.filters[1].isdigit():
            length = int(args.filters[1])
        else:
            parser.error('length must be an integer')
    elif len(args.filters) > 2:
        parser.error('too many arguments: use [pattern] [length]')

    effective_length: Optional[int] = length if length is not None else (len(pattern) if pattern is not None else None)

    bag: Counter[str] = Counter(letters)
    for word in load_words():
        if effective_length is not None and len(word) != effective_length:
            continue
        if pattern is not None and not matches_pattern(word, pattern, len(word)):
            continue
        if not (Counter(word) - bag):
            print(word)
