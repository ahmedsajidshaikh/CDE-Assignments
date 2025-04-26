# # Python Basic (Variable)

# # 1 Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
# print("My Name is \nAhmed Sajid \nand my date of birth is \n 07/08/1999")

# # 2 Write your small bio using variables and print it using print function
# name = "Ahmed Sajid"
# age = 24
# bio= "Mathematics Teacher with over 06 years of hands - on, successful teaching experience, I am confident in my ability and passion to become a positive addition to your school community. It is with great pleasure and enthusiasm that I submit my resume and write this letter in response to your job advertisement seeking an experienced Mathematics Teacher for Middle and Secondary O/Levels. "
# print("My name is " + name + " and I am " + str(age) + "years old" + bio )

# # 3 Write a program in which use all the operators we can use in Python. 
# # Arithmetic Operators
# a = 10
# b = 5

# print("Arithmetic Operators:")
# print("Addition:", a + b)          # Addition
# print("Subtraction:", a - b)       # Subtraction
# print("Multiplication:", a * b)    # Multiplication
# print("Division:", a / b)          # Division
# print("Modulus:", a % b)           # Modulus
# print("Exponentiation:", a ** b)   # Exponentiation
# print("Floor Division:", a // b)   # Floor Division

# # Comparison Operators
# print("\nComparison Operators:")
# print("Equal:", a == b)             # Equal
# print("Not Equal:", a != b)         # Not Equal
# print("Greater than:", a > b)       # Greater than
# print("Less than:", a < b)          # Less than
# print("Greater than or equal to:", a >= b)  # Greater than or equal to
# print("Less than or equal to:", a <= b)     # Less than or equal to

# # Logical Operators
# print("\nLogical Operators:")
# print("Logical AND:", a > 5 and b < 10)  # Logical AND
# print("Logical OR:", a > 5 or b > 10)    # Logical OR
# print("Logical NOT:", not(a > 5))         # Logical NOT

# # Assignment Operators
# print("\nAssignment Operators:")
# c = 5
# print("Initial value of c:", c)
# c += 2
# print("After c += 2:", c)                 # Add and assign
# c -= 2
# print("After c -= 2:", c)                 # Subtract and assign
# c *= 2
# print("After c *= 2:", c)                 # Multiply and assign
# c /= 2
# print("After c /= 2:", c)                 # Divide and assign

# # 4 Write a program Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables Mention Variable of Total Marks and assign 300 to it then Calculate Percentage. 
# english = 85
# islamiat = 90
# maths = 80
# total_marks = 300
# percentage = ((english + islamiat + maths) / total_marks) * 100
# print("Percentage:", percentage)



# # Part -2 Python Basics (Conditional Statements)

# # 1 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter your salary: $"))
# year_of_service = int(input("Enter your year of service: "))
# if year_of_service > 5:
#     bonus = salary * 0.05
#     print("Net bonus amount: $", bonus)
# else:
#     print("No bonus is applicable.")
    
# # 2 Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible.
# age = int(input("Enter your age: "))
# if age > 17:
#     print("Eligible for voting.")
# else:
#     print("Not eligible for voting.")
    
# # 3 Write a program to check whether a number entered by user is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number.")
# else:
#     print("Odd number.")
    
# # 4 Write a program to check whether a number is divisible by 7 or not. Show Answer.
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print("Number is divisible by 7.")
# else:
#     print("Number is not divisible by 7.")
    
# # 5 Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")
    
# # 6 Write a program to display the last digit of a number.
# num = int(input("Enter a number: "))
# print("Last digit of the number is:", num % 10)

# #  7 Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
# length = int(input("Enter the length of rectangle: "))
# breadth = int(input("Enter the breadth of rectangle: "))
# if length == breadth:
#     print("It is a square.")
# else:
#     print("It is a rectangle.")
    
# #  8 Take two int values from user and print greatest among them.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("Greatest number is:", num1)
# else:
#     print("Greatest number is:", num2)
    
# # 9 A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
# quantity = int(input("Enter the quantity of items: "))
# cost_per_item = 100
# total_cost = quantity * cost_per_item
# if total_cost > 1000:
#     discount = 0.1
#     total_cost_after_discount = total_cost - (total_cost * discount)
#     print("Total cost after discount is:", total_cost_after_discount)
# else:
#     print("Total cost is:", total_cost)
    
# # 10 A school has following rules for grading system:
# """a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade."""   

# marks = int(input("Enter your marks: "))
# if marks < 25:
#     print("Grade is F")
# elif marks >= 25 and marks <= 45:
#     print("Grade is E")
# elif marks >= 45 and marks <= 50:
#     print("Grade is D")
# elif marks >= 50 and marks <= 60:
#     print("Grade is C")
# elif marks >= 60 and marks <= 80:
#     print("Grade is B")
# else:
#     print("Grade is A")

# print(marks) 

# # 11 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
# units = int(input("Enter the number of units: "))
# if units <= 100:
#     print("No charge")
# elif units <= 300:
    
# # A student will not be allowed to sit in exam if his/her attendence is less than 75%.Take following input from user Number of classes held Number of classes attended. And print percentage of class attended Is student is allowed to sit in exam or not.

#  classes_held = int(input("Enter the number of classes held: "))
# classes_attended = int(input("Enter the number of classes attended: "))
# percentage = (classes_attended / classes_held) * 100

# if percentage >= 75:
#     print("Student is allowed to sit in exam.")
# else:
#     print("Student is not allowed to sit in exam.")
    
# # Write a program to check if a year is leap year or not.If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Year is a leap year.")
#         else:
#             print("Year is not a leap year.")
#     else:
#         print("Year is a leap year.")
# else:
#     print("Year is not a leap year.")
            
               
# # Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750.
# units = int(input("Enter the number of units: "))
# if units <= 100:
#     print("No charge")
# elif units <= 200:
#     print("Total bill amount is: ", units* 5)
# elif units > 200:
#     print("Total bill amount is: ", units* 10)
# else:
#     print("Invalid input")
    

# # Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Enter the age of first person: "))
age2 = int(input("Enter the age of second person: "))
age3 = int(input("Enter the age of third person: "))
if age1 >= age2 and age1 >= age3:
    print("Oldest is", age1)
    if age2 >= age3:
        print("Youngest is", age3)
    else:
        print("Youngest is", age2)
else:
    if age2 >= age1 and age2 >= age3:
        print("Oldest is", age2)
    else:
        print("Oldest is", age3)
        if age1 >= age3:
            print("Youngest is", age3)
        else:
            print("Youngest is", age1)
            
            
            
            
            
        
        
    
        
        
        
    
    

    
    
        
        
    
    
    
    
    
    
    
    
    
    
    


