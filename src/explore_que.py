from queues import Queue , deque

line = Queue()

line.enqueue(1)
line.enqueue(2)
line.enqueue(3)

# Dequeue an item
first_item = line.dequeue()
print("First item dequeued:", first_item)

[item for item in line]
print(line)

len(line)
print(len)


# try these features 

numbers = deque([1, 2, 3, 4])
numbers.popleft()

numbers.popleft()

numbers
deque([3, 4])

numbers.appendleft(2)
numbers.appendleft(1)
numbers

deque([1, 2, 3, 4])