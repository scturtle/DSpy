from Queue import deque

class Node(object):
    __slots__ = 'key left right'.split()

    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    @staticmethod
    def merge_recursively(a, b):
        if a is None:
            return b
        if b is None:
            return a
        else:
            if a.key > b.key: # min heap
                a, b = b, a
            t = a.right
            a.right = a.left
            a.left = Node.merge_recursively(b, t)
            return a

    @staticmethod
    def merge(a, b):
        if a is None:
            return b
        if b is None:
            return a
        l = []
        while a:
            t = a.right
            l.append(a)
            a = t
        while b:
            t = b.right
            l.append(b)
            b = t
        l.sort(key=lambda o:o.key) # min heap
        while len(l) > 1:
            a, b = l.pop(), l.pop()
            b.right = b.left
            b.left = a
            l.append(b)
        return l[0]

class SkewHeap:

    def __init__(self):
        self.root = None

    def push(self, key):
        self.root = Node.merge(self.root, Node(key))

    def pop(self):
        t, k = self.root, self.root.key
        self.root = Node.merge(t.left, t.right)
        del t
        return k

    def __iadd__(self, other):
        self.root = Node.merge(self.root, other.root)
        other.root = None
        return self

if __name__ == '__main__':
    a = SkewHeap()
    for i in [1,2,3]:
        a.push(i)
    b = SkewHeap()
    for i in [0,4,5]:
        b.push(i)
    a += b
    for i in xrange(6):
        print a.pop(),
