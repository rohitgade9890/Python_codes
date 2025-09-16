#check wether sum of two numbers from array makes target return true or false
arr=[2,34,2,53,2,4,7,8,4]
target=8
def two_sum(arr,target):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] + arr[y] == target:
                return True
    return False
print(two_sum(arr,target))