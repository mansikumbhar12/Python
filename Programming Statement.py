Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ASSIGNMENT NO 2
>>> #1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
>>> num = int(input("Enter a number: "))
Enter a number: 235
>>> result = "Even" if num % 2 == 0 else "Odd"
>>> print("The number is {result}.")
The number is {result}.
>>> print(f"The number is {result}.")
The number is Odd.
>>> 
>>> #2. Using input function take two number and then swap the number
>>> num1 = float(input("Enter the first number:"))
Enter the first number:34
>>> num2 = float(input("Enter the second number:"))
Enter the second number:12
>>> num1, num2 = num2, num1
>>> print(f"After swapping: First number = {num1}, Second number = {num2}")
After swapping: First number = 12.0, Second number = 34.0
>>> 
>>> #3. Write a Program to Convert Kilometers to Miles
>>> kilometers = float(input("Enter distance in kilometers:"))
Enter distance in kilometers:400
>>> miles = kilometers * 0.621371
>>> print(f"Distance in miles: {miles}")
Distance in miles: 248.54840000000002
>>> 
>>> #4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
>>> principle = 200
>>> time = 5
>>> rate = 5
>>> simple_interest = (principle * time * rate) / 100)
SyntaxError: unmatched ')'
>>> simple_interest = (principle * time * rate) / 100
>>> print(f"Simple interest: Rs. {simple_interest}")
Simple interest: Rs. 50.0
