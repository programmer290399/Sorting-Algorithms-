from random import randint
numbers = [randint(1,1000) for i in range(10000)]

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]
  return

def shell_sort(arr, step):
  while step >= 1:
    for x in range(step):
      for i in range(x, len(arr) - step, step):
        if arr[i] > arr[i+step]:
          swap(arr, i, i+step)
          for j in range(i, x, -step):
            if arr[j] < arr[j-step]:
              swap(arr, j, j-step)
            else:
              break
    step //= 2
  return arr