from collections import deque

class Queue:
    # Constructor to initialize an empty deque as the underlying storage
    def __init__(self):
        self._elements = deque()

    # Append element to the end of the queue using the append() method of deque
    def enqueue(self, element):
        self._elements.append(element)

    # Remove and return the element at the front of the queue using the pop() method with a left argument of 0 (first element) for deque
    def dequeue(self):
        return self._elements.popleft()
    
    # Add an iterator using the built-in iter() function to return an iterator over the elements in the queue
    def __iter__(self):
        return iter(self._elements)

    # Return the number of elements in the queue using the len() method for deque
    def __len__(self):
        return len(self._elements)

    # Reverse the order of the elements in the queue using the reversed() function with the underlying storage as an argument
    def __reversed__(self):
        return reversed(self._elements)

    # Check if a given element is present in the queue using the built-in in keyword and operator for set membership
    def __contains__(self, element):
        return element in self._elements