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
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

def max_subarray(arr):
    max_ending_here = arr[0]
    max_so_far = arr[0]
    start = end = s = 0   # s is a temp start index

    for i in range(1, len(arr)):
        num = arr[i]

        # extend the current subarray or start new one
        if max_ending_here + num > num:
            max_ending_here = max_ending_here + num
        else:
            max_ending_here = num
            s = i   # new subarray starts here

        # update global max
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, arr[start:end+1]

print(max_subarray(arr))