# K’th smallest element in an unsorted array using sorting:
from heap import MinHeap, MaxHeap


def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]


def kth_smallest_using_set(arr, k):
    s = set(arr)

    for i in s:
        if k == 1:
            return i
        k -= 1


def find_kth_min_heap(arr, n, k):
    heap_obj = MinHeap(arr, n)

    for i in range(k-1):
        heap_obj.extract_min()

    return heap_obj.extract_min()


def find_kth_max_heap(arr, n, k):
    heap_obj = MaxHeap(arr, k)

    for i in range(k, n):
        if heap_obj.getMax() > arr[i]:
            heap_obj.replaceMax(arr[i])

    return heap_obj.getMax()


def quick_sort_partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[r], arr[i] = arr[i], arr[r]
    return i


def quick_sort_find_kth_smallest(arr, l, r, k):
    if r - l + 1 >= k:
        pos = quick_sort_partition(arr, l, r)
        if pos - l == k-1:
            return arr[pos]
        if(pos - l > k-1):
            return quick_sort_find_kth_smallest(arr, l, pos-1, k)
        return quick_sort_find_kth_smallest(arr, pos+1, r, k-pos+l - 1)


arr = [12, 3, 5, 7, 4, 19, 26]
N = len(arr)
K = 4
print("K'th smallest element is", quick_sort_find_kth_smallest(arr, 0, N - 1, K))
print("K'th smallest element is", find_kth_max_heap(arr, N, K))
print("K'th smallest element is", find_kth_min_heap(arr, N, K))
print("K'th smallest element is", kth_smallest_using_set(arr, K))
print("K'th smallest element is", kth_smallest(arr, K))
