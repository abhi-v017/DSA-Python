f = open("hello.txt", "r")
x = f.read()
y = f.readline()
z = f.readlines()
f.close()

with open("hello.txt", "r") as f:
    a = f.read()
    b = f.readline()
    c = f.readlines()
# no need to close the file when using 'with' statement

with open("hello2.txt", "w") as f:
    f.write("hello this is the second file\n")
    f.write("that is been created...\n")
    f.write("this is the third line\n")
    
with open("hello2.txt", "a") as f:
    f.write("this line is been appended\n")
    f.write("this is the last line\n")