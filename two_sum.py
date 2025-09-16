#check wether sum of two numbers from array makes target return true or false
#bruteforce
arr=[2,34,2,53,2,4,7,8,4]
target=8
def two_sum(arr,target):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] + arr[y] == target:
                return True
    return False
print(two_sum(arr,target))



#check wether sum of two numbers from array makes target return indexes
#bruteforce
arr=[2,34,2,53,2,4,7,8,4]
target=8
def two_sum(arr,target):
    res=[]
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] + arr[y] == target:
                res.append([x,y])
    return res
print(two_sum(arr,target))