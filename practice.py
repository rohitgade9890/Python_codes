#remove duplicates in place sorted array
arr=[1,3,4,4,5,7,7,8,2]
def dedup(arr):
    pos=0
    for x in range(1,len(arr)):
        if arr[x] != arr[pos]:
            arr[pos+1] = arr[x]
            pos+=1
    return arr[:pos+1]
print(dedup(arr))

#remove deplicates from array
def dedup(arr):
    seen=set()
    res=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            res.append(num)
    return res
print(dedup(arr))