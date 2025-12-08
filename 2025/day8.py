#!/usr/bin/evn python3

import math

from aoc import mul, read_input


def eucl(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def connect(input: list[tuple[int, int, int]]) -> None:
    dist, clusters = {}, []
    for a in range(len(input)):
        for b in range(a + 1, len(input)):
            dist[(a, b)] = eucl(input[a], input[b])

    for ix, ((a, b), _) in enumerate(sorted(dist.items(), key=lambda item: item[1])):
        if ix == 1000:
            print(f"Part I: {mul(sorted(map(len, clusters), reverse=True)[:3])}")

        ac, bc = None, None
        for ic, c in enumerate(clusters):
            if a in c:
                ac = ic
            if b in c:
                bc = ic

        match (ac, bc):
            case (None, None):
                clusters.append(set([a, b]))
            case (ic, None):
                clusters[ic].add(b)
            case (None, ic):
                clusters[ic].add(a)
            case (ic1, ic2) if ic1 != ic2:
                merged = clusters.pop(max(ic1, ic2))
                clusters[min(ic1, ic2)].update(merged)

        if sum(map(len, clusters)) == len(input):
            break

    print(f"Part II: {input[a][0] * input[b][0]}")


def main():
    connect([
        tuple([int(n) for n in l.split(",")])
        for l in read_input().splitlines()
    ])


if __name__ == "__main__":
    main()
