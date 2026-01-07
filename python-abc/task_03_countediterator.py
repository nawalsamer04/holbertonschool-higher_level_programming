#!/usr/bin/env python3
"""Task 3: CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    """Iterator wrapper that counts how many items have been fetched."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        return self.count
