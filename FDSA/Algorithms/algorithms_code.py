# Some relevant code to the "Analysis of Algorithms Video" seen in
# the "Foundations of Data Structures and Algorithms" series

def bs_iterative(data, target):
  # Binary Search Iterative
  low = 0
  high = len(data)-1 
  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      high = mid − 1
    else:
      low = mid + 1
  return False