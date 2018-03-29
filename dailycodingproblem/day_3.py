class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def serialize(self):
        return str(self)

    def preorder(self, sentinel=None):
        serial = [self.value]
        if self.left:
            serial.extend(self.left.preorder(sentinel))
        else:
            serial.append(sentinel)
        if self.right:
            serial.extend(self.right.preorder(sentinel))
        else:
            serial.append(sentinel)
        return serial

    def inorder(self, root):
        return (self.inorder(root.left) + [root.value] + self.inorder(root.right)) if root else []

    def levelorder(self):
        nodes = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                nodes.append(node.value)
                queue.extend([child for child in [node.left, node.right] if child])
        return nodes

    @classmethod
    def deserialize(cls, source):
        from ast import literal_eval as make_tuple

        def _tuple_to_node(tup):
            value, left, right = tup
            node = cls(value)
            if isinstance(left, tuple):
                node.left = _tuple_to_node(left)
            else:
                node.left = left
            if isinstance(right, tuple):
                node.right = _tuple_to_node(right)
            else:
                node.right = right
            return node

        return _tuple_to_node(make_tuple(source))

    def __repr__(self):
        return '({!r}, {!r}, {!r})'.format(self.value, self.left, self.right)


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    ser = node.serialize()
    deser = Node.deserialize(ser)

    print(ser)
    print('ASSERT:', deser.left.left.value == 'left.left')

    print('# TODO: Deserialize using other traversals.')


if __name__ == '__main__':
    main()
