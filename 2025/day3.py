#!/usr/bin/evn python3

import sys

from functools import cache


def read_lines(path: str) -> list[tuple[int, ...]]:
    with open(path, "r") as f:
        return [
            tuple(int(n) for n in l.strip())
            for l in f.readlines()
        ]


@cache
def max_joltage(bank: tuple[int, ...], length: int) -> int:
    if length == 0:
        return 0
    curr = 0
    for i in range(0, len(bank) - length + 1):
        lead = bank[i] * 10 ** (length - 1)
        next = lead + max_joltage(bank[i + 1:], length - 1)
        if next > curr:
            curr = next
    return curr


def main():
    input = read_lines(sys.argv[1])
    print(f"Part I: {sum(max_joltage(b, 2) for b in input)}")
    print(f"Part II: {sum(max_joltage(b, 12) for b in input)}")


if __name__ == "__main__":
    main()
