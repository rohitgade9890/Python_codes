#majority element
arr=[1,3,2,-5,8,2]
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
print(max_subarray_sum(arr))
