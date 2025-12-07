import sys

from functools import reduce
from typing import Iterator


Board = list[list[str]]


def read_input() -> str:
    with open(sys.argv[1], "r") as f:
        return f.read()


def read_board() -> Board:
    with open(sys.argv[1], "r") as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def shape(board: Board) -> tuple[int, int]:
    return len(board[0]), len(board)


def find_start(board: Board, mark: str = "S") -> tuple[int, int]:
    X, Y = shape(board)
    for y in range(Y):
        for x in range(X):
            if board[y][x] == mark:
                return (x, y)
    raise Exception("start point not found")


def iter_board(board: Board) -> Iterator[tuple[int, int]]:
    X, Y = shape(board)
    return (
        (x, y)
        for y in range(0, Y)
        for x in range(0, X)
    )


def ns(b: Board, x: int, y: int) -> Iterator[tuple[int, int]]:
    X, Y = shape(b)
    return (
        (i, j)
        for i in [x - 1, x, x + 1]
        for j in [y - 1, y, y + 1]
        if (
            i >= 0 and j >= 0 and
            i < X and j < Y and
            (i, j) != (x, y)
        )
    )


def mul(ns: list[int]) -> int:
    return reduce(lambda a, b: a * b, ns)
