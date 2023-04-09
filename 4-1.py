# sum up all elements of the array by recursion
import time


def sumup(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumup(arr[1:])


lst = range(1,333)

print(sumup(lst))
print(time.process_time())