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
