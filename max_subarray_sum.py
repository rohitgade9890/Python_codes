#maximum subarray sum return max sum
#bruteforce
arr=[-2,-3,4,-1,-2,1,5,-3]
def max_subarray_sum(arr):
    max_sum=0
    for x in range(len(arr)):
        current_sum=0
        for y in range(x,len(arr)):
            current_sum += arr[y]
            if current_sum > max_sum:
                max_sum=current_sum
    return max_sum
print(max_subarray_sum(arr))

#maximum subarray sum return array
arr=[-2,-3,4,-1,-2,1,5,-3]
def max_subarray_sum(arr):
    start=0
    end=0
    max_sum=0
    for x in range(len(arr)):
        current_sum=0
        for y in range(x,len(arr)):
            current_sum += arr[y]
            if current_sum > max_sum:
                max_sum=current_sum
                start=x
                end=y
    return arr[start:end+1]
print(max_subarray_sum(arr))


#kadane's algorithm
arr=[-2,-3,4,-1,-2,1,5,-3]
def maxSubarraySum(arr):
    maxx=float('-inf')
    current_sum=0
    for x in range(len(arr)):
        current_sum = current_sum + arr[x]
        if current_sum > maxx:
            maxx = current_sum
        if current_sum < 0:
            current_sum = 0
    return maxx
print(maxSubarraySum(arr))

print(maxSubarraySum(arr))
#return array
arr=[-2,-3,4,-1,-2,1,5,-3]
def maxSubarraySum(arr):
    maxx=float('-inf')
    current_sum=0
    start=end=s=0
    for x in range(len(arr)):
        current_sum = current_sum + arr[x]
        if current_sum > maxx:
            start=s
            end=x
        if current_sum < 0:
            current_sum = 0
            s=x+1
    return arr[start:end]
print(maxSubarraySum(arr))
