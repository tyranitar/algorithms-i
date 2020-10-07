def in_place_swap(arr, i1, i2):
    if arr[i1] != arr[i2]:
        diff = arr[i1] - arr[i2]
        arr[i1] = arr[i2]
        arr[i2] = arr[i2] + diff

def merge_sort(arr, lo = 0, hi = len(arr) - 1):
    mid = (hi - lo) / 2

    # Base case.
    if mid == 0:
        if arr[lo] > arr[hi]:
            in_place_swap(arr, lo, hi)
        return

    merge_sort(arr, lo, mid)
    merge_sort(arr, mid + 1, hi)

    #