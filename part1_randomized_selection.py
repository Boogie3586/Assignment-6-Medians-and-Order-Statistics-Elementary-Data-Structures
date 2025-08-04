import random

def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def quickselect(arr, k):
    def select(low, high):
        if low == high:
            return arr[low]
        pivot_index = random.randint(low, high)
        pivot_index = partition(arr, low, high, pivot_index)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(low, pivot_index - 1)
        else:
            return select(pivot_index + 1, high)
    return select(0, len(arr) - 1)