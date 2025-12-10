#!/usr/bin/evn python3

from collections import deque

from aoc import read_input


Machine = tuple[tuple[bool, ...], list[list[int]], tuple[int, ...]]
Input = list[Machine]


def switch(b: tuple[bool, ...], s: list[int]) -> tuple[bool, ...]:
    curr = list(b)
    for a in s:
        curr[a] = not curr[a]
    return tuple(curr)


def joltage(j: tuple[int, ...], s: list[int]) -> tuple[int, ...]:
    curr = list(j)
    for a in s:
        curr[a] += 1
    return tuple(curr)


def switch_count(m: Machine) -> int:
    b, sw, _ = m
    q = deque([(tuple([False] * len(b)), s, 1) for s in sw])
    while q:
        curr, s, c = q.popleft()
        switched = switch(curr, s)
        if switched == b:
            return c
        for ns in sw:
            q.append((switched, ns, c + 1))
    raise ValueError("oops")


def joltage_count(m: Machine) -> int:
    _, sw, j = m
    q = deque([(tuple([0] * len(j)), 0)])
    while q:
        curr, c = q.popleft()
        for s in sw:
            switched = joltage(curr, s)
            if switched == j:
                return c + 1
            for x, y in zip(j, switched):
                if y > x:
                    break
            else:
                q.append((switched, c + 1))
    raise ValueError("oops")


def part_1(input: Input) -> int:
    return sum(switch_count(m) for m in input)


def part_2(input: Input) -> int:
    return sum(joltage_count(m) for m in input)


def main():
    input = []
    for l in read_input().splitlines():
        split = l.split(" ")
        lights = tuple(a == "#" for a in split[0][1:-1])
        switches = [
            [int(b) for b in a[1:-1].split(",")]
            for a in split[1:-1]
        ]
        joltage = tuple(int(a) for a in split[-1][1:-1].split(","))
        input.append((lights, switches, joltage))

    print(f"Part I: {part_1(input)}")
    print(f"Part II: {part_2(input)}")


if __name__ == "__main__":
    main()
