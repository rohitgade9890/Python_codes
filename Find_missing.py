#1. Find the missing number in an array of 1…n integers.
arr=[1,2,3,5,6]
def find_missing(arr):
    summ=sum(arr)
    actual_summ=0
    for x in range(1,len(arr)+2):
        actual_summ = actual_summ + x
    return actual_summ - summ
print(find_missing(arr))