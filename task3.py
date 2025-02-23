import heapq

import matplotlib.pyplot as plt
import networkx as nx


def dijkstra(num_nodes, graph, start_node):
    distances = [float("inf")] * num_nodes
    distances[start_node] = 0
    visited = [False] * num_nodes

    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if visited[current_node]:
            continue
        visited[current_node] = True

        for neighbor, weight in graph[current_node]:
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    return distances


def show_graph(nx_graph):
    pos = nx.spring_layout(nx_graph)
    edge_labels = nx.get_edge_attributes(nx_graph, "weight")
    nx.draw(
        nx_graph,
        pos,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=10,
        font_weight="bold",
    )
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)
    plt.show()


def read_input(file_path):
    station_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open(file_path, "r") as file:
        data = file.read().strip().split()
    num_nodes, num_edges = map(int, data[:2])
    edges = []
    index = 2
    for _ in range(num_edges):
        u = station_names.index(data[index])
        v = station_names.index(data[index + 1])
        w = int(data[index + 2])
        edges.append((u, v, w))
        index += 3
    start_node = station_names.index(data[index])
    return num_nodes, edges, start_node, station_names


def build_graph(num_nodes, edges, station_names):
    graph = [[] for _ in range(num_nodes)]
    nx_graph = nx.Graph()
    for u, v, w in edges:
        graph[u].append((v, w))
        nx_graph.add_edge(station_names[u], station_names[v], weight=w)
    return graph, nx_graph


def main():
    file_path = "test_input.txt"
    num_nodes, edges, start_node, station_names = read_input(file_path)
    graph, nx_graph = build_graph(num_nodes, edges, station_names)

    shortest_path = dijkstra(num_nodes, graph, start_node)

    for i in range(num_nodes):
        print(
            f"Shortest distance from {station_names[start_node]} to {station_names[i]}: {shortest_path[i]}"
        )

    show_graph(nx_graph)


if __name__ == "__main__":
    main()
