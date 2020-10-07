def sort_and_count_inversions(a, b, n):
    mid = len(a) / 2

    if mid == 0:
        return a, n

    first_half, n = sort_and_count_inversions(a[:mid], b, n)
    second_half, n = sort_and_count_inversions(a[mid:], b, n)

    i = 0 # First half iterator.
    j = 0 # Second half iterator.
    i_len = mid
    j_len = len(second_half)
    joined = []
    inv = 0

    while i < i_len and j < j_len:
        if first_half[i]['val'] <= second_half[j]['val']:
            joined.append(first_half[i])
            b[first_half[i]['idx']] += inv
            i += 1
        else:
            joined.append(second_half[j])
            j += 1
            inv += 1
            n += i_len - i

    first_half_rest = first_half[i:]

    for x in first_half_rest:
        b[x['idx']] += inv

    joined += first_half_rest + second_half[j:]

    return joined, n

def main():
    f = open('data/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt')
    a = 'RAHUL'
    a = list(a)
    a_len = len(a)

    for i in range(a_len):
        a[i] = { 'idx': i, 'val': a[i] }

    b = [0] * len(a)
    f.close()

    sorted_a, n = sort_and_count_inversions(a, b, 0)
    print b

if __name__ == '__main__':
    main()