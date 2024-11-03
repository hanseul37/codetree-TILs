n = int(input())
arr = list(map(int, input().split()))

def heapify(index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
  
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(largest, heap_size)

for i in range(n // 2 - 1, -1, -1):
    heapify(i, n)
for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(0, i)

for i in range(n):
    print(arr[i], end=' ')