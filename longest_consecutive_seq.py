#find longest consecutive sequence in an array and return its length
arr = [100, 4, 200, 1, 3, 2,2]

def longestSuccessiveElements(nums):
    nums.sort()  
    n = len(nums)
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1
    
    for i in range(n):
        if nums[i] - 1 == lastSmaller:
            cnt += 1
            lastSmaller = nums[i]
        elif lastSmaller != nums[i]:
            cnt = 1
            lastSmaller = nums[i]
        
        longest = max(longest, cnt)
    return longest
print(longestSuccessiveElements(arr))


#easy approach
arr = [100, 4, 200, 1, 3, 2,2,2]

def longestSuccessiveElements(nums):
    nums.sort()  
    last_smaller=nums[0]
    cnt=1
    max_cnt=1
    for x in range(1,len(nums)):
        if nums[x] == last_smaller:
            continue
        if nums[x] - 1 == last_smaller:
            cnt += 1
        else:
            cnt = 1
        max_cnt=max(max_cnt,cnt)
        last_smaller=arr[x]
    return max_cnt
print(longestSuccessiveElements(arr))
