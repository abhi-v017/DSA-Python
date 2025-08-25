s = {1,2,34,55,5,6,3,2,1,4,5}  # unordered collection of unique items
s1 = {1,2,3}

print("Set:",s)
print("Set1:",s1)

# Iterations
for i in s:
    print(i)

for i in range(0, len(s)):
    print(i)

# Set operations
s.add(7)    
s.update([8,9,10])
s.remove(3)
s.discard(4)
s.pop()  # removes and returns an arbitrary element
s.clear()
print("Updated Set:",s) 
print("Is s1 subset of s?", s1.issubset(s))
print("Is s1 superset of s?", s1.issuperset(s)) 
print("Union of s and s1:", s.union(s1))
print("Intersection of s and s1:", s.intersection(s1))
print("Difference of s and s1:", s.difference(s1))
print("Symmetric difference of s and s1:", s.symmetric_difference(s1))  
print("Length of set s:", len(s))
print("Is 5 in set s?", 5 in s)
print("Is 15 not in set s?", 15 not in s)

# Set comprehension
mySet = {i for i in range(0,11) if i%2==0}
print("Set Comprehension:", mySet)
