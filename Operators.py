Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Assignment Questions:
>>> # 1. Calculate the multiplication and sum of two numbers
>>> a = 5
>>> b = 10
>>> multiplication = a*b
>>> print("Multiplication of two numbers is :",multiplication)
Multiplication of two numbers is : 50
>>> sum = a+b
>>> print("Sum of two numbers is :",sum)
Sum of two numbers is : 15
>>> 
>>> # 2. Declare two variables and print that which variable is largest using ternary operators
>>> x = 15
>>> y = 25
>>> largest = x if x>y else y
>>> print("The largest number between two number is:",largest)
The largest number between two number is: 25
>>> 
>>> # 3. Python program to convert the temperature in degree centigrade to Fahrenheit
>>> celsius = 25
>>> fahrenheit = (celsius * 9/5) + 32
>>> print("Celsius is equal to fahrenheit is:",fahrenheit)
Celsius is equal to fahrenheit is: 77.0
>>> 
>>> # 4. Python program to find the area of a triangle whose sides are given
>>> import math
>>> a = 5, b = 6, c = 7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a = 5
>>> b = 6
>>> c = 7
>>> s = (a+b+c)/2
>>> area = math.sqrt(s*(s-a)*(s-b)*(s-c))
>>> print("The area of the triangle is:",area)
The area of the triangle is: 14.696938456699069
>>> a = float(input("Enter the length of the first side: "))
Enter the length of the first side: 5
>>> b = float(input("Enter the length of the second side: "))
Enter the length of the second side: 6
>>> c = float(input("Enter the length of the third side: "))
Enter the length of the third side: 7
>>> s = (a + b + c) / 2
>>> area = math.sqrt(s*(s-a)*(s-b)*(s-c))
>>> print("The area of the triangle is:",area)
The area of the triangle is: 14.696938456699069
