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