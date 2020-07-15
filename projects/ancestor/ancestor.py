
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    path = [starting_node]
    queue.enqueue(path)
    visited = set()
    while queue.size() > 0:
        p = queue.dequeue()
        np = []
        for element in p:
            for ancestor in ancestors:
                if ancestor[1] == element and element not in visited:
                    visited.add(element)
                    np.append(ancestor[0])
                    queue.enqueue(np)
        if len(np) <= 0:
            if p[0] == starting_node:
                return - 1
            else:
                return p[0]