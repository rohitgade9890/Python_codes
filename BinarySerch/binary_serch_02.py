#find lower bound using binary serch
#u have to find index of number which is closest or closest greter than target no
arr=[2,5,12,12,12,12,12,18]
target=12 #>=12
#ans = 6  #no = 15
def lower_bound(arr,target):
    start=0
    end=len(arr)-1
    ans=len(arr)
    while start <= end:
        mid=(start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            ans = mid
    return ans
print(lower_bound(arr,target))

arr = [2,5,12,12,12,12,12,18]
target = 12

def lower_bound(arr, target):
    start = 0
    end = len(arr) - 1
    ans = len(arr)         # standard "not found" sentinel for lower_bound
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            ans = mid      # possible answer, try to find a smaller index
            end = mid - 1
        else:
            start = mid + 1
    return ans

print(lower_bound(arr, target))