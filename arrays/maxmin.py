# Maximum and minimum of an array using minimum number of comparisons

# will return a tuple of (min,max)
def minmax_using_sorting(arr):
    arr.sort()
    return (arr[0], arr[-1])


def minmax_linear_search(arr, n):
    maximum = 0
    minimum = 0
    if n == 1:
        maximum = minimum = arr[0]
        return (minimum, maximum)
    maximum, minimum = max(arr[0], arr[1]), min(arr[0], arr[1])
    for i in range(2, n):
        maximum, minimum = max(arr[i], maximum), min(arr[i], minimum)
    return (minimum, maximum)


def minmax_divide_conquer(arr, low, high):
    if low == high:
        return (arr[low], arr[low])
    elif low == high + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))
    else:
        n = (low + high)//2
        t1, t2 = minmax_divide_conquer(
            arr, low, n-1), minmax_divide_conquer(arr, n+1, high)
        return (min(t1[0], t2[0]), max(t1[1], t2[1]))


def minmax_pair_method(arr, n):
    is_even = n % 2 == 0
    minimum = maximum = 0
    if is_even:
        minimum, maximum = min(arr[0], arr[1]), max(arr[0], arr[1])
    else:
        minimum = maximum = arr[0]

    lost_element = 2 if is_even else 1

    for i in range(lost_element, n-1, 2):
        if arr[i] < arr[i+1]:
            maximum = max(arr[i+1], maximum)
            minimum = min(arr[i], minimum)
        else:
            maximum = max(arr[i], maximum)
            minimum = min(arr[i+1], minimum)
    return (minimum, maximum)


a = list(map(int, input("Please enter the comma seperated list").split(",")))
print(minmax_using_sorting(a))
print(minmax_linear_search(a, len(a)))
print(minmax_divide_conquer(a, 0, len(a)-1))
print(minmax_pair_method(a, len(a)))
