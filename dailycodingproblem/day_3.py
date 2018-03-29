class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def serialize_to_list(self, sentinel=None):
        serial = [self.value]
        if self.left:
            serial.extend(self.left.serialize(sentinel))
        else:
            serial.append(sentinel)
        if self.right:
            serial.extend(self.right.serialize(sentinel))
        else:
            serial.append(sentinel)
        return serial

    def serialize_to_tuple(self):
        return repr(self)

    @classmethod
    def deserialize_from_tuple(cls, source):
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

    ser = node.serialize_to_tuple()
    deser = Node.deserialize_from_tuple(ser)

    print('ASSERT:', deser.left.left.value == 'left.left')

    print('# TODO: Deserialize from list.')


if __name__ == '__main__':
    main()
