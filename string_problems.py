#Reverse a string.
name='rohit'
def reverser(s):
    ms=''
    for x in range(len(s)):
        ms = s[x] + ms
    return ms
print(reverser(name))

#Check if a string is a palindrome.
name='madam'
def is_palindrome(s):
    start=0
    end=len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
print(is_palindrome(name))

#Count vowels in a string.
strr='i love you'
def cnt_vowels(s):
    cnt=0
    for char in s.lower():
        if char in ('a','e','i','o','u'):
            cnt += 1
    return cnt
print(cnt_vowels(strr))

#Reverse words in a string.
strr='rohit arun gade'
def reverse(s):
    l=s.split(' ')
    start=0
    end=len(l)-1
    while start < end:
        l[start],l[end]=l[end],l[start]
        start += 1
        end -= 1
    return ' '.join(l)
print(reverse(strr))

#Find the first non-repeating character

s='rrohitrro'
def first_non_repeting(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for x,y in freq.items():
        if y == 1:
            return x
    return -1
print(first_non_repeting(s))