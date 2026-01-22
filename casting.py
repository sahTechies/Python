x=str(2)
y=int(7)
z=float(9)
print("\n",x,"\n",y,"\n",z,"\n")
print(type(x)) 
print(type(y))
print(type(z))
input_var = input("Enter a value: ")
print("You entered:", input_var)

"""Trying to figure out input only takes string values or int also how to check"""
#casting in python
a = input("Enter an integer: ") 
b = int(a)
c = float(a)
print("Integer value:", b)
print("Float value:", c)

#it seems like here we can only take string values as input and then cast them to int or float as needed