import math

def binary_search(list, item):
  low = 0
  high = len(list)-1

  while low <= high:
    mid = math.floor((low + high) / 2)
    print(('low: ' + str(low) + ', high: ' + str(high)))
    guess = list[mid]
    print(('position:' + str(mid) + ', value:' + str(guess) + '\n'))

    if guess == item:
      return item
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return None
  
def qsort(arr: list):
	if len(arr) < 2:
		return arr
	else:
		mid = math.floor(len(arr)/2)
		pivot = arr[mid]
		del arr[mid]
		less = [i for i in arr if i <= pivot]
		greater = [i for i in arr if i > pivot]
		return qsort(less)+[pivot]+qsort(greater)


arr = [1, 2, 32, 3, 4, 6, 0, 7, 8, 9, 10, 24, 57, 248]
list = qsort(arr)
print(list)
result = binary_search(list, 7)
print(result)
print('_______')
result2 = binary_search(list, 726)
print(result2)

