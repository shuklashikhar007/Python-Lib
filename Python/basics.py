array = [1,2,3]
# array -> []
# tuple -> ()
# dictionary -> {}
mydic = {'name' : 'shikhar', 'age' : 20, 'college' : 'IIT-BHU' }
print(mydic['name'])
print(mydic['age'])
print(mydic['college'])
mytup = ('name' , 20, 'pagalhati', 'chatpata samosa')
print(mytup[2])
# arithematic 
# +,-,*,/ same as C++
a = 10
b = 3
print(a/b)
print(a//b) # floor kar denge
print(a%b)
print(a**10)
#comparison operator -> same as C++
# membership operator
nums = [10,20,30,40]
print(20 in nums) # we can check direct ki hai ki nahi element present
a = [1,2,3]
b = [4,5,6]
print(a is b)
c = b
print(c is b)
# a is b actually checks whether these are the same object or not 
# some things have a natural true value
print(bool(0)) # 0 is naturally false
print(bool(10)) # 10 is naturally true
# if any of list tuple ya dict mai data nahi hai to it is bydefault false
# if data hoga to it will be true
# Loops
for i in range(5): print(i)
for i in range(2,6): print(i)
# print from start till stop-1
for i in range(2,10,2): print(i)
# print from start till end - step and inc step num every time
# reverse loops
for i in range(10,0,-1) : print(i)
nums = [10,20,30,40]
for x in nums: print(x)
for i,x in enumerate(nums):
    print(i,x)
for i,x in enumerate(nums):
    print(i,x)
i = 0
while i < 5:
    print(i)
    i += 1
j = 0
while j < 4 :
    if(j == 3) : break
    print(j)
    j += 1
for i in range(5):
    if i == 2: continue
    print(i)
for i in range(3):
    for j in range(5): 
        print(i,j)
for i in range(5):
    for j in range(i+1):print("*", end="")
    # upper line is similar to C++ cout << "*"
    # instead of using cout << "*" << endl -> this is the default code
    print()
# python's else with loops
for i in range(5):
    print(i)
else:
    print("Loop finished")
for i in range(5):
    if i==2:
        break
else:
    print("Loop finished") # this does not run since loop was terminated by break already
arr = [10,20,30,40]
for x in nums:
    if x == 70:
        print("Found")
        break
else:
    print("Not Found")
name = "Shikhar"
for ch in name : print(ch, end="")
print()
cnt = 0
for ch in name:
    if ch == 'a':
        cnt += 1
print(cnt)
# when we need to iterate in index only
for i in range(len(arr)): print(i)
# both index and value
for i,x in enumerate(arr): print(i,x)
# Functions in python
def add(a,b) :
    return a+b
# no {} scope brackets indentation will define the body here
result = add(10,20)
print(result)
def greet():
    print("Hello")
def meranaam():
    print("Shikhar Shukla")
meranaam()
def square(x): return x*x
ans = square(5)
print(ans)
# default arguements wese hi dete hai jese ki C++ mai same way
def add(a,b=10): return a+b
ans = add(10)
print(ans)
ans = add(10,20)
print(ans)
# variable length arguements
def add(*args):
    sum = 0
    for x in args: sum += x
    return sum
ans = add(10,20,30)
print(ans)
# keyword arguements
def add(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
add(name="Shikhar",age=20,college="IIT-BHU")
def add(*args):
    total = 0
    for x in args:
        total += x
    return total
print(add(1,2,3,4,5))
def student(**kwargs):
    print(kwargs)
student(name="Shikhar", age = 20, branch = "Chemical")
# *args -> tuple
# **kwargs -> dictionary
# scope
x = 10
def test():
    x = 20
    print(x)
test()
print(x)
def factorial(n):
    if n == 0 : return 1
    return n*factorial(n-1)
# Python type hints don't enforce the type at runtime by themselves.
def add(a: int, b: int) -> int:
    return a + b
def square(x) : return x * x
f = square
print(f(5))
# python mai functions objects hote hai 
def square(x): return x*x
def apply(func,x):
    return func(x)
print(apply(square,5))


















