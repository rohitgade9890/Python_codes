#sort an array of 0's 1's and 2's
#bruteforce
arr=[0,2,2,1,0,0,1,1]
def sortt(arr):
    cnt0=0
    cnt1=0
    cnt2=0
    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    for x in range(cnt0):
        arr[x] = 0
    for y in range(cnt0,cnt0+cnt1):
        arr[y] = 1
    for z in range(cnt0+cnt1,cnt2+cnt1+cnt0):
        arr[z] = 2
    return arr
print(sortt(arr))

#optimized
#sort arrays of 0's 1's and 2's
#using dutch national flag algo
arr=[0,0,2,1,1,2,0,1,2]
def sort(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high -= 1
    return arr
print(sort(arr))