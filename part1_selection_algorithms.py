def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians)//2)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))