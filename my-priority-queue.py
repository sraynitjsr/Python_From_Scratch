class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority):
        """
        Adds an item to the priority queue based on priority.
        """
        self.items.append((item, priority))

    def dequeue(self):
        """
        Removes and returns the item with the highest priority.
        """
        if not self.is_empty():
            highest_priority_item = 0
            for i in range(1, len(self.items)):
                if self.items[i][1] < self.items[highest_priority_item][1]:
                    highest_priority_item = i
            return self.items.pop(highest_priority_item)
        else:
            print("Priority queue is empty")
            return None

    def peek(self):
        """
        Returns the item with the highest priority without removing it.
        """
        if not self.is_empty():
            highest_priority_item = 0
            for i in range(1, len(self.items)):
                if self.items[i][1] < self.items[highest_priority_item][1]:
                    highest_priority_item = i
            return self.items[highest_priority_item]
        else:
            print("Priority queue is empty")
            return None

    def size(self):
        """
        Returns the size of the priority queue.
        """
        return len(self.items)

pq = PriorityQueue()
pq.enqueue('A', 3)
pq.enqueue('B', 1)
pq.enqueue('C', 2)

print("Priority Queue size:", pq.size())
print("Front of the Priority Queue:", pq.peek())

print("Dequeue:", pq.dequeue())
print("Front of the Priority Queue after dequeue:", pq.peek())
