# The Blocks Problem

class Blocks():
    def __init__(self, size):
        self.size = size
        self.table = {k: [k] for k in range(size)}

    def _get_position(self, block):
        for k, v in self.table.items():
            if block in v:
                return k, v.index(block)
        return None

    def _get_over(self, block):
        x, y = self._get_position(block)
        return self.table[x][y + 1:]

    def _move(self, block, pos, index=None):
        x, y = self._get_position(block)
        if index is None:
            return self.table[pos].append(self.table[x].pop(y))
        else:
            return self.table[pos].insert(index, self.table[x].pop(y))

    def _return_home(self, block):
        return self._move(block, block, 0)

    def moveonto(self, a, b):
        for block in self._get_over(a):
            self._return_home(block)
        for block in self._get_over(b):
            self._return_home(block)
        x, _ = self._get_position(b)
        return self._move(a, x)

    def moveover(self, a, b):
        for block in self._get_over(a):
            self._return_home(block)
        x, _ = self._get_position(b)
        return self._move(a, x)

    def pileonto(self, a, b):
        for block in self._get_over(b):
            self._return_home(block)
        x, _ = self._get_position(b)
        for block in [a] + self._get_over(a):
            self._move(block, x)

    def pileover(self, a, b):
        x, _ = self._get_position(b)
        for block in [a] + self._get_over(a):
            self._move(block, x)

    def quit(self):
        for k, v in self.table.items():
            print('{}: {}'.format(k, ' '.join([str(d) for d in v])))

    def __repr__(self):
        return repr(self.table)


def main():
    n = int(input())

    actions = []
    while True:
        try:
            action = input()
        except EOFError:
            break
        else:
            actions.append(action)

    b = Blocks(n)

    ACTIONS = {
        'move': {
            'over': b.moveover,
            'onto': b.moveonto,
        },
        'pile': {
            'over': b.pileover,
            'onto': b.pileonto,
        }
    }

    for action in actions:
        if action == 'quit':
            b.quit()
        else:
            action = action.split()
            ACTIONS[action[0]][action[2]](int(action[1]), int(action[3]))


if __name__ == '__main__':
    main()
