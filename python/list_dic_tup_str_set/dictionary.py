d = {"name": "Alice", "age": 30, "city": "New York"}
d.get("name")
d.keys()
d.values()
d.items()
d.update({"age": 31})
d.pop("city")
# Dictionarys are mutable and unordered collections of key-value pairs
print("Dictionary:", d) 
d["country"] = "USA"
print("Updated Dictionary:", d)
d.clear()
print("Cleared Dictionary:", d)

for i in d:
    print(i, d[i])
    
for key, value in d.items():
    print(key, value)
    
for i in d.keys():
    print(i)

for i in d.values():
    print(i)