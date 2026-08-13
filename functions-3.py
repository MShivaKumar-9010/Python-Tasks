Section 1: Functions Without Parameters
# 1. Write a function welcome() that prints "Welcome to Python Programming".

def welcome():
    print("welcome to python programming")
welcome()

# 2. Write a function display_details() that prints your name, age, and city.

def display_details():
    print("name:vasudha")
    print("age:22")
    print("city:hyd")
display_details()

# 3. Write a function show_even_numbers() that prints all even numbers from 1 to 20.

def even_num():
    for i in range(1,21):
        if i%2==0:
            print(i)
even_num()

# 4. Write a function multiplication_table() that prints the multiplication table of 5.

def mul_table():
    for i in range(5,5+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
mul_table()


Section 2: Functions With Parameters
# 5. Write a function greet(name) that accepts a name and prints a greeting message.

Example:
Input: Ravi
Output: Hello Ravi
def greet(name):
    print("Hello", name)
greet("jack!!")

# 6. Write a function add(a, b) that accepts two numbers and prints their sum.

def add(a,b):
    print(a+b)
add(2,3)

# 7. Write a function find_square(n) that accepts a number and prints its square.

def square(n):
    print(n**2)
square(6)

# 8. Write a function find_greatest(a, b, c) that accepts three numbers and prints the greatest number.

def greatest(a,b,c):
    if a>b and a>c:
        print("a is greatest")
    elif b>a and b>c:
        print("b is greatest")
    else:
        print("c is greatest")
greatest(8,6,2)


Section 3: Functions Using return
# 9. Write a function add(a, b) that accepts two numbers and returns their sum. Display the returned value outside the function.

def add(a,b):
    return a+b
print(add(2,3))

# 10. Write a function is_even(n) that returns True if the number is even and False otherwise.

def is_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd" 
print(is_even(8))
    
# 11. Write a function find_factorial(n) that calculates and returns the factorial of a number.

def fact(n):
    mul=1
    for i in range(1,9):
        mul=mul*i
    return mul
print(fact(8))

# 12. Write a function calculate_area(length, breadth) that returns the area of a rectangle.

def area(length,bredth):
    return length*bredth
print(area(2,3))


Section 4: Positional Arguments
# 13. Create a function student_details(name, age, course) and call it using positional arguments.

def std_details(name,age,course):
    print("name:",name,"age:",age,"course:",course)
std_details("sandeep",24,"cse")
    
# 14. Create a function calculate_bill(item, price, quantity) that returns the total bill amount.Call the function by passing all arguments positionally.

def cal_bill(item,price,quantity):
    total_bill=price*quantity
    print("item:",item,total_bill)
cal_bill("mobile",10000,2)

# 15. Create a function employee_details(name, department, salary).
Call the function using positional arguments and display the employee details.

def emp_details(name,dept,sal):
    print("name:",name,"dept:",dept,"sal:",sal)
emp_details("bablu","testing",25000)


Section 5: Default Arguments
# 16. Create a function greet(name, message="Good Morning").
Call the function:
By passing only the name.
By passing both name and message.
Observe the difference in output.

def greet(name,message="Good Morning"):
    print("name:",name,message)
greet("anji")
def greet(name,message="Good Morning"):
    print("name:",name,message)
greet("anji","Good Evening")

# 17. Create a function calculate_simple_interest(principal, rate=5, time=2) that returns simple interest.
Call the function using:
Only principal
Principal and rate
Principal, rate, and time

def cal_simple_interest(principal,rate,time):
    interset=principal*rate*time/100
    return"interest:",interset
print(cal_simple_interest(10000,2,3))

def cal_simple_interest(principal,rate,time=5):
    interest=principal*rate*time/100
    return"interest:",interest
print(cal_simple_interest(10000,2))

def cal_simple_interest(principal=10000,rate=6,time=5):
    interest=principal*rate*time/100
    return"interest:",interest
print(cal_simple_interest(10000))

Section 6: Keyword Arguments
# 18. Create a function student_details(name, age, course).
Call the function using keyword arguments in a different order.

def std_details(name,age,course):
    print(name,age,course)
std_details(name="mani",age=22,course="cse")

# 19. Create a function product_details(product, price, quantity) that returns the total price.
Call the function using keyword arguments in different orders.

def product_details(product,price,quantity):
    total_price=price*quantity
    print("product:",product,total_price)
product_details(product="earbuds",price=950,quantity=2)


Section 7: Mixed Challenge — All Concepts
# 20. Create a function calculate_salary(name, basic_salary, bonus=5000).
The function should:
Accept name and basic_salary.
Have a default value of 5000 for bonus.
Calculate the total salary.
Return the total salary.
Call the function once using positional arguments.
Call it again using keyword arguments.
Call it a third time by using the default value for bonus.

def cal_sal(name,basic_sal,bonus=5000):
    total_sal=basic_sal+bonus
    return total_sal
print(cal_sal("sandeep",50000,2000))
print(cal_sal(name="sandeep",basic_sal=50000,bonus=2000))
print(cal_sal("sandeep",50000))
    


