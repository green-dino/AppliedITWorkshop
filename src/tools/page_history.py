from collections import deque

# Define a tuple named 'sites', containing three string URLs.
sites = ('google.com', 'yahoo.com', 'bing.com')

# Initialize an empty Deque named 'pages' with a maximum length of 5 elements, using the maxlen attribute provided by Deque.
pages = deque(maxlen=5)

# Print the maximum length value of the 'pages' Deque, obtained using its maxlen attribute.
print(pages.maxlen)

# Add URLs from the 'sites' tuple to the front of the 'pages' Deque using afor loop and the appendleft() method provided by Deque.
for site in sites:
    pages.appendleft(site)

# Print the current contents of the 'pages' Deque, obtained using its print() method.
print(pages)