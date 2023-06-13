class MinHeap:
    def __init__(self, arr, size):
        self.heap = arr
        self.size = size
        for i in range(self.size//2, -1, -1):
            self.heapify(i)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def heapify(self, i):
        smallest = i
        left_node = self.left(i)
        right_node = self.right(i)

        if self.size > left_node and self.heap[smallest] > self.heap[left_node]:
            smallest = left_node

        if self.size > right_node and self.heap[smallest] > self.heap[right_node]:
            smallest = right_node

        self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]

        if smallest != i:
            self.heapify(smallest)

    def extract_min(self):
        minimum_element = float('-inf')
        if self.size > 0:
            minimum_element = self.heap[0]
            self.heap[0], self.heap[self.size -
                                    1] = self.heap[self.size - 1], self.heap[0]
            self.size -= 1
            self.heapify(0)

        return minimum_element


class MaxHeap:
    def __init__(self, arr, size):
        self.heap = arr
        self.size = size
        for i in range(self.size//2, -1, -1):
            self.heapify(i)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def heapify(self, i):
        largest = i
        left_node = self.left(i)
        right_node = self.right(i)

        if self.size > left_node and self.heap[largest] < self.heap[left_node]:
            largest = left_node

        if self.size > right_node and self.heap[largest] < self.heap[right_node]:
            largest = right_node

        self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]

        if largest != i:
            self.heapify(largest)

    def getMax(self):
        return self.heap[0]

    def replaceMax(self, num):
        self.heap[0] = num
        self.heapify(0)
