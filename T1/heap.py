class Heap:
  
  def __init__(self, data=None):
    self._data = []
    if data:
      for x in data:
        self.insert(x)

  def getMin(self):
    return self._data[0]

  def removeMin(self):
    first = self._data[0]
    last = self._data.pop()

    if self._data:
      self._data[0] = last
      self._heapifyDown(0)
    return first

  def insert(self, num):
    self._data.append(num)
    self._heapifyUp(len(self._data) - 1)

  def heapSort(self):
    copy = list(self._data)
    temp = Heap(copy)
    sorted_list = []
    while temp._data:
      sorted_list.append(temp.removeMin())
    return sorted_list

  def printHeap(self):
    print("Heap:")
    for num in self._data:
      print(f"{num} ", end='')
    print()

  def _heapifyUp(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self._data[index] < self._data[parent]:
        self._swap(index, parent)
        index = parent
      else:
        break

  def _heapifyDown(self, index):
    last_index = len(self._data) - 1
    while True:
      left = 2 * index + 1
      right = 2 * index + 2
      smallest = index

      if left <= last_index and self._data[left] < self._data[smallest]:
        smallest = left
      if right <= last_index and self._data[right] < self._data[smallest]:
        smallest = right
      if smallest != index:
        self._swap(index, smallest)
        index = smallest
      else:
        break

  def _swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]
