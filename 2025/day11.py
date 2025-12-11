#!/usr/bin/evn python3

from collections import deque

from aoc import mul, read_input


Graph = dict[str, list[str]]


def count_paths(graph: Graph, start: str, end: str) -> int:
    nodes = set(graph.keys())
    for n in graph.values():
        nodes.update(n)

    indegree = {n: 0 for n in nodes}
    for node, ns in graph.items():
        for n in ns:
            indegree[n] += 1

    q = deque(n for n in nodes if indegree[n] == 0)
    topo = []

    while q:
        n = q.popleft()
        topo.append(n)
        for n in graph.get(n, []):
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

    path_count = {n: 0 for n in nodes}
    path_count[start] = 1
    for node in topo:
        for n in graph.get(node, []):
            path_count[n] += path_count[node]
    return path_count[end]


def part_1(graph: Graph) -> int:
    return count_paths(graph, "you", "out")


def part_2(graph: Graph) -> int:
    return mul([
        count_paths(graph, "svr", "fft"),
        count_paths(graph, "fft", "dac"),
        count_paths(graph, "dac", "out"),
    ])


def main():
    graph = {
        l.split(": ")[0]: l.split(": ")[1].split()
        for l in read_input().splitlines()
    }
    print(f"Part I: {part_1(graph)}")
    print(f"Part II: {part_2(graph)}")


if __name__ == "__main__":
    main()
