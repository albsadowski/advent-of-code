#!/usr/bin/evn python3

from collections import defaultdict

from aoc import Board, find_start, iter_board, read_board, shape


def part_1(b: Board) -> int:
    bs, count = set([find_start(b)[0]]), 0
    for x, y in iter_board(b):
        if b[y][x] == "." or x not in bs:
            continue
        count += 1
        bs.remove(x)
        bs.add(x - 1)
        bs.add(x + 1)
    return count


def part_2(b: Board) -> int:
    bs = defaultdict(int)
    bs[find_start(b)[0]] = 1
    for x, y in iter_board(b):
        if b[y][x] == "." or x not in bs:
            continue
        bs[x - 1] += bs[x]
        bs[x + 1] += bs[x]
        bs[x] = 0
    return sum(bs.values())


def main():
    board = read_board()
    print(f"Part I: {part_1(board)}")
    print(f"Part II: {part_2(board)}")


if __name__ == "__main__":
    main()
