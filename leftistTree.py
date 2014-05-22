from Queue import deque

class Node(object):
    __slots__ = 'key left right dist'.split()

    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.dist = 0

    @staticmethod
    def merge(a, b):
        if a is None:
            return b
        if b is None:
            return a
        else:
            if a.key > b.key: # min heap
                a, b = b, a
            a.right = Node.merge(a.right, b)
            if a.left is None or a.right.dist > a.left.dist:
                a.left, a.right = a.right, a.left
            a.dist = 0 if a.right is None else a.right.dist + 1
            return a

class LeftistTree:

    def __init__(self, l=None):
        if not l:
            self.root = None
            return
        q = deque(map(Node, l))
        while len(q) > 1:
            a, b = q.popleft(), q.popleft()
            q.append(Node.merge(a, b))
        self.root = q.pop()

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
    a = LeftistTree([1,2,3])
    b = LeftistTree([0,4,5])
    a += b
    for i in xrange(6):
        print a.pop(),
