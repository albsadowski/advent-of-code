#!/usr/bin/evn python3

import sys


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        return [l.strip() for l in f.readlines()]


def rotate(curr: int, value: int) -> tuple[int, int]:
    hits = abs(value) // 100
    if value > 0:
        value = value - hits * 100
    if value < 0:
        value = value + hits * 100
    if (
        (value < 0 and curr != 0 and value + curr <= 0) or
        (value > 0 and curr + value >= 100)
    ):
        hits += 1
    return (curr + value) % 100, hits


def part_1(input: list[int]) -> int:
    curr, count = 50, 0
    for value in input:
        curr, _ = rotate(curr, value)
        if curr == 0:
            count += 1
    return count


def part_2(input: list[int]) -> int:
    curr, count = 50, 0
    for value in input:
        curr, hits = rotate(curr, value)
        count += hits
    return count


def main():
    input = [
        -int(l[1:]) if l[0] == "L" else int(l[1:])
        for l in read_lines(sys.argv[1])
    ]
    print(f"Part I: {part_1(input)}")
    print(f"Part II: {part_2(input)}")


if __name__ == "__main__":
    main()
