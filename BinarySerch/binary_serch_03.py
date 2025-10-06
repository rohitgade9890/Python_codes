#find first and last occurance in an array
arr=[2,11,4,23,3,11,4,11]
target=11
def find_occurance(arr,k):
    first=-1
    last=-1
    for x in range(len(arr)):
        if arr[x] == k:
            if first == -1:
                first=x
            last=x
    return [first,last]
print(find_occurance(arr,target))

#if array is sorted we can use binary serch
arr=[2,4,6,8,8,8,11,13]       
k=8
def find_occurence_bs(arr,k):
    first=-1
    last=-1
    start=0
    end=len(arr)-1
    while start <= end:
        mid=(start+end)//2
        if arr[mid] == k:
            if first == -1 or first > mid:
                first=mid
            last=mid
            
        elif arr[mid] < k:
            start=mid+1
        else:
            end=mid-1
    return [first,last]

print(find_occurence_bs(arr,k))

