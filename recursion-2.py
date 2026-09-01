#1 Write a function factorial(n) that returns the factorial of a non‑negative integer n using recursion.
n=6
def fact(n,f=1):
    if n==0:
        return f
    f=f*n
    return fact(n-1,f)
print(fact(n))

#2 Implement a function fib(n) that returns the n‑th Fibonacci number (with fib(0) = 0, fib(1) = 1) recursively.
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=4
print(fib(n))

#3 Create a function sum_digits(num) that computes the sum of all decimal digits of a non‑negative integer num via recursion.
n=5
def sum(n,s=0):
    if n==0:
        return s
    s=s+n
    return sum(n-1,s)
print(sum(n))

#4 Develop a recursive function reverse_string(s) that returns the characters of string s in reverse order.
def rev_str(s):
    if len(s)<=1:
        return s
    return s[-1]+rev_str(s[:-1])
print(rev_str("Hasini"))

#5 (Optional) Design a helper function is_palindrome(s) that determines whether a string s is a palindrome by recursively comparing characters from the ends toward the center.
def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
s="amma"
if is_palindrome(s):
    print("palindrome")
else:
    print("not a palindrome")
is_palindrome(s)

