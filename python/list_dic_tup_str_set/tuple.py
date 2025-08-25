tup = (1,2,3,4,5,6)  # cann't change values after creation, immutable

print("Tuple:",tup)

# Iterations
for i in tup:
    print(i)    

for i in range(0, len(tup)):
    print(tup[i])

tup.count(3)
tup.index(4)