from heap import Heap

def linearSelection(A, k):
  size = len(A)
  
  if k <= 0 or k > size:
    raise Exception("k está fora dos limites da lista.")
  
  if size <= 5:
    A.sort()
    return A[k - 1]

  groups = size // 5
  if (size % 5) != 0:
    groups += 1

  partitions = []
  list
  for i in range(0, groups):
    heap = Heap(A[i*5:i*5+5])
    partitions.append(heap.heapSort())

  medianSet = []
  for partition in partitions:
    medianSet.append(partition[len(partition)//2])
  medianSet.sort()
  
  median = linearSelection(medianSet, len(medianSet)//2)

  leftPartition = []
  rightPartition = []
  equalPartition = []
  for num in A:
    if num < median:
      leftPartition.append(num)
    elif num > median:
      rightPartition.append(num)
    else:
      equalPartition.append(num)

  lSize = len(leftPartition)
  rSize = len(rightPartition)
  eSize = len(equalPartition)
  
  if lSize == 0 and rSize == 0:
    return median
  
  if lSize == k - 1 or (k > lSize and k <= (lSize + eSize)):
    return median
  if lSize > k - 1:
    return linearSelection(leftPartition, k)
  else:
    return linearSelection(rightPartition, k - lSize - eSize)