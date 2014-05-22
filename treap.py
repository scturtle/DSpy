import random

class Node(object):
    __slots__ = 'key value fix left right'.split()

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.fix = random.random()
        self.left = None
        self.right = None

#      y                           x
#     / \       Left Rotation    /  \
#    x   T3   < - - - - - - -   T1   y
#   / \                            / \
#  T1  T2                        T2   T3
    def left_rotate(x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

#      x                           y
#     / \     Right Rotation     /  \
#    y   T3   - - - - - - - >   T1   x
#   / \                            / \
#  T1  T2                        T2   T3
    def right_rotate(x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def __str__(self):
        return '[key:{!r}, value:{!r}, fix:{!r}] left:{!r} right:{!r}'.format(
                self.key, self.value, self.fix, self.left, self.right)

    def __repr__(self):
        return '[key:{!r}, value:{!r}, fix:{!r}]'.format(
                self.key, self.value, self.fix)

class Treap:

    def __init__(self):
        self.root = None

    def _insert(self, root, node):
        if root is None:
            return node
        if node.key < root.key:
            root.left = self._insert(root.left, node)
            if root.left.fix < root.fix:
                root = root.right_rotate()
        else:
            root.right = self._insert(root.right, node)
            if root.right.fix < root.fix:
                root = root.left_rotate()
        return root

    def insert(self, key, data):
        self.root = self._insert(self.root, Node(key, data))

    def _delete(self, root, key):
        if root is None:
            return None, None
        if root.key == key:
            if root.left is None or root.right is None:
                return root.left or root.right, root
            else:
                if root.left.fix < root.right.fix:
                    root = root.right_rotate()
                    root.right, t = self._delete(root.right, key)
                else:
                    root = root.left_rotate()
                    root.left, t = self._delete(root.left, key)
        elif key < root.key:
            root.left, t = self._delete(root.left, key)
        else:
            root.right, t = self._delete(root.right, key)
        return root, t

    def delete(self, key):
        self.root, node = self._delete(self.root, key)
        return node.value

    def show(self, node='root', prefix=0):
        if node == 'root':
            node = self.root
        print(' '*prefix + str(node))
        if node:
            self.show(node.left, prefix+2)
            self.show(node.right, prefix+2)

if __name__ == '__main__':
    import random
    t = Treap()
    l = range(10)
    random.shuffle(l)
    print l
    for i in l:
        t.insert(i, i)
    t.show()
    for i in l:
        v = t.delete(i)
        print v,
