from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '({!r}, {!r}, {!r})'.format(self.value, self.left, self.right)


def count_unival(root):
    unival = 0
    stack = deque([root])
    while stack:
        current = stack.popleft()
        left = current.left.value if isinstance(current.left, Node) else current.left
        right = current.right.value if isinstance(current.right, Node) else current.right
        if left == right:
            unival += 1
        for child in (current.left, current.right):
            if child is not None:
                stack.append(child)
    return unival


def main():
    node = Node(0)
    node.left = Node(1)
    node.right = Node(0)
    node.right.left = Node(1)
    node.right.right = Node(0)
    node.right.left.left = Node(1)
    node.right.left.right = Node(1)
    print(node)

    print(count_unival(node))


if __name__ == '__main__':
    main()
