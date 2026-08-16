Pattern-Based Programming Questions (All 34 Questions - Interview Style)
________________________________________
🔷 Square, Rectangle, and Triangle Patterns (1–15)

1.	Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("* ",end="")
    print()
    
    
2.	Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
m=3
n=5
for i in range(m): 
    stars=''
    for j in range(n): 
        stars += '* '
    print(stars)


3.	Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
n=5
for i in range(1,n+1):
    for j in range(i):
        print("* ",end="")
    print()
n=4
for i in range(1,n+1):
    print("" * (n-i)+" *"*i)


4.	Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
n=4
for i in range(1,n+1):
    print("  " * (n-i)+" *"*i)
        

5.	Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(n,0,-1):
    print(""*(n-1)+" *"*i)


6.	Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
n=5
for i in range(5,0,-1):
    print(" "*(n-1)+"* "*i)
  

7.	Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
n=4
for i in range(1,n+1):
    print(" " * (n-i) + "*"*(2*i-1))


8.	Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
n=3
for i in range(1,n+1):
    print(" " * (n-i) + "*"*(2*i-1))
for j in range(n-1,0,-1):
    print(" " * (n-j)+ "*"*(2*j-1))


9.	Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *
for row in range(1,6):
    for col in range(1,6):
        if col==1 or col==5 or row==3 or (row in(2,4) and col in (2,4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


10.	Left-Aligned Half Diamond
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
n=4
for i in range(1,n+1):
    print("" * (n-i) + "* "*i)
for i in range(3,0,-1):
    print("" * (n-i) + "* "*i)


11.	Right-Aligned Half Diamond
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *
n=4
for i in range(1,n+1):
    print("  " * (n-i) + "* "*i)
for i in range(3,0,-1):
    print("  " * (n-i) + "* "*i)


12.	Sandglass Pattern
# Input: n = 4
# Output:
# * * * *
#   * * *
#     * *
#       *
#     * *
#   * * *
# * * * *
n=4
for i in range(n,0,-1):
    print("  " * (n-i) + " *"*i)
for i in range(2,n+1):
    print("  " * (n-i) + " *"*i)
 

13.	Increasing Width Triangle
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
n=5
for i in range(1,n+1):
    print("" * (n-i) + "* "*i)

    
14.	Decreasing Width Triangle
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(n,0,-1):
    print("" * (n-i) + "* "*i)


15.	Right-Aligned Hill Pattern
# Input: n = 4
# Output:
#       *
#     * *
#   * * *
# * * * *
n=4
for i in range(1,n+1):
    print("  " * (n-i) + "* "*i)


___________________________________
🔲 Hollow Patterns (16–25)
16.	Hollow Square Pattern
# Problem: Print a hollow square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *
n=4
for row in range(1,n+1):
    for col in range(1,n+1):
        if row in(1,n) or col in(1,n):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
        

17.	Hollow Rectangle Pattern
# Problem: Print a hollow rectangle of m rows and n columns.
# Input: n=4
# Output:
# * * * * *
# *       *
# *       *
# * * * * *
n=4
for row in range(1,n+1):
    for col in range(1,n*2+1):
        if row in(1,n) or col==1 or col==n*2:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


18.	Hollow Right-Angled Triangle (Left-Aligned)
# Input: n = 5
# Output:
# *
# * *
# *   *
# *     *
# * * * * *
n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


19.	Hollow Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     *   *
#   *     *
# * * * * *
n=5
for i in range(1,n+1):
    print("  " * (n-i),end="")
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


20.	Hollow Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# *     *
# *   *
# * *
# *
n=5
for i in range(n,0,-1):
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
        

21.	Hollow Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *
n=5
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(i):
        if j==0 or j==i-1 or i==n:
            print(" *",end="")
        else:
            print("  ",end="")
    print()


22.	Hollow Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     *   *
#   *       *
# * * * * * * *
n=4
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


23.	Hollow Diamond Pattern
# Input: n = 3
# Output:
#     *
#   *   *
# *       *
#   *   *
#     *
n=3
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 :
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for i in range(n-1,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    

24.	Hollow Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# *   *   *
# *       *
# *   *   *
# * *   * *
# *       *
n=4
for row in range(1,2*n+1):
    for col in range(1,2*n+1):
        if col==1 or col==2*n  or row == col or row + col == 2*n+1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


25.	Hollow Hourglass Pattern
# Input: n = 5
# Output:
# * * * * *
# *       *
#   *   *
#     *
#   *   *
# *       *
# * * * * *
n=5
for rows in range(n,0,-1):
    for cols in range(1,n+1):
        if rows in(1,5) or rows == cols or cols ==n+1-rows:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
_____________________________________
🔢 Number-Based Patterns (26–34)
26.	Increasing Number Triangle
# Problem: Print numbers from 1 to n in triangle form.
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


27.	Repeating Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print() 


28.	Continuous Number Triangle
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()


29.	Reverse Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


30.	Inverted Number Triangle
# Input: n = 5
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


31.	Right-Aligned Number Triangle
# Input: n = 5
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    
32.	Pyramid Number Pattern
# Input: n = 4
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()


33.	Even Number Triangle
# Input: n = 5
# Output:
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*2,end=" ")
    print()
       
    
34.	Odd Number Triangle
# Input: n = 5
# Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j*2-1,end=" ")
    print()
