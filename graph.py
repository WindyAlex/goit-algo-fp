import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.Graph()

    routers = ["Router1", "Router2", "Router3", "Router4"]
    servers = ["Server1", "Server2", "Server3", "Server4", "Server5"]

    G.add_nodes_from(routers, node_type="router")
    G.add_nodes_from(servers, node_type="server")

    edges = [
        ("Router1", "Router2"),
        ("Router2", "Router3"),
        ("Router3", "Router4"),
        ("Router1", "Router3"),
        ("Router2", "Router4"),

        ("Router1", "Server1"),
        ("Router1", "Server2"),
        ("Router2", "Server3"),
        ("Router3", "Server4"),
        ("Router4", "Server5"),
    ]
    G.add_edges_from(edges)

    return G


def create_weighted_graph():
    G = create_graph()

    weights = {
        ("Router1", "Router2"): 3,
        ("Router2", "Router3"): 2,
        ("Router3", "Router4"): 4,
        ("Router1", "Router3"): 6,
        ("Router2", "Router4"): 1,

        ("Router1", "Server1"): 1,
        ("Router1", "Server2"): 2,
        ("Router2", "Server3"): 2,
        ("Router3", "Server4"): 3,
        ("Router4", "Server5"): 1,
    }

    for (u, v), w in weights.items():
        G[u][v]["weight"] = w

    return G


def draw_graph(G, title="Graph"):
    pos = nx.spring_layout(G, seed=42)

    node_colors = []
    for node in G.nodes():
        t = G.nodes[node].get("node_type", "")
        node_colors.append("lightblue" if t == "router" else "lightgreen")

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1800,
        font_size=9
    )

    plt.title(title)
    plt.show()


def draw_weighted_graph(G, title="Weighted graph"):
    pos = nx.spring_layout(G, seed=42)

    node_colors = []
    for node in G.nodes():
        t = G.nodes[node].get("node_type", "")
        node_colors.append("lightblue" if t == "router" else "lightgreen")

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1800,
        font_size=9
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title(title)
    plt.show()
