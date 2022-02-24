#https://practice.geeksforgeeks.org/problems/heap-sort/1/


class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        self.swim(arr, n, i)
        self.sink(arr, n, i)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n):
            self.swim(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        while n > 0:
            self.remove(arr, n, 0)
            n -= 1
        arr.reverse()

    def swim(self, heap, n, index):
        curr_node = index
        curr_parent = self.parent(curr_node)
        while curr_node and heap[curr_parent] > heap[curr_node]:
            heap[curr_parent], heap[curr_node] = heap[curr_node], heap[curr_parent]
            curr_node = curr_parent
            curr_parent = self.parent(curr_node)

    def sink(self, heap, n, index):
        curr = index
        left = self.leftChild(curr)
        right = self.rightChild(curr)
        min_idx = left
        if min_idx >= n:
            return
        if right < n and heap[left] > heap[right]:
            min_idx = right

        if heap[curr] > heap[min_idx]:
            heap[min_idx], heap[curr] = heap[curr], heap[min_idx]
            self.sink(heap, n, min_idx)

    def insert(self, heap, element, n):
        heap[n] = element
        self.swim(heap, n + 1, n)

    def remove(self, heap, n, index):
        heap[n-1], heap[index] = heap[index], heap[n-1]
        self.heapify(heap, n-1, index)

    def update(self, heap, val, n, index):
        heap[index] = val
        self.heapify(heap, n, index)

    def getMin(self, heap):
        if len(heap):
            return heap[0]

    # Helper functions

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index-1) // 2
