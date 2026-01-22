""""Rules 
of Variable in Python
Explore"""


#1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
_var1 = 10  
var2 = 20
print(_var1)
print(var2)

#2. Variable names can contain letters, digits (0-9), and underscores (_)
var_3 = 30
var4_5 = 40
print(var_3)
print(var4_5)

#3. Variable names are case-sensitive (e.g., myVar and myvar are different variables)
myVar = 50
myvar = 60
print("myVar:", myVar)
print("myvar:", myvar)

#4. Variable names cannot be the same as Python reserved keywords (e.g., if, else, while, for, etc.)
# The following line would cause a syntax error if uncommented                  
# if = 100
#   print(if)   
#    nice try to use reserved keywords as variable names        
