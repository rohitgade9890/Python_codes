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


#check wether sum of two numbers from array makes target return true or false
#optimized
arr = [2,34,2,53,2,4,7,8,4]
target = 8

def two_sum_set(arr, target):
    seen = set()
    for v in arr:
        if target - v in seen:
            return True
        seen.add(v)
    return False

print(two_sum_set(arr, target))

#check wether sum of two numbers from array makes target return True or False
#optimized
arr=[2,2,4,4,3,5]
target = 7

def two_sum(arr,target):
    hashmap={}
    for x in range(len(arr)):
        num=arr[x]
        more_needed=target - num
        if more_needed in hashmap:
            return True
        hashmap[num] = x
    return False
print('xxx')
print(two_sum(arr,target))
print('xxx')


#check wether sum of two numbers from array makes target return True or False
#optimized
arr=[2,2,4,4,3,5]
target = 7

def two_sum(arr,target):
    hashmap={}   
    for i in range(len(arr)):
        num=arr[i]
        moreNeeded =target-num
        if moreNeeded in hashmap:
            return [hashmap[moreNeeded],i]
        hashmap[num] = i
    return [-1,-1]

print(two_sum(arr,target))