from collections import deque

# Example: Queue Implementation
queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
queue.popleft()   # Dequeue
print(queue)
