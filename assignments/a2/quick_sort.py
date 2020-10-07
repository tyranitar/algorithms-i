from math import ceil
from random import randint

def swap_in_place(a, i, j):
    if a[i] != a[j]:
        a[i] = a[i] - a[j]
        a[j] = a[j] + a[i]
        a[i] = a[j] - a[i]

def find_low(a, lo, hi):
    return a[lo], lo

def find_high(a, lo, hi):
    return a[hi - 1], hi - 1

def find_median(a, lo, hi):
    mid = int(ceil((hi + lo) / 2.0)) - 1
    median = sorted([(a[lo], lo), (a[mid], mid),  (a[hi - 1], hi - 1)])[1]
    return median[0], median[1] # Value, index.

# Bonus.
def find_random(a, lo, hi):
    rn = randint(lo, hi - 1)
    return a[rn], rn

def quick_sort(a, lo, hi, find_pivot):
    if hi - lo < 2:
        return 0

    pivot, pivot_idx = find_pivot(a, lo, hi)
    swap_in_place(a, lo, pivot_idx)

    i = lo + 1

    while i < hi and a[i] < pivot:
        i += 1

    j = i + 1

    while j < hi:
        if a[j] < pivot:
            swap_in_place(a, i, j)
            i += 1
        j += 1

    swap_in_place(a, lo, i - 1) # Place pivot where it belongs
    left_sum = quick_sort(a, lo, i - 1, find_pivot)
    right_sum = quick_sort(a, i, j, find_pivot)

    return hi - lo - 1 + left_sum + right_sum

def main():
    f = open('data/_32387ba40b36359a38625cbb397eee65_QuickSort.txt')
    a = map(int, f.readlines())
    f.close()
    a_len = len(a)

    a_1 = a[:]
    a_2 = a[:]
    a_3 = a[:]
    a_4 = a[:]

    print quick_sort(a_1, 0, a_len, find_low)
    print quick_sort(a_2, 0, a_len, find_high)
    print quick_sort(a_3, 0, a_len, find_median)
    print quick_sort(a_4, 0, a_len, find_random)

    print a_1 == a_2 == a_3 == a_4 == sorted(a)

if __name__ == '__main__':
    main()