from sys import path

path.append('../utils')

from utils import swap
from math import ceil

def get_parent_idx(i):
    return int(ceil(i / 2.0)) - 1

def get_child_indices(i):
    i_2 = i * 2
    return i_2 + 1, i_2 + 2

# Simple min-heap, only deals with size-2 tuples (key, value)
class MinHeap:
    def __init__(self, s = None):
        self.data = []
        self.size = 0

        if s: # Assumes s is a size-2 tuple.
            self.insert(s)

    def insert(self, x):
        self.data.append(x)

        i = self.size

        while i > 0:
            parent_idx = get_parent_idx(i)

            if self.data[parent_idx][0] > x[0]:
                swap(self.data, i, parent_idx)
                i = parent_idx
            else:
                break

        self.size += 1 # Do this at end since 0-indexed array.

    # Will throw IndexError if heap has 0 items.
    def extract_min(self):
        ret = self.data[0]
        self_last = self.data.pop()
        self.size -= 1 # Do this at beginning since 0-indexed array.

        if not self.data:
            return ret

        self.data[0] = self_last

        i = 0

        while i < self.size:
            child_i, child_j = get_child_indices(i)
            child_i_key = float('inf')
            child_j_key = float('inf')

            if child_i < self.size:
                child_i_key = self.data[child_i][0]

            if child_j < self.size:
                child_j_key = self.data[child_j][0]

            min_child_key = min(child_i_key, child_j_key)

            if min_child_key < self.data[i][0]:
                if min_child_key == child_i_key:
                    swap(self.data, i, child_i)
                    i = child_i
                else:
                    swap(self.data, i, child_j)
                    i = child_j
            else:
                break

        return ret