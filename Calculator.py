#this project is to create calculator 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y    
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return x ** 0.5
def percentage(x, y):
    return (x / 100) * y
def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number not defined."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def average(x, y):
    return (x + y) / 2
def cube(x):
    return x ** 3
def cube_root(x):
    if x >= 0:
        return x ** (1/3)
    else:
        return -(-x) ** (1/3)
 def logarithm(x, base=10):
    import math
    if x <= 0:
        return "Error! Logarithm of non-positive number not defined."
    return math.log(x, base)
def sine(x):
    import math
    return math.sin(math.radians(x))
def cosine(x):
    import math
    return math.cos(math.radians(x))
def tangent(x):
    import math
    return math.tan(math.radians(x))
def cotangent(x):
    import math
    if x % 180 == 0:
        return "Error! Cotangent undefined for this angle."
    return 1 / math.tan(math.radians(x))
def secant(x):
    import math
    if x % 90 == 0 and (x // 90) % 2 != 0:
        return "Error! Secant undefined for this angle."
    return 1 / math.cos(math.radians(x))
def cosecant(x):
    import math
    if x % 180 == 0:
        return "Error! Cosecant undefined for this angle."
    return 1 / math.sin(math.radians(x))
def radians_to_degrees(x):
    import math
    return math.degrees(x)
def degrees_to_radians(x):
    import math
    return math.radians(x)
def exponential(x):
    import math
    return math.exp(x)
   
