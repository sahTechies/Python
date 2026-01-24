#this project is to create calculator 
def add(x, y): #returns sum of two numbers
    return x + y

def subtract(x, y): #returns difference of two numbers
    return x - y

def multiply(x, y): #returns product of two numbers
    return x * y

def divide(x, y): #returns quotient of two numbers
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y): #returns x raised to the power of y
    return x ** y

def modulus(x, y): #returns remainder when x is divided by y
    return x % y

def floor_divide(x, y): #returns floor division of x by y
    if y == 0:
        return "Error! Division by zero."
    return x // y

def square_root(x): #returns square root of x
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return x ** 0.5

def percentage(x, y): #returns y percent of x
    return (x / 100) * y

def factorial(x): #returns factorial of x
    if x < 0:
        return "Error! Factorial of negative number not defined."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1): 
        result *= i
    return result

def average(x, y): #returns average of two numbers
    return (x + y) / 2

def cube(x): #returns cube of a number
    return x ** 3

def cube_root(x): #returns cube root of a number
    if x >= 0:
        return x ** (1/3)
    else:
        return -(-x) ** (1/3)

def logarithm(x, base=10):  #returns logarithm of x to the given base
    import math
    if x <= 0:
        return "Error! Logarithm of non-positive number not defined."
    return math.log(x, base)

def sine(x):  #returns sine of an angle in degrees 
    import math 
    return math.sin(math.radians(x))

def cosine(x):  #returns cosine of an angle in degrees
    import math
    return math.cos(math.radians(x))

def tangent(x): #returns tangent of an angle in degrees
    import math
    return math.tan(math.radians(x))

def cotangent(x): #returns cotangent of an angle in degrees
    import math
    if x % 180 == 0:
        return "Error! Cotangent undefined for this angle."
    return 1 / math.tan(math.radians(x))

def secant(x):  #
    import math
    if x % 90 == 0 and (x // 90) % 2 != 0:
        return "Error! Secant undefined for this angle."
    return 1 / math.cos(math.radians(x))

def cosecant(x):  # returns cosecant of an angle in degrees
    import math
    if x % 180 == 0:
        return "Error! Cosecant undefined for this angle."
    return 1 / math.sin(math.radians(x))

def radians_to_degrees(x): #converts radians to degrees
    import math
    return math.degrees(x)

def degrees_to_radians(x): #converts degrees to radians
    import math
    return math.radians(x)

def exponential(x): #returns e raised to the power of x
    import math
    return math.exp(x)

def absolute(x): #returns absolute value of a number
    return abs(x)

def maximum(x, y): #returns maximum of two numbers
    return max(x, y)

def minimum(x, y): #returns minimum of two numbers
    return min(x, y)

def main():
    #make user freindly interface here
    print("Welcome to the Calculator!")