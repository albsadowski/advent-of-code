#!/usr/bin/evn python3

import sys

from aoc import Board, iter_board, ns, read_board, shape


def can_access(b: Board, x: int, y: int) -> bool:
    if b[y][x] != "@":
        return False
    return sum(b[j][i] == "@" for i, j in ns(b, x, y)) < 4


def part_1(b: Board) -> int:
    return sum(can_access(b, x, y) for x, y in iter_board(b))


def remove(b: Board) -> int:
    to_remove = [
        (x, y)
        for x, y in iter_board(b)
        if can_access(b, x, y)
    ]
    for x, y in to_remove:
        b[y][x] = "."
    return len(to_remove)


def part_2(input: Board) -> int:
    count = 0
    while (removed := remove(input)) > 0:
        count += removed
    return count


def main():
    input = read_board(sys.argv[1])
    print(f"Part I: {part_1(input)}")
    print(f"Part II: {part_2(input)}")


if __name__ == "__main__":
    main()
