#Check if an array is sorted and rotated.
arr=[2,4,6]
def is_sorted(arr):
    flag=True
    for x in range(1,len(arr)):
        if arr[x] < arr[x-1]:
            flag=False
            break
    return flag
print(is_sorted(arr))