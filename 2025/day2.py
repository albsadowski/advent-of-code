#!/usr/bin/evn python3

import sys

from typing import Callable


def read_ranges(path: str) -> list[tuple[int, int]]:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    return [
        tuple(int(b) for b in l.split("-"))
        for l in lines[0].split(",")
    ]


def is_invalid_1(s: str) -> bool:
    return s[:len(s) // 2] == s[len(s) // 2:]


def is_made_of_dupes(s: str, i: int) -> bool:
    seg = s[0:i]
    for a in range(0, len(s), i):
        if seg != s[a:a + i]:
            return False
    return True


def is_invalid_2(s: str) -> bool:
    return any(is_made_of_dupes(s, i) for i in range(1, (len(s) // 2) + 1))


def count_invalid(input: list[tuple[int, int]], is_invalid: Callable[str, bool]) -> int:
    return sum(
        n
        for l, u in input
        for n in range(l, u + 1)
        if is_invalid(str(n))
    )


def main():
    input = read_ranges(sys.argv[1])
    print(f"Part I: {count_invalid(input, is_invalid_1)}")
    print(f"Part II: {count_invalid(input, is_invalid_2)}")


if __name__ == "__main__":
    main()
