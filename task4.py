import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            lx = x - 1 / (2 ** layer)
            pos[node.left.id] = (lx, y - 1)
            add_edges(graph, node.left, pos, x=lx, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            rx = x + 1 / (2 ** layer)
            pos[node.right.id] = (rx, y - 1)
            add_edges(graph, node.right, pos, x=rx, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root, title="Binary tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [n[1]["color"] for n in tree.nodes(data=True)]
    labels = {n[0]: n[1]["label"] for n in tree.nodes(data=True)}

    plt.figure(figsize=(9, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap):
    if not heap:
        return None

    nodes = [Node(v) for v in heap]

    for i in range(len(nodes)):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            nodes[i].left = nodes[li]
        if ri < len(nodes):
            nodes[i].right = nodes[ri]

    return nodes[0]


def visualize_heap(heap, title="Binary heap visualization"):
    root = heap_to_tree(heap)
    if root is None:
        print("Heap is empty.")
        return
    draw_tree(root, title=title)


def main():
    heap = [0, 4, 1, 5, 10, 3]
    visualize_heap(heap, "Binary Heap (array -> tree)")


if __name__ == "__main__":
    main()
