#!/usr/bin/evn python3

import sys


Input = tuple[list[tuple[int, int]], list[int]]


def read_input(path: str) -> Input:
    ranges, ids, parse_ranges = [], [], True
    with open(path, "r") as f:
        for l in (l.strip() for l in f.readlines()):
            if l == "":
                parse_ranges = False
                continue
            if parse_ranges:
                split = l.split("-")
                assert len(split) == 2, "not a valid range"
                ranges.append((int(split[0]), int(split[1])))
            else:
                ids.append(int(l))
    return ranges, ids


def part_1(input: Input) -> int:
    ranges, ids = input
    fresh = 0
    for id in ids:
        for l, u in ranges:
            if id >= l and id <= u:
                fresh += 1
                break
    return fresh


def part_2(input: Input) -> tuple[int, int]:
    rs, sets = sorted(input[0]), []
    for l, u in rs:
        for ix, (sl, su) in enumerate(sets):
            if l >= sl and u <= su:
                break
            if l <= su and su < u:
                sets[ix][1] = u
                break
        else:
            sets.append([l, u])
    return sum(u - l + 1 for l, u in sets)


def main():
    input = read_input(sys.argv[1])
    print(f"Part I: {part_1(input)}")
    print(f"Part II: {part_2(input)}")


if __name__ == "__main__":
    main()
