# Find the duplicate in an array of N+1 integers

def find_duplicates(arr, n):
    arr.sort()
    for i in range(n-1):
        if arr[i+1] == arr[i]:
            return arr[i]
    return -1


def frequency_arr(arr, n):
    f_a = [0] * (n+1)

    for i in range(n):
        if f_a[arr[i]] == 0:
            f_a[arr[i]] += 1
        else:
            return arr[i]

    return -1


# floyd warshall in array
def floy_warshall_duplicate_array(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


a = list(map(int, input("Please enter the comma seperated list").split(",")))

print(find_duplicates(a, len(a)))
print(frequency_arr(a, len(a)))
print(floy_warshall_duplicate_array(a))
