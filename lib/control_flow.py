#!/usr/bin/env python3

def admin_login(username, password):
    if username == 'ADMIN' and password == "12345": 
        message = "Access granted"
    elif username == 'admin' and password == '12345':
        message = "Access granted"
    else:
        message = "Access denied"
    return message




def hows_the_weather(temperature):
    if temperature < 40:
        message = "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65 :
        message = "It's a little chilly out there!"
    elif temperature > 85 : 
        message = "It's too dang hot out there!"
    else :
        message =   "It's perfect out there!"
    return message



def fizzbuzz(num):
    if num % 3 == 0 and num % 5 ==0:
        message = "FizzBuzz"
    elif num % 3 == 0:
        message = "Fizz"
    elif num %5 == 0:
        message = "Buzz"
    else :
        message = num
    return message



def calculator(operation, num1, num2):
    if operation == '+' :
        message = num1 +num2
    elif operation == "-":
        message = num1 - num2
    elif operation == "*":
        message = num1*num2
    elif operation == "/" :
        message = num1/num2
    else:
        print("Invalid operation!")
        return None
    return message
