import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        print(f'Heap : {self.minHeap}')
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # it will remove the smallest element from the heap 


    def add(self, val) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #first element in the heap is the kth largest element