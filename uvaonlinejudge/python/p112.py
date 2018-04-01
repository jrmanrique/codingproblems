# Tree Summing

import re


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

    @property
    def children(self):
        return [self.left, self.right]

    def __repr__(self):
        return '({!r}, {!r}, {!r})'.format(self.value, self.left, self.right)


def sum_leaves(root):
    leaf_sums = []
    stack = [[root.value, root.children]]
    while stack:
        sigma, children = stack.pop(0)
        nones = 0
        for child in children:
            if child is None:
                nones += 1
            else:
                stack.append([sigma + child.value, child.children])
        if nones == 2:
            leaf_sums.append(sigma)
    return leaf_sums


def load_input():
    inp = ''
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            inp += line + '\n'
    return inp


def parse_input(string):
    inp = re.sub(r'\s+', ' ', string)
    cases = []
    while inp:
        goal, inp = inp.split(' ', 1)

        counter = 0
        for i, char in enumerate(inp):
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            if counter == 0:
                end = i + 1
                break

        node_str = re.sub(r'\s+', '', inp[:end])
        node_str = node_str[0] + node_str[1:].replace('(', ',(')
        node_str = node_str.replace('()', 'None')

        cases.append((int(goal), node_str))
        inp = inp[end:].strip()
    return cases


def main():
    inputs = load_input()
    cases = parse_input(inputs)

    for case in cases:
        goal, inp = case
        if inp == 'None':
            print('no')
            continue
        node = Node.deserialize(inp)
        print('yes' if goal in sum_leaves(node) else 'no')


if __name__ == '__main__':
    main()
