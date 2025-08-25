# print statement
print("Hello world!")
print("I am", end=" ")
print("Abhsihek")

# variables
a=10
b="Abhishek"

print(a)
print("i am", b)
print(f"i am {b}")

# Escape sequences
print("Hello \nworld")
print("Hello \tworld")
print("Hello \\world")
print("Hello \'world\'")
print("Hello \"world\"")
print("Hello \bworld")

# Datatypes
a=10
b="Abhishek"
c=10.5
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Type casting
a=str(a)
print("Converted type",type(a))
b=int(20.5)
print("Converted type",type(b))

# Input function
name=input("Enter your name: ")
print("Hello",name)

#operators
a = 10
b = 20
# Arithmetic Operators
print("a + b =", a + b)        
print("a - b =", a - b)
print("a * b =", a * b) 
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Comparison Operators
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)  
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("a > 5 and b < 25:", a > 5 and b < 25)
print("a > 15 or b < 25:", a > 15 or b < 25)
print("not(a > 5):", not(a > 5))   

# Assignment Operators
a += 5  
print("a after a += 5:", a)
a -= 3      
print("a after a -= 3:", a)
a *= 2      
print("a after a *= 2:", a) 
a /= 4
print("a after a /= 4:", a)
a %= 3
print("a after a %= 3:", a)
a **= 2
print("a after a **= 2:", a)
a //= 2
print("a after a //= 2:", a)

# if-elif-else statement
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# Loops
# for loop
print("For loop:")
for i in range(5):
    print(i)
    
# while loop
print("While loop:")
count = 0
while count < 5:
    print(count)
    count += 1
    
# Control statements
print("Control statements:")
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)