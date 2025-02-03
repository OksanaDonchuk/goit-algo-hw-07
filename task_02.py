class Node:
    def __init__(self, key: int):
        """
        Клас для представлення вузла двійкового дерева пошуку (BST).

        Args:
            key (int): Значення вузла.
        """
        self.left: "Node | None" = None
        self.right: "Node | None" = None
        self.key: int = key


def get_min_value(node: Node | None) -> int | None:
    """
    Знаходить найменше значення у двійковому дереві пошуку.

    Args:
        node (Node | None): Кореневий вузол дерева.

    Returns:
        int | None: Найменше значення або None, якщо дерево порожнє.
    """
    if node is None:
        return None  # Якщо дерево порожнє

    current = node
    # Рухаємося ліворуч до самого кінця
    while current.left is not None:
        current = current.left
    return current.key


# Приклад використання:
root = Node(10)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(16)
root.right.left = Node(12)
root.right.right = Node(28)

# Виклик функції
print("Найменше значення в дереві:", get_min_value(root))
