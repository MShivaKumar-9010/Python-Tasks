Interview-Style Programming Questions: Loops, Strings, and Number Operations
________________________________________
1. Print Numbers from 1 to n
Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5
n=5
for i in range(1,n+1):
    print(i)


2. Print Numbers from m to n
Question: Write a program to print numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7
m=3
n=7
for i in range(m,n+1):
    print(i)


3. Print Numbers from n to 1 in Reverse
Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1
n=5
for i in range(5,0,-1):
    print(i)


4. Print Numbers from n to m in Reverse
Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6
m=6
n=10
for i in range(n,m-1,-1):
    print(i)


5. Sum of n Natural Numbers
Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15
n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

n = 5
print(sum(range(1, n+1)))


6. Factorial of a Number
# Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120
n=5
mul=1
for i in range(1,n+1):
    mul=mul*i
print(mul)


7. Sum of m to n Numbers
Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18
m=3
n=6
sum=0
for i in range(m,n+1):
    sum=sum+i
print(sum)


8. Product of m to n Numbers
Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24
m=2
n=4
mul=1
for i in range(m,n+1):
    mul=mul*i
print(mul)


9. Print Factors of a Number
Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6
n=6
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


10. Count of Factors
Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4
n=6
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)


11. Prime Number Check
Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime
n = 7
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")


12. Even Numbers from m to n
Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10
m=3
n=10
for i in range(m,n+1,1):
    if i%2==0:
        print(i)


13. Odd Numbers from m to n
Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9
m=3
n=10
for i in range(m,n+1,1):
    if i%2!=0:
        print(i)


14. Count of Even and Odd Numbers
Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3
m=3
n=7
even=0
odd=0
for i in range(m,n+1,1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print('even',even)
print('odd',odd)

       
15. Reverse a String
Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
a="hello"
print(a[::-1])

a = "hello"
rev = ""
for i in a:
    rev = i + rev
print(rev)


16. Check for Palindrome String
Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome
s="madam"
if s== s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


17. Sum of Digits
Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
n=123
sum=0
while n!=0:
    sum += n%10  # 3+2+1
    n=n//10 #12+1+0
print(sum)

18. Product of Digits
Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
n=123
mul=1
while n!=0:
    mul*=n%10
    n=n//10
print(mul)


19. Armstrong Number Check
Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number
n=153
t1=n
c=0
while n!=0:
    c+=1
    n=n//10
sum=0
while t1!=0:
    rem=t1%10
    sum=sum+rem**c
    t1=t1//10
print(sum)
    

20. Reverse a Number
Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
num = 121
rev = 0

while num  != 0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
print(rev)

21. Palindrome Number Check
Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
num = 121
t1=num
rev = 0

while num  != 0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
if rev == t1:
    print("palindrome")
else:
    print("not palindrome")


22. Count Vowels in String
Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
x="apple"
vowels="aeiou"
c=0
for i in x:
    if i in vowels:
        c+=1
print(c)


23. Count Consonants in String
Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3
x="apple"
vowels="aeiou"
c=0
for i in x:
    if i not in vowels:
        c+=1
print(c)


24. Count Vowels and Consonants
Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3
x="apple"
vowels="aeiou"
v=0
c=0
for i in x:
    if i in vowels:
        v+=1
    else:
        c+=1
print("vowels",v)
print("consonants",c)


25. Perfect Number Check
Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
n=28
for i in range(1,n+1):
 if i * i == n:
    print("perfect square")
    break
else:
    print("not a perfect square")

n = 28

if int(n ** 0.5) ** 2 == n:
    print("Perfect square")
else:
    print("Not a perfect square")        


26. Neon Number Check
Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number
n=9
square=n*n
sum=0
while square>0:
    digit=square%10
    sum=sum+digit
    square=square//10

if sum == n:
    print("neon number")
else:
    print(" not a neon number")


27. Strong Number Check
Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number
n = 145
t1 = n
sum = 0
while n!=0:
    rem = n%10
    fact = 1
    for i in range(1, rem + 1):
        fact = fact*i

    sum += fact
    n = n//10
if sum == t1:
    print("strong number")
else:
    print("not strong number")


28. Harshad Number Check
Question: Check if a number is divisible by the sum of its digits. Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number
n = 18
t1 = n
sum = 0

while n != 0:
    rem = n % 10
    sum += rem
    n = n // 10

if t1 % sum == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")


29. Fibonacci Series
Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3
n = 5
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


30. Check for Neon Number (Repeated)
Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 - Output: Neon number
n=9
square=n*n
sum=0
while square>0:
    digit=square%10
    sum=sum+digit
    square=square//10

if sum == n:
    print("neon number")
else:
    print(" not a neon number")