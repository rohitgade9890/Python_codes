#Find the intersection of two arrays.
arr1=[1,3,4,4,6,9]
arr2=[3,6,7,4,4]
def intercest(arr1,arr2):
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    res=[]
    i=0
    j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1
    return res
print(intercest(arr1,arr2))