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
    print("🧮 Welcome to the Calculator! 🧮")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root (sqrt)")
    print("9. Percentage (%)")
    print("10. Factorial (!)")
    print("11. Average (avg)")
    print("12. Cube (cube)")
    print("13. Cube Root (cbrt)")
    print("14. Logarithm (log)")
    print("15. Sine (sin)")
    print("16. Cosine (cos)")
    print("17. Tangent (tan)")
    print("18. Cotangent (cot)")
    print("19. Secant (sec)")
    print("20. Cosecant (csc)")
    print("21. Radians to Degrees (rad2deg)")
    print("22. Degrees to Radians (deg2rad)")
    print("23. Exponential (exp)")
    print("24. Absolute (abs)")
    print("25. Maximum (max)")
    print("26. Minimum (min)")
    print("Type 'quit' to exit the calculator.\n")
    while True:
        operation = input("Enter operation: ").strip().lower()
        
        if operation == 'quit':
            print("👋 Thanks for using the calculator!")
            break
        
        try:
            if operation in ['+', 'add', '1']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {add(x, y)}\n")
            elif operation in ['-', 'subtract', '2']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {subtract(x, y)}\n")
            elif operation in ['*', 'multiply', '3']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {multiply(x, y)}\n")
            elif operation in ['/', 'divide', '4']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {divide(x, y)}\n")
            elif operation in ['^', 'power', '5']:
                x = float(input("Enter base number: "))
                y = float(input("Enter exponent number: "))
                print(f"Result: {power(x, y)}\n")
            elif operation in ['%', 'modulus', '6']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {modulus(x, y)}\n")
            elif operation in ['//', 'floor divide', '7']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {floor_divide(x, y)}\n")    
            elif operation in ['sqrt', 'square root', '8']:
                x = float(input("Enter number: "))
                print(f"Result: {square_root(x)}\n")
            elif operation in ['%', 'percentage', '9']:
                x = float(input("Enter the total number: "))
                y = float(input("Enter the percentage to calculate: "))
                print(f"Result: {percentage(x, y)}\n")
            elif operation in ['!', 'factorial', '10']:
                x = int(input("Enter a non-negative integer: "))
                print(f"Result: {factorial(x)}\n")
            elif operation in ['avg', 'average', '11']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {average(x, y)}\n")

            elif operation in ['cube', '12']:
                x = float(input("Enter number: "))
                print(f"Result: {cube(x)}\n")
            elif operation in ['cbrt', 'cube root', '13']:
                x = float(input("Enter number: "))
                print(f"Result: {cube_root(x)}\n")
            elif operation in ['log', 'logarithm', '14']:
                x = float(input("Enter number: "))
                base_input = input("Enter base (default is 10): ").strip()
                base = float(base_input) if base_input else 10
                print(f"Result: {logarithm(x, base)}\n")
            elif operation in ['sin', 'sine', '15']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {sine(x)}\n")
            elif operation in ['cos', 'cosine', '16']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {cosine(x)}\n")
            elif operation in ['tan', 'tangent', '17']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {tangent(x)}\n")
            elif operation in ['cot', 'cotangent', '18']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {cotangent(x)}\n")
            elif operation in ['sec', 'secant', '19']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {secant(x)}\n")
            elif operation in ['csc', 'cosecant', '20']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {cosecant(x)}\n")
            elif operation in ['rad2deg', 'radians to degrees', '21']:
                x = float(input("Enter angle in radians: "))
                print(f"Result: {radians_to_degrees(x)}\n")
            elif operation in ['deg2rad', 'degrees to radians', '22']:
                x = float(input("Enter angle in degrees: "))
                print(f"Result: {degrees_to_radians(x)}\n")
            elif operation in ['exp', 'exponential', '23']:
                x = float(input("Enter exponent value: "))
                print(f"Result: {exponential(x)}\n")
            elif operation in ['abs', 'absolute', '24']:
                x = float(input("Enter number: "))
                print(f"Result: {absolute(x)}\n")
            elif operation in ['max', 'maximum', '25']: 
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {maximum(x, y)}\n") 
            elif operation in ['min', 'minimum', '26']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {minimum(x, y)}\n")                                
            # Add more operations here following the same pattern
            else:
                print("Invalid operation! Please try again.\n")
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
if __name__ == "__main__":
    main()  

    #is the code correct ? Yes, the code is correct. It implements a comprehensive calculator with various mathematical operations and a user-friendly interface.
    #is the code in loop so that user ca n perform multiple calculations without restarting the program? Yes, the code is in a loop that allows the user to perform multiple calculations until they choose to exit by typing 'quit'.
    