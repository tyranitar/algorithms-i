from sets import Set

# Naive but perhaps the best solution...
def two_sum_naive(a, lo, hi):
    a_set = Set(a)
    t_set = Set()
    a = list(a_set) # Ensures distinctness.

    t_interval = range(lo, hi + 1)

    for t in t_interval:
        for x in a:
            if ((t - x) in a_set) and (x != (t - x)) and (t not in t_set):
                t_set.add(t)

    return len(t_set)

# Assumes sorted, non-empty array
# Returns index and value of closest element.
def binary_search_closest(a, x):
    highest = len(a) - 1

    lo = 0
    hi = highest
    mid = (lo + hi) / 2

    val = a[mid]

    while lo < hi:
        if x == val:
            return mid, val
        elif x < val:
            hi = mid - 1
        else:
            lo = mid + 1

        # These need to be set after the above lo and hi assignments.
        mid = min(max((lo + hi) / 2, 0), highest)
        val = a[mid]

    return mid, val

# TODO: WIP, doesn't quite work...
def two_sum(a, lo, hi):
    a = sorted(list(Set(a))) # Ensures distinctness.

    t_set = Set()
    idx = 0

    for x in a:
        lo_x = lo - x
        hi_x = hi - x

        i, i_val = binary_search_closest(a, lo_x)
        j, j_val = binary_search_closest(a, hi_x)

        # Edges.
        if i_val >= lo_x and x != i_val:
            t_set.add(x + i_val)
        if j_val <= hi_x and x != j_val:
            t_set.add(x + j_val)

        # In-betweens.
        for k in range(i + 1, j):
            if k != idx:
                t_set.add(x + a[k])

        idx += 1

    return len(t_set)

# "Optimal" solution as per Stack Overflow.
def two_sum_optimal(a, lo, hi):
    a_set = Set(a)

    return sum(any(t - x in a_set and 2 * x != t for x in a_set) for t in range(lo, hi + 1))

def main():
    f = open('data/algo1-programming_prob-2sum.txt')
    a = f.readlines()
    f.close()

    a = map(int, a)
    print two_sum_naive(a, -10000, 10000)

if __name__ == '__main__':
    main()