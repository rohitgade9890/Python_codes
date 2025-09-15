#find largest
arr=[12,5,33,5,35,2]
def find_largest(arr):
    largest=float('-inf')
    for num in arr:
        if num > largest:
            largest = num
    return largest
print(find_largest(arr))

#find second largest
def second_largest(arr):
    largest=float('-inf')
    second_largest=float('-inf')
    for num in arr:
        if num > largest:
            second_largest=largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest=num
    return second_largest
print(second_largest(arr))

#check if sorted
def is_sorted(arr):
    for x in range(len(arr)-1):
        if arr[x] > arr[x+1]:
            return False
    return True
print(is_sorted(arr))

#remove duplicate
def distinct(arr):
    res=[]
    seen=set()
    for num in arr:
        if num not in seen:
            seen.add(num)
            res.append(num)
    return res
print(distinct(arr))