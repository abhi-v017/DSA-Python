def add():
    a = 10
    b = 21
    return a + b

print("Sum:", add())

def subtract(a, b):
    return a - b

print("Difference:", subtract(21, 10))

#named parameters
def marks(hin, eng, math):
    return hin + eng + math

print("Total Marks:", marks(eng=85, hin=90, math=95))

# default parameters
def greet(name="Guest"):
    return "Hello, " + name + "!"
print(greet())
print(greet("Abhishek"))