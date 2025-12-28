from collections import deque

from task4 import heap_to_tree, draw_tree


def gradient_colors(n):
    # Generate n colors from dark blue to light blue as hex RGB: #RRGGBB
    if n <= 0:
        return []

    colors = []
    for i in range(n):
        t = i / max(1, n - 1)

        r = int(40 + 50 * t)
        g = int(70 + 80 * t)
        b = int(150 + 105 * t)

        colors.append(f"#{r:02x}{g:02x}{b:02x}")

    return colors


def dfs_stack_order(root):
    order = []
    if root is None:
        return order

    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_queue_order(root):
    order = []
    if root is None:
        return order

    q = deque([root])
    while q:
        node = q.popleft()
        order.append(node)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return order


def apply_colors_by_order(visit_order):
    colors = gradient_colors(len(visit_order))
    for node, color in zip(visit_order, colors):
        node.color = color


def visualize_dfs(root):
    order = dfs_stack_order(root)
    apply_colors_by_order(order)
    draw_tree(root, title="DFS traversal (stack) — dark -> light")
    print("DFS order:", [n.val for n in order])


def visualize_bfs(root):
    order = bfs_queue_order(root)
    apply_colors_by_order(order)
    draw_tree(root, title="BFS traversal (queue) — dark -> light")
    print("BFS order:", [n.val for n in order])


def main():
    heap = [0, 4, 1, 5, 10, 3]
    root = heap_to_tree(heap)

    visualize_dfs(root)
    visualize_bfs(root)


if __name__ == "__main__":
    main()
