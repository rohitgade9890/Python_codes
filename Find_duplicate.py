#2. Find the duplicate number in an array of 1…n integers.
arr=[1,2,3,3,4,5]
def find_duplicate(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for x,y in freq.items():
        if y > 1:
            return x
    return -1
print(find_duplicate(arr))