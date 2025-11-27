#!/usr/bin/env python3

def admin_login(username, password):
    # Case-insensitive username "admin"
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if num % 15 == 0:    # multiple of 3 and 5
        return "FizzBuzz"
    elif num % 3 == 0:   # multiple of 3 only
        return "Fizz"
    elif num % 5 == 0:   # multiple of 5 only
        return "Buzz"
    else:
        return num       # return the number itself


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

