from typing import Iterator


Board = list[list[str]]


def read_board(path: str) -> Board:
    with open(path, "r") as f:
        return [[c for c in l.strip()] for l in f.readlines()]


def shape(board: Board) -> tuple[int, int]:
    return len(board[0]), len(board)


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
