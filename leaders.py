#leaders of array
#bruteforce
arr=[10,22,12,3,0,6]
#op=[22,12,6]
def leaders(arr):
    res=[]
    for x in range(len(arr)):
        is_leader=True
        for y in range(x+1,len(arr)):
            if arr[x] < arr[y]:
                is_leader=False
                break
        if is_leader:
            res.append(arr[x])
    return res
print(leaders(arr))

#optimized
#leaders of array
arr=[10,22,12,3,0,6]
#op=[22,12,6]
def leaders(arr):
    res=[]
    maxx=0
    for x in range(len(arr)-1,-1,-1):
        if arr[x] > maxx:
            res.append(arr[x])
            maxx=arr[x]
    return res
print(leaders(arr))