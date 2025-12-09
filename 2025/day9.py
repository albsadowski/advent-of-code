#!/usr/bin/evn python3

from aoc import read_input


Point = tuple[int, int]
Input = list[Point]


def area(p: Point, q: Point) -> int:
    return abs(p[0] - q[0] + 1) * abs(p[1] - q[1] + 1)


def orient(p: Point, q: Point, r: Point) -> int:
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if v == 0:
        return 0
    return 1 if v > 0 else 2


def cross_line(l1: tuple[Point, Point], l2: tuple[Point, Point]) -> bool:
    p1, q1 = l1
    p2, q2 = l2

    if p1 == p2 or p1 == q2 or q1 == p2 or q1 == q2:
        return False

    o1, o2 = orient(p1, q1, p2), orient(p1, q1, q2)
    o3, o4 = orient(p2, q2, p1), orient(p2, q2, q1)

    return (o1 != o2) and (o3 != o4)


def cross_rec(line: tuple[Point, Point], p: Point, q: Point) -> bool:
    return any(cross_line(line, rl) for rl in [
        (p, (q[0], p[1])),
        ((q[0], p[1]), q),
        (q, (p[0], q[1])),
        ((p[0], q[1]), p)
    ])


def part_1(input: Input) -> int:
    return max(area(p, q) for p in input for q in input)


def part_2(input: Input) -> int:
    lines, last = [], input[0]
    for p in input[1:]:
        lines.append((last, p))
        last = p
    lines.append((last, input[0]))

    return max(
        area(p, q)
        for p in input
        for q in input
        if not any(cross_rec(line, p, q) for line in lines)
    )


def main():
    input = [
        tuple(int(n) for n in l.split(","))
        for l in read_input().splitlines()
    ]
    print(f"Part I: {part_1(input)}")
    print(f"Part II: {part_2(input)}")


if __name__ == "__main__":
    main()
