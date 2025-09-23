#rearrange the array by sign
arr=[1,-2,3,3,-4,-9]
def rearrange(arr):
    pos=[]
    neg=[]
    posindex=0
    negindex=0
    for num in arr:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    for x in range(len(arr)):
        if x % 2 == 0:
            arr[x] = pos[posindex]
            posindex += 1
        else:
            arr[x] = neg[negindex]
            negindex += 1
    return arr
print(rearrange(arr))


