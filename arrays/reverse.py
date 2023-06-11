# Write a program to reverse an array or string
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def recursive_reverse_array(a, start, end):
    if start >= end:
        return
    a[start], a[end] = a[end], a[start]
    recursive_reverse_array(a, start + 1, end - 1)


a = list(map(int, input("Please enter the comma seperated list").split(",")))
print("Before reversing the list ", a)
reverse_array(a, 0, len(a)-1)
print("After reversing the list", a)
recursive_reverse_array(a, 0, len(a)-1)
print("After recursive reversing the list", a)
