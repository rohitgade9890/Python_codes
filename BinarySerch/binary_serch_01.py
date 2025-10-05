#binary serch lecture 1
#we implement binary serch to reduct serching time if array is sorted
#find index where number appers in arr
arr=[3,4,6,7,9,12,16,17]
target=4
def find_num(arr,k):
    start=0
    end=len(arr)-1
    
    while start <= end:
        mid=(start+end)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end=mid-1
        else:
            start=mid+1
    return -1
print(find_num(arr,target))

#find index where number is present in list using binary serch
#recursive method
arr=[2,5,6,7,8,11,15,18]
target=12
start=0
end=len(arr)-1
def find_num_recursive(arr,start,end,target):
    if start > end:
        return -1
    else:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return find_num_recursive(arr,mid+1,end,target)
        else:
            return find_num_recursive(arr,start,mid-1,target)
print(find_num_recursive(arr,start,end,target))