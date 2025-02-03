class Node:
    def __init__(self, key: int):
        """Клас для представлення вузла двійкового дерева пошуку (BST)."""
        self.left: "Node | None" = None
        self.right: "Node | None" = None
        self.key: int = key

def get_max_value(node: Node | None) -> int | None:
    """
    Знаходить найбільше значення в двійковому дереві пошуку.

    Args:
        node (Node | None): Кореневий вузол дерева.

    Returns:
        int | None: Найбільше значення або None, якщо дерево порожнє.
    """
    if node is None:
        return None  # Якщо дерево порожнє

    current = node
    # Рухаємося праворуч до кінця дерева
    while current.right is not None:
        current = current.right
    return current.key

# Створення правильного BST:
root = Node(10)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(16)
root.right.left = Node(12)
root.right.right = Node(28)

# Виклик функції
print("Найбільше значення в дереві:", get_max_value(root))