sqaures = [x*x for x in range(5)]
print(sqaures)
# general pattern => 
# [exp for var in range]
even = [x for x in range(10) if x % 2 == 0]
# [exp for var in range if condition]
# dic comp
squares = {x: x*x for x in range(10) if x % 2 == 0}
# zip feature
names = ["A", "B", "C"]
marks = [90, 80, 70]
# pair up kardiya names aur marks ko ek sath
students = dict(zip(names, marks))
print(students)
# map function
# apply a function to every element
def square(x):
    return x*x
# marks ke har ek element par square function laga do
result = list(map(square,marks))
print(result)
# filter() -> keep only wo element that satisfy a condition
nums = [1,2,3,4,5,6]
def is_even(x):
    return x%2 == 0
result = list(filter(is_even,nums))
print(result)
# lambda -> in line anonymous function 
# syntax 
# lambda arguements : expression
square = lambda x : x*x
print(square(5))
add = lambda a,b : a+b
print(add(2,3))
students = [
    ("A", 90),
    ("B", 70),
    ("C", 85)
]
# custom sort by marks ( 2nd value )
students.sort(key = lambda x : x[1])
print(students)
students.sort(key = lambda x : x[1], reverse=True)
# sorting dictionaries
students2 = [
    {"name": "A", "marks": 90},
    {"name": "B", "marks": 70},
    {"name": "C", "marks": 85}
]
students2.sort(key = lambda x : x["marks"])
print(students2)
# any() → at least one is True
# all() → everything is True

