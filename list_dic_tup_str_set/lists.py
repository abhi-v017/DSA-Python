list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d','e','f']

print("List1:",list1)
print("List2:",list2)

# Iterations
for i in list1:
    print(i)

for i in range(0, len(list1)):
    print(list1[i])
    
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
print(sorted(list1, reverse=True))

list1.append(7)
list1.insert(0,0)
list1.remove(3)
list1.pop()
list1.index(4)
list1.count(2)
list1.extend([8,9,10])
list1.reverse() 
list1.clear()


# Membership Operators
print(3 in list1)
print(10 not in list1)

# List comprehension
myList = []
for i in range(0,11):
    myList.append(i)

my_list = [i for i in range(0,11)]

# List slicing
print(my_list[2:5])
print(my_list[:5])
print(my_list[5:])
print(my_list[::2])
print(my_list[::-1])