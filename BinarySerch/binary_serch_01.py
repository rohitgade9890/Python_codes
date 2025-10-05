#find index where number is present in list using binary serch
arr=[2,5,6,7,8,11,15,18]
target=11
def find_num(arr):
    arr.sort()
    start=0
    end=len(arr)-1
    while start <= end:
        mid=(start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
print(find_num(arr))