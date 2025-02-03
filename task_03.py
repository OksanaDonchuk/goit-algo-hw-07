class Node:
    def __init__(self, value: int):
        """
        Клас для представлення вузла двійкового дерева пошуку (BST).

        Args:
            value (int): Значення вузла.
        """
        self.value: int = value
        self.left: "Node | None" = None
        self.right: "Node | None" = None

def get_sum_value(node: Node | None) -> int:
    """
    Рекурсивно обчислює суму всіх значень у двійковому дереві пошуку.

    Args:
        node (Node | None): Кореневий вузол дерева.

    Returns:
        int: Сума всіх значень у дереві. Якщо дерево порожнє, повертає 0.
    """
    if node is None:
        return 0
    
    # Рекурсивний підхід: сума значення поточного вузла + сума лівого та правого піддерева
    return node.value + get_sum_value(node.left) + get_sum_value(node.right)

# Приклад використання:
root = Node(10)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(16)
root.right.left = Node(12)
root.right.right = Node(28)

# Виклик функції
print("Сума всіх значень у двійковому дереві:", get_sum_value(root))