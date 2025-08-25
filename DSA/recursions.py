# when a function calls iteself directly or indirectly

count = 0
def func1():   # head recursion
    global count
    if count == 4:
        return
    else:
        print("Hello")
        count+=1
        func1()
func1()

def func2(): # tail recursion
    global count
    if count == 4:
        return
    else:
        count+=1
        func2()
        print("Hello")
func2()

# functional recursion
def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# time complexity: O(n)
# space complexity: O(n) due to the stack space used by recursive calls

def reverse_arr(arr, left, right):
    if left>=right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_arr(arr, left+1, right-1)
    
arr = [1,2,3,4,5]
reverse_arr(arr, 0, len(arr)-1)
print(arr)