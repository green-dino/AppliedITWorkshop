from collections import deque 
from time import perf_counter

# Define TIMES, which represents the number of times the function will beexecuted to calculate average time.
TIMES = 100_000

# Initialize an empty list and deque data structures with the same name 'a'.
a_list = []
a_deque = deque()

# Define a helper function named 'average_time' that takes in a function andnumber of times as arguments,
# calculates the total time taken by executing the passed function 'times' number of times,
# returns the average time taken by the function per execution.
def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    return total / times

# Define two lambda functions to be passed as arguments to the 'average_time' function, one for list.insert() and another for deque.appendleft().
list_time = average_time(lambda i: a_list.insert(0,i), TIMES)
deque_time = average_time(lambda i: a_deque.appendleft(i), TIMES)

# Calculate the gain in performance of list.insert() over deque.appendleft() by dividing the time taken by list.insert() by the time taken by deque.appendleft().
gain = list_time / deque_time

# Print the average time taken for list.insert() and deque.appendleft(), along with the calculated gain in performance.
print(f"list.insert()   {list_time:.6} ns")
print(f"deque.appendleft()  {deque_time:.6} ns ({gain:.6}x faster)")