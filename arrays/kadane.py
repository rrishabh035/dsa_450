# # Maximum Subarray Sum: Kadane’s Algorithm

def brute_force_max_subarray(arr, n):
    max_sum = float("-inf")
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]

            if(current_sum > max_sum):
                max_sum = current_sum

    return max_sum


def kadane_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n-1):
        current_sum += arr[i]

        if (current_sum >= max_sum):
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


# 1, 3, 8, -2, 6, -8, 5
a = list(map(int, input("Please enter the comma seperated list").split(",")))
print(brute_force_max_subarray(a, len(a)))
print(kadane_sub_array_sum(a, len(a)))
