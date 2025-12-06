#!/usr/bin/evn python3

from aoc import mul, read_input


def solve(op: str, ns: list[int]) -> int:
    return (sum if op == "+" else mul)(ns)


def part_1() -> int:
    *nums, ops = [
        [w for w in l.split()]
        for l in read_input().splitlines()
    ]
    return sum(
        solve(op, [int(ns[ix]) for ns in nums])
        for ix, op in enumerate(ops)
    )


def part_2() -> int:
    *nums, ops = read_input().splitlines()
    curr, res = [], 0
    for x in range(len(nums[0]) - 1, -1, -1):
        ds = []
        for y in range(len(nums)):
            if (c := nums[y][x]) != " ":
                ds.append(int(c))
        if ds:
            curr.append(sum(d * 10 ** ix for ix, d in enumerate(reversed(ds))))
            if (op := ops[x]) != " ":
                res += solve(op, curr)
                curr = []
    return res


def main():
    print(f"Part I: {part_1()}")
    print(f"Part II: {part_2()}")


if __name__ == "__main__":
    main()
