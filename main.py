import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


data_sizes = [100, 1000, 10000]

for size in data_sizes:
    data = [random.randint(0, 1000) for _ in range(size)]

    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=10)

    print(f"Data size: {size}")
    print("Merge Sort execution time:", merge_sort_time)
    print("Insertion Sort execution time:", insertion_sort_time)
    print("Timsort execution time:", timsort_time)
    print()


def merge_k_lists(lists):
    merged = []
    while any(lists):
        min_val = float('inf')
        min_idx = -1
        for i, lst in enumerate(lists):
            if lst and lst[0] < min_val:
                min_val = lst[0]
                min_idx = i
        merged.append(lists[min_idx].pop(0))
    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
