#rotate array by d to left

arr = [1,2,5,34,2,64,23]
def rotator(start,end,arr):
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start += 1
        end -= 1
    return arr
def left_rotator(arr,k):
    k=k%len(arr)
    rotator(0,k-1,arr)
    rotator(k,len(arr)-1,arr)
    rotator(0,len(arr)-1,arr)
    return arr
print(left_rotator(arr,2))

#move zeros to end
arr = [0,12,3,0,3,0,0,3]
def move_zeros(arr):
    pos=0
    for x in range(len(arr)):
        if arr[x] != 0:
            arr[x],arr[pos]=arr[pos],arr[x]
            pos += 1
    return arr
print(move_zeros(arr))

#linear serch
#Input: nums = [2, 3, 4, 5, 3], target = 3
#Output: 1
nums = [2, 3, 4, 5, 3]
target = 3
def find_index(nums,target):
    for x in range(len(nums)):
        if nums[x] == target:
            return x
    return -1
print(find_index(nums,target))

#union of two sorted arrays
arr1=[1,3,5,5,8]
arr2=[2,3,3,6,10]
def merge(arr1,arr2):
    res=[]
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not res or arr1[i] != res[-1]:
                res.append(arr1[i])
            i += 1
        else:
            if not res or arr2[j] != res[-1]:
                res.append(arr2[j])
            j += 1
    while i < len(arr1):
        if arr1[i] != res[-1]:
            res.append(arr1[i])
        i += 1
    while j < len(arr2):
        if arr2[j] != res[-1]:
            res.append(arr2[j])
        j += 1
    return res
print(merge(arr1,arr2))

arr1=[1,3,3,5,5,8]
arr2=[2,3,3,6,10]
#intersecion of two sorted arrays
def intersection(arr1,arr2):
    res=[]
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1
    return res
print(intersection(arr1,arr2))
