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

#Check if two strings are anagrams.
s1='rohit'
s2='irtoh'
def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
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



#find substring in string
s='rohit arin gade'
s1='hit'
def find_string(s,s1):
    maxx=len(s1)
    for x in range(len(s)):
        if s[x:x+maxx] == s1:
            return True
    return False
print(find_string(s,s1))

#Find the longest common prefix among strings.
strings=['rohhu','roohit arun','ro']
def longest_common_prefix(arr):
    min_len = len(min(arr, key=len))
    prefix = ""
    
    for i in range(min_len):
        current_char = arr[0][i]   
        for word in arr[1:]:
            if word[i] != current_char:  
                return prefix
        prefix += current_char
    return prefix
print(longest_common_prefix(strings))

#Encode and decode a string using run-length encoding
s='rrrohiitss'
s = 'rrrohiitss'

def encoding(s):
    cnt = 1
    res = ''
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            res += s[i-1] + str(cnt)
            cnt = 1
    res += s[-1] + str(cnt)
    return res
print(encoding(s))

#Replace all spaces in a string with `%20`.
s='im rohit & trying string problems'
def replacer(s):
    res=''
    for char in s:
        if char == ' ':
            res = res + '%20'
        else:
            res = res + char
    return res
print(replacer(s))