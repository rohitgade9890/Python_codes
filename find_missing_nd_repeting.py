#write code to find missing and repeting element from array
arr=[4,3,6,2,1,1]
def mis_rep(arr):
    miss=None
    rep=None
    arr.sort()
    freq={}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for x,y in freq.items():
        if y == 2:
            rep=x
    for x in range(1,len(arr)):
        if arr[x] - arr[x-1] > 1:
            miss = arr[x] - 1
    return [miss,rep]
print(mis_rep(arr))