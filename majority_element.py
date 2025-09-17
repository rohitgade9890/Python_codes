#find number that appers more then n/2 elements from array
#bruteforce
arr=[1,2,3,2,3,2,2]
def majority_ele(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for x,y in freq.items():
        if y > len(arr)/2:
            return x
    return -1
print(majority_ele(arr))
    
#moore's voting algorithm
arr = [1, 2, 3, 2, 3, 2, 2]

def majority_ele(arr):
    # Step 1: Find candidate
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1

print(majority_ele(arr))