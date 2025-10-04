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


#to be learned
arr = [4,3,6,2,1,1]

def mis_rep(arr):
    n = len(arr)
    S = sum(arr)
    P = sum(x*x for x in arr)
    S_n = n*(n+1)//2
    P_n = n*(n+1)*(2*n+1)//6

    diff = S - S_n           # rep - miss
    diff_sq = P - P_n        # rep^2 - miss^2

    sum_rep_miss = diff_sq // diff   # rep + miss

    rep = (diff + sum_rep_miss)//2
    miss = sum_rep_miss - rep

    return [miss, rep]

print(mis_rep(arr))  # [5, 1]
