def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)-1):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_ind = findSmallest(arr)
        newArr.append(arr.pop(smallest_ind))
    return newArr

a = [55, 66 , 33, 12, 45, 87, 5, 3, 45, 99, 0, 111111, 99, 8, 78, 786]
b = a[:]

print(selectionSort(b))
print(a[findSmallest(a)])