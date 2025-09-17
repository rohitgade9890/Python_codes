#left rotate the array by k place
arr = [23,4,2,6,34]
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    return arr
print(rotateArr(arr,2))

#right rotate
arr = [23,4,2,6,34]
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, n - d, n - 1)
    reverse(arr, 0, n - d - 1)
    reverse(arr, 0, n - 1)
    return arr
print(rotateArr(arr,2))