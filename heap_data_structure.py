class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap)-1) #yeni index sayısı ile yığında aşağıdan yukarı tekrar sıralama işlemi
    def delete(self):
        if(len(self.heap) == 0):
            return None
        if (len(self.heap) == 1):
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    
    def _heapify_up(self,index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index] , self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    def _heapify_down(self,index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    

# Örnek kullanım
max_heap = MaxHeap()
max_heap.insert(12)
max_heap.insert(11)
max_heap.insert(13)
max_heap.insert(5)
max_heap.insert(6)
max_heap.insert(7)

print("Max Heap:")
print(max_heap.heap)

# Kök düğümü kaldır
print("Kök düğümü kaldırıldı:", max_heap.delete())
print("Max Heap güncellendi:")
print(max_heap.heap)
'''
3,9,2,1,4,5
0,1,2,3,4,5

         9
        / \
       4     5
      / \   / \
    1    3  2  7 
'''