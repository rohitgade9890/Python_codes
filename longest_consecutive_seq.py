#find longest consecutive sequence in an array and return its length
arr = [100, 4, 200, 1, 3, 2]

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
