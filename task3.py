import heapq

from graph import create_weighted_graph, draw_weighted_graph


def dijkstra_heap(graph, start):
    dist = {node: float("inf") for node in graph.nodes}
    prev = {node: None for node in graph.nodes}
    dist[start] = 0

    heap = [(0, start)]  # (distance, node)
    visited = set()

    while heap:
        current_dist, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        if current_dist > dist[u]:
            continue

        for v, attrs in graph[u].items():
            w = attrs.get("weight", 1)
            new_dist = current_dist + w

            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, prev


def reconstruct_path(prev, start, target):
    if start == target:
        return [start]

    if prev[target] is None:
        return None

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    if path[-1] != start:
        return None

    path.reverse()
    return path


def main():
    G = create_weighted_graph()
    start = "Router1"

    dist, prev = dijkstra_heap(G, start)

    print(f"Starting vertex: {start}\n")

    print("Shortest distances to all vertices:")
    for node in sorted(G.nodes()):
        d = dist[node]
        print(f"  {node}: {'∞' if d == float('inf') else d}")

    print("\nShortest paths:")
    for node in sorted(G.nodes()):
        path = reconstruct_path(prev, start, node)
        if path is None:
            print(f"  {start} -> {node}: path not found")
        else:
            print(f"  {start} -> {node}: {' -> '.join(path)} "
                  f"(cost: {dist[node]})")

    draw_weighted_graph(G, "Internet topology (weighted)")


main()
