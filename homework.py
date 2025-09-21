#Check if an array is sorted and rotated.
nums=[2,4,6]
def check(nums):
    n=len(nums)
    cnt_breacks=0
    for x in range(len(nums)):
        if nums[x] > nums[(x+1) % n]:
            cnt_breacks += 1
    if cnt_breacks <=1:
        return True
    else:
        return False
    
#Find the maximum sum of a contiguous subarray
arr=[1,3,-2,3,-5,2,1,3]
def max_sum(arr):
    maxx_sum=float('-inf')
    summ=0
    start=0
    ans_start=-1
    ans_end=-1
    for x in range(len(arr)):
        if summ == 0:
            start = x
        summ += arr[x]
        if summ > maxx_sum:
            maxx_sum=summ
            ans_start=start
            ans_end=x
        if summ < 0:
            summ = 0
    return arr[ans_start:ans_end+1]
print(max_sum(arr))

#Count frequency of elements in an array
arr=['rohit','is','lazy','is','rohit','hardworking']
def cnt_freq(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(cnt_freq(arr))

#Find all pairs in an array that sum to a target.
arr=[1,2,5,4,4,1,3]
target=8
def two_sum(arr,k):
    seen=set()
    res=[]
    for x in range(len(arr)):
        num=arr[x]
        more_req=k-num
        if more_req in seen:
            res.append([more_req,num])
        seen.add(arr[x])
    return res
print(two_sum(arr,target))

#Remove duplicates from a sorted array in-place.
arr=[1,3,3,4,5,5,8]
def sortt(arr):
    pos=0
    for x in range(1,len(arr)):
        if arr[pos] != arr[x]:
            arr[pos+1] = arr[x]
            pos += 1
    return arr
print(sortt(arr))
        
