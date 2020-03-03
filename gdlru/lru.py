"""
This example is based on an exercise available at:
https://leetcode.com/problems/lru-cache/submissions/
"""


from collections import Counter
from tqdm import tqdm


# Simple generator that yields the next sequential id number
def access_counter():
    i = 0
    while True:
        yield i
        i += 1


class LRUCache:
    def __init__(self, capacity: int):
        # Our database. Can be linked directly to mongo
        self.d = {}
        # Capacity of the cache
        self.capacity = capacity
        # Hacking the access ledger around the Counter() class since it lets us use the most_common() function
        self.access_ledger = Counter()
        # Instance of the generator producing unique access IDs
        self.access_id = access_counter()

    def get(self, key: int) -> int:
        # Get the response from the database
        answer = self.d.get(key, -1)
        # Update the ledger if relevant
        if answer != -1:
            self.access_ledger[key] = next(self.access_id)
        return answer

    def get_stale_key(self):
        # Find a stale key in the DB
        # By finding the difference between the d.keys() & access_ledger.keys()
        # we get a set of keys that are in the DB but not in the ledger
        difference_set = self.d.keys() - self.access_ledger.keys()

        # If the difference_set is non-empty, we can clear any of the keys in the
        # difference set to free up capacity
        if len(difference_set) > 0:
            return difference_set.pop()
        # Otherwise, we'll just return the "least_common" key in the ledger
        # Note: since we're abusing the behavior of the Counter() class, the
        # most common key is the most recently accessed. Furthermore, the least
        # common key is actually the oldest key in the ledger
        else:
            freq_count = self.access_ledger.most_common()
            return freq_count[-1][0]

    def put(self, key: int, value: int) -> None:
        # If we are out of capacity, find a stale key and remove it from the db
        if len(self.d) >= self.capacity and key not in self.d.keys():
            stale_key = self.get_stale_key()
            del self.d[stale_key]
            del self.access_ledger[stale_key]

        # Add the new key, value pair to the DB and update the ledger
        self.d[key] = value
        self.access_ledger[key] = next(self.access_id)