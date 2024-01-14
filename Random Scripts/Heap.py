class MinHeap:
    def __init__(self):
        self.heap = []

    # calculate the index of a node's parent
    def parent(self, index):
        return (index - 1) // 2

    # calculate the index of a node's left child
    def left_child(self, index):
        return 2 * index + 1

    # calculate the index of a node's right_child
    def right_child(self, index):
        return 2 * index + 2

    # check if a node at a given index has a parent
    def has_parent(self, index):
        return self.parent(index) >= 0

    # check if a node at a given index has a left child
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    # check if a node at a given index has a right child
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)

    # return the number of elements in a heap
    def size(self):
            return len(self.heap)

    # check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # string representation of a heap
    def __str__(self):
        return str(self.heap)

    # swap the heap elements
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    # heapify up
    def heapify_up(self, index):
        # compare the value to its parent and swap if necessary
        # repeat until the heap property is satisfied or item reaches the root of the heap
        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index
            
    # heapify down
    def heapify_down(self, index):
        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)
            if self.has_right_child(index) and self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index
    # heap from array
    def heapify(self, array):
        # build a new heap from the given array
        self.heap = array
        # heapify from the last non-leaf node and move up to the root
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    # insert into a heap
    def insert(self, value):
        # insert at the end of the heap
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
        
    
    # delete from a heap
    def pop(self):
        # check if the heap is empty
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        # if the heap has only one element, just remove it
        if len(self.heap) == 1:
            return self.heap.pop()
        # in case of heap with more than one element
        root = self.heap[0]
        # remove the last element
        self.heap[0] = self.heap.pop()
        # maintain the heap property
        self.heapify_down(0)
        return root
    
# Example implementation
heap = MinHeap()
list1 = [15, 16, 25, 5, 12]
heap.heapify(list1)
print(heap)
