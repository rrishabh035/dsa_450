# Program to cyclically rotate an array by one
import reverse


def rotate(arr, n):
    last_element = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = last_element
    return arr


def rotate_two_pointers(arr, n):
    i = 0
    j = n-1
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


def rotate_by_slicing(arr):
    arr = arr[-1:] + arr[:-1]
    return arr


def reverse_rotations(arr, n):
    reverse.reverse_array(arr, 0, n-2)
    reverse.reverse_array(arr, 0, n-1)
    return arr


a = list(map(int, input("Please enter the comma seperated list").split(",")))

print("Rotations 1 :", rotate(a, len(a)))
print("Rotations 2 :", rotate_two_pointers(a, len(a)))
print("Rotations 3 :", rotate_by_slicing(a))
print("Before rotation:", a)
print("Rotations 4 :", reverse_rotations(a, len(a)))
