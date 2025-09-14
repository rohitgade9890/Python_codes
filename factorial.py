print('writing code to find factorial or number')
n=int(input("Enter a number: "))
def factorial(n):
    fact=1
    for x in range(2,n+1):
        fact = fact * x
    return fact
print(factorial(n))