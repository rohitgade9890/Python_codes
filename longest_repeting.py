#Find the longest consecutive sequence in an unsorted array.

arr=[1,2,3,3,3,2,1,5,9,0,0,0,0,0]
def longest_subsequence(arr):
    max_cnt=1
    cnt=1
    for x in range(1,len(arr)):
        if arr[x] == arr[x-1]:
            cnt += 1
            max_cnt=max(max_cnt,cnt)
        else:
            cnt=1
    return max_cnt
print(longest_subsequence(arr))
