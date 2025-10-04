#prefix sum

arr=[11,2,3,55,2,6]

def prefix_sum(arr):
    for x in range(len(arr)):
        arr[x] = arr[x-1] + arr[x]
    return arr
print(prefix_sum(arr)) 

#prefix sum
#give me sum from index 2 to 5
arr=[11,2,3,55,2,6]

def prefix_sum(arr):
    start=2
    end=5
    for x in range(1,len(arr)):
        arr[x] = arr[x-1] + arr[x]
    print(arr)
    ans=arr[end]-arr[start-1]
    return ans
print(prefix_sum(arr)) 


arr = [1, 2, 3, -1, 1]
k = 3

def count_subarrays_sum_k(arr, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}  
    
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]
        if prefix_sum in freq:
            freq[prefix_sum] += 1
        else:
            freq[prefix_sum] = 1   
    return count

print(count_subarrays_sum_k(arr, k)) 