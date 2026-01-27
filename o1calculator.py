#calculator

val1=int(input("Enter first value: "))
val2=int(input("Enter second value: "))

print("Select operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

userinput=int(input("Enter your choice: "))
if userinput==1:
    print("Addition:", val1 + val2)
elif userinput==2:
    print("Subtraction:", val1 - val2)
elif userinput==3:
    print("Multiplication:", val1 * val2)
elif userinput==4:
    print("Division:", val1 / val2)
else:
    print("Invalid input! Performing all operations by default.")40