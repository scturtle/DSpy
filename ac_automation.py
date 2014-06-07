from collections import deque
import sys

class Node:
    __slots__ = 'ch tran out fail'.split()
    def __init__(self, ch):
        self.ch, self.tran, self.out, self.fail = ch, {}, [], None
    def __repr__(self):
        return str(id(self))

class ACAutomation:
    def __init__(self, keywords):
        self.root = Node(None)

        # phase I: build trie tree
        for keyword in keywords:
            current_node = self.root
            for ch in keyword:
                if ch not in current_node.tran:
                    current_node.tran[ch] = Node(ch)
                current_node = current_node.tran[ch]
            current_node.out.append(keyword)

        # phase II: build 'out' and 'fail'
        q = deque([self.root])
        while q:
            current_node = q.popleft()
            for ch, node in current_node.tran.iteritems():
                q.append(node)
                fail_node = current_node.fail
                while fail_node and ch not in fail_node.tran:
                    fail_node = fail_node.fail
                node.fail = fail_node.tran[ch] if fail_node else self.root
                node.out += node.fail.out

    def count(self, s):
        ans = 0
        current_node = self.root
        for ch in s:
            while ch not in current_node.tran and current_node is not self.root:
                current_node = current_node.fail
            if ch in current_node.tran:
                current_node = current_node.tran[ch]
            else:
                current_node = self.root
            ans += len(current_node.out)
        return ans

    def show(self, root=None):
        if root is None:
            root = self.root
        print id(root), root.ch, root.tran, root.fail, root.out
        for child in root.tran.itervalues():
            self.show(child)

def main():
    ac = ACAutomation(['2', '32'])
    print ac.count('023223')

main()
