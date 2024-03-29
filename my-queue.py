class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the first item from the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the size of the queue.
        """
        return len(self.items)

    def peek(self):
        """
        Returns the first item in the queue without removing it.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())
print("Front of the queue:", q.peek())

print("Dequeue:", q.dequeue())
print("Front of the queue after dequeue:", q.peek())
