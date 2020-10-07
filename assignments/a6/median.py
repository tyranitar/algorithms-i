from heapq import heappush, heappop

def median(a):
    inf = float('inf')

    max_heap = [inf]
    max_heap_len = 1
    min_heap = [inf]
    min_heap_len = 1

    median_sum = 0

    for x in a:
        median_lo = -max_heap[0]
        median_hi = min_heap[0]

        if x > median_lo and x < median_hi:
            # So we can assume x is not a median.
            median_lo = x
            x = -heappop(max_heap)
            heappush(max_heap, -median_lo)

        # Assume x is not a median.
        if x < median_lo:
            heappush(max_heap, -x)
            max_heap_len += 1
        else: # x > median_hi
            heappush(min_heap, x)
            min_heap_len += 1

        # Maintain invariance in relative heap sizes.
        if max_heap_len - min_heap_len > 1:
            heappush(min_heap, -heappop(max_heap))
            max_heap_len -= 1
            min_heap_len += 1
        elif min_heap_len > max_heap_len:
            heappush(max_heap, -heappop(min_heap))
            max_heap_len += 1
            min_heap_len -= 1

        median_sum += -max_heap[0]

    return median_sum % len(a)

def main():
    f = open('data/Median.txt')
    a = f.readlines()
    f.close()

    a = map(int, a)

    print median(a)

if __name__ == '__main__':
    main()