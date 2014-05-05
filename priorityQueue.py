''' Priority queue implemented by heap.
    Some codes are copied from the official library heapq.
    Priority changes for queue item is possible and fast. '''


class PQ:
    def __init__(self):
        self.heap = []
        self.priority = {}
        self.position = {}

    def _siftdown(self, startpos, pos):
        ''' lift up item from pos until startpos '''
        heap, prio = self.heap, self.priority
        newitem = heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if prio[newitem] < prio[parent]:
                heap[pos] = parent
                self.position[parent] = pos
                pos = parentpos
                continue
            break
        heap[pos] = newitem
        self.position[newitem] = pos

    def _siftup(self, pos):
        ''' sink down item at pos '''
        heap, prio = self.heap, self.priority
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and prio[heap[childpos]] > prio[heap[rightpos]]:
                childpos = rightpos
            heap[pos] = heap[childpos]
            self.position[heap[childpos]] = pos
            pos = childpos
            childpos = 2*pos + 1
        heap[pos] = newitem
        self.position[newitem] = pos
        self._siftdown(startpos, pos)

    def push(self, item, priority):
        self.heap.append(item)
        self.priority[item] = priority
        self.position[item] = len(self.heap)-1
        self._siftdown(0, len(self.heap)-1)

    def contains(self, item):
        return item in self.position

    def get_priority(self, item):
        return self.priority[item]

    def change_priority(self, item, new_priority):
        old_priority = self.priority[item]
        self.priority[item] = new_priority
        if new_priority < old_priority:
            self._siftdown(0, self.position[item])
        else:
            self._siftup(self.position[item])

    def pop(self):
        lastitem = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastitem
            self.position[lastitem] = 0
            self._siftup(0)
        else:
            returnitem = lastitem
        prio = self.priority[returnitem]
        del self.priority[returnitem]
        del self.position[returnitem]
        return returnitem, prio


if __name__ == '__main__':
    ''' test '''
    pq = PQ()
    import random
    queue = zip('abcdefghi', '123456789')
    random.shuffle(queue)
    for item, prio in queue:
        pq.push(item, prio)
    a = random.choice(queue)
    print a[0], 'in pq:', pq.contains(a[0])
    print 'priority of it:', pq.get_priority(a[0])
    b = random.choice(queue)
    print 'swap priority of ', a, b
    pq.change_priority(a[0], b[1])
    pq.change_priority(b[0], a[1])
    for i in xrange(len(queue)):
        item, prio = pq.pop()
        print item, prio