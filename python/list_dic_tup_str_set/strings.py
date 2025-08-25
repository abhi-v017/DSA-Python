a = "I am Abhishek"

# Iteration
for i in a:
    print(i)

for i in range(0, len(a)):
    print(a[i])
    
for i in range(len(a)-1, -1, -1):
    print(a[i])
    
a.title()
a.upper()   
a.lower()
a.strip()
a.replace("I", "You")
a.split(" ")
a.find("Abhi")
a.index("A")
a.count("a")
a.startswith("I")
a.endswith("k")
a.isalnum()
a.isalpha()
a.isdigit()
a.islower()
a.isupper()
a.isspace()
a.join(" Hello ")

print(a)