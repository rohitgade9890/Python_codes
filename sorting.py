#sort an array using selection sort
arr=[21,4,21,6,34,11]
def selection_sort(arr):
    for x in range(len(arr)-1):
        min_index=x
        for y in range(x+1,len(arr)):
            if arr[y] < arr[min_index]:
                min_index=y
        arr[x],arr[min_index]=arr[min_index],arr[x]
    return arr
print(selection_sort(arr))

arr1=[21,4,21,6,34,11]
def bubble_sort(arr):
    for x in range(len(arr)-1,-1,-1):
        for y in range(x):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1]=arr[y+1],arr[y]
    return arr
print(bubble_sort(arr1))

#notebook teached version 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):   # go till the unsorted part
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
