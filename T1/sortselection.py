def BubbleSort(A):
  sorted = False
  
  while not sorted:
    sorted = True
    for i, num in enumerate(A):
      if i+1 == len(A):
        break
      nextNum = A[i+1]
      if num > nextNum:
        A[i] = nextNum
        A[i+1] = num
        sorted = False
  return A
        

def sortSelection(A, k):
  aOrd = BubbleSort(A)
  return aOrd[k-1]