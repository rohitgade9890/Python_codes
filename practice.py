#Anagram Checker
s1='rohit'
s2='mohit'

def is_anagram(s1,s2):
    freq={}
    for char in s1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in s2:
        if char not in freq or freq[char] < 1:
            return False
        freq[char] -= 1
    return True
print(is_anagram(s1,s2))

s="Longest Word in a Sentence"

def longest_word(s):
    longest=''
    ls = s.split(' ')
    for words in ls:
        if len(words) > len(longest):
            longest = words
    return longest
print(longest_word(s))


#Sum of Digits
num=9375
def find_sum(num):
    temp=num
    summ=0
    while temp > 0:
        digit = temp % 10
        summ = summ + digit
        temp = temp // 10
    return summ
print(find_sum(num))

#Check Perfect Number
#sum of divisors equals the number
n=28
def is_perfect(num):
    summ = 0
    for x in range(1, num // 2 + 1):  # include num//2
        if num % x == 0:
            summ += x
    return summ == num
print(is_perfect(n))

#Reverse Words in a String
s='im rohit arun gade'
def reverser(s):
    ls=s.split(' ')
    start=0
    end=len(ls)-1
    while start < end:
        srev=''
        for char in ls[start]:
            srev=char+srev
        erev=''
        for char in ls[end]:
            erev=char+erev
        ls[start]=srev
        ls[end]=erev
        ls[start],ls[end]=ls[end],ls[start]
        start += 1
        end -= 1
    return ' '.join(ls)
print(reverser(s))

#Count Substrings
string='rohit arun garude'
substring='ru'
def cnt_substring(s,s1):
    max_len=len(s1)
    cnt=0
    for x in range(len(s)):
        if s[x:x+max_len]==s1:
            cnt += 1
    return cnt
print(cnt_substring(string,substring))


#Find Missing Number in Array
arr=[1,2,3,5,6]
def find_missing(arr):
    given_sum=sum(arr)
    n=len(arr)+1
    actual_sum=n*(n+1)/2
    print(actual_sum-given_sum)
find_missing(arr)


#Flatten Nested List
l=[1,2,3,[2,3,2],3,[3,4,[3,4]]]
def flatten(l):
    res=[]
    stack=l[:]
    while stack:
        item=stack.pop(0)
        if isinstance(item,list):
            stack = item + stack
        else:
            res.append(item)
    return res
print(flatten(l))



#best time to buy and sell stocks
stocks=[2,7,4,1,5,8]

def buy_sell(arr):
    min_price=arr[0]
    max_profit=float('-inf')
    for x in range(1,len(arr)):
        profit=arr[x]-min_price
        if profit > max_profit:
            max_profit = profit
        min_price=min(min_price,arr[x])
    return max_profit
print(buy_sell(stocks))


#rearrange the array by signs
arr=[2,2,-3,1,-9,2,-7,-9]
def rearrange(arr):
    pos=[]
    neg=[]
    pos_index=0
    neg_index=0
    for num in arr:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    for x in range(len(arr)):
        if x % 2 == 0:
            arr[x] = pos[pos_index]
            pos_index += 1
        else:
            arr[x] = neg[neg_index]
            neg_index += 1
    return arr
print(rearrange(arr))


#find leaders of array
arr=[2,7,4,1,5,8]
#leader = no element from right should be greter than that number
def leaders(arr):
    res=[]
    maxx=float('-inf')
    for x in range(len(arr)-1,-1,-1):
        if arr[x] > maxx:
            res.append(arr[x])
        maxx = arr[x]
    return res
print(leaders(arr))

#longest consecutive sequence
arr=[1,6,3,2,101,9,102,99,100,100]
def longest_sequece(arr):
    arr.sort()
    cnt=1
    max_cnt=1
    last_ele=arr[0]
    for x in range(1,len(arr)):
        if arr[x] - last_ele == 1:
            cnt += 1
        else:
            cnt = 1
        max_cnt=max(max_cnt,cnt)
        last_ele=arr[x]
    return max_cnt

print(longest_sequece(arr))

arr=[1,6,3,2,101,9,100,102,99,100,102,100]
def longest_sequence(arr):
    arr.sort()
    cnt = 1
    max_cnt = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == last:
            continue
        if arr[i] == last + 1:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
        last = arr[i]
    return max_cnt

print(longest_sequence(arr))