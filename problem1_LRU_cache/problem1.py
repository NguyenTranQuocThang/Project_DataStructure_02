
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict({})
        self.history = dict({})

    def get(self, key):
        value = self.dict.get(key)
        if value == None:
            return -1
        else:
            # if key in self.history:
            self.history[key] = self.history[key] + 1
            # else:
            #     self.history[key] = 1
            return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if(self.capacity == len(self.history)):
            min_val = min(self.history, key=self.history.get)
            self.history.pop(min_val)
            self.dict.pop(min_val)

        self.dict[key] = value

        self.history[key] = 0


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(7, 7)
print(our_cache.get(4))  # return - 1

# Test Case 2
our_cache.set(None, "")
print(our_cache.get(None))  # return ' '
print(our_cache.get(5))    # return -1

# Test Case 3
our_cache.set(None, None)
# return 9999999999999999999
our_cache.set(9999999999999999999, 9999999999999999999)
print(our_cache.get(9999999999999999999))
