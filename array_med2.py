#find element that appears once
arr=[12,34,23,34,12,7]
def once_list(arr):
    freq={}
    res=[]
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for x,y in freq.items():
        if y == 1:
            res.append(x)
    return res
print(once_list(arr))

#find missing element
arr=[1,2,4,5]
def find_missing(arr):
    summ=sum(arr)
    actual_summ=0
    for x in range(len(arr)+2):
        actual_summ += x
    return actual_summ - summ
print(find_missing(arr))

#methon 2 for non sorted more than one missing numbers
arr=[2,4,9,7,13]
def find_missings(arr):
    missings=[]
    arr=sorted(arr)
    for x in range(len(arr)-1):
        if arr[x+1] - arr[x] > 1:
            for y in range(arr[x]+1,(arr[x+1])):
                missings.append(y)
    return missings
print(find_missings(arr))

#max consecutive numbers
arr=[3,3,1,2,3,3,3,4,2,3,2,2,2,2,]

def max_cons_num(arr):
    pos=1
    max_no=1
    for x in range(1,len(arr)):
        if arr[x] == arr[x-1]:
            pos += 1
            max_no=max(pos,max_no)
        else:
            pos = 1
    return max_no
print(max_cons_num(arr))