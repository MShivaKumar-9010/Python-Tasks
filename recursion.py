# Write a recursive function to print numbers from 1 to 10.

def num(n):
    if n==11:
        return
    print(n)
    return num(n+1)
n=0
num(n)

# Write a recursive function to print numbers from 10 to 1.

def num(n):
    if n==0:
        return
    print(n)
    return num(n-1)
n=10
num(n)

# Write a recursive function to print numbers from 1 to n.
# Example: n = 5 → 1 2 3 4 5

def num(n):
    if n==6:
        return
    print(n)
    return num(n+1)
n=1
num(n)

# Write a recursive function to print numbers from n to 1.
# Example: n = 5 → 5 4 3 2 1

def num(n):
    if n==0:
        return
    print(n)
    return num(n-1)
n=5
num(n)

# Write a recursive function to find the sum of numbers from 1 to n.
# Example: n = 5 → 15

n=1
def sum(n):
    if n==16:
        return
    print(n)
    return sum(n+1)
sum(n)

# Write a recursive function to find the factorial of a number.
# Example: 5! → 120

n=5
def fact(n,f=1):
    if n==0:
        return f
    f=f*n
    return fact(n-1,f)
print(fact(n)) 

# Write a recursive function to find the sum of all digits of a number.
# Example: 1234 → 10

n=1
def sum(n):
    if n==11:
        return 
    print(n)
    return sum(n+1)
sum(n)

# Write a recursive function to print each character of a string.
# Example: "Python" → P y t h o n

def chars(s):
    if s == "": 
        return
    print(s[0])  
    chars(s[1:]) 
chars("Python")

# Write a recursive function to reverse a string.
# Example: "hello" → "olleh"

def rev_str(s):
    if len(s)<=1:
        return s
    return s[-1]+ rev_str(s[:-1])#last character + remove last character
s="hello"
print(rev_str(s))

# Write a recursive function to check whetwher a string is a palindrome.
# Example: "madam" → Palindrome

def palindrome(s):
    if len(s)<=1:
        return s
    return s[-1]+palindrome(s[:-1])
s="madam"
if s==palindrome(s):
    print("palindrome")
else:
    print("not a palindrome")
palindrome(s)

