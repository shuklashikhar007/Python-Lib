print("Starting of Numpy as a library")
import numpy as np 
import time as t
start = t.time()
py_list = [i*2 for i in range(100000)]
print("\n list op time : ", t.time()-start)
np_arr = np.arange(100000) * 2
print("\n numpy op time : ", t.time()-start)
a = np.array([[1,2,3],[4,5,6]])
print(a)
# ndim -> method to know the number of dimensions here
print(a.ndim)
print(a.shape) # row X col print karega ye
print(a.size) # row*col ans hoga yaha
print(a.dtype)
# special array banane ke method
c = np.zeros(5)
print(c)
d = np.zeros((2,3))
print(d)
e = np.full((2,3),7)
print(e)
f= np.eye(3)
print(f)
# linespace -> generate n equally spaced number b/w a start and end value
g = np.linspace(0,1,5)
print(g) 
# indexing and slicing all are same as normal python 
# indexing 2D arrays
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1])
print(a[1, 2])
print(a[0 : 2,0 : 2])
# Mathematical operations -> is library ka asli use yaha par hoga 
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a+b)
print(b-a)
print(a*b)
print(b/a)
c = [5,10,15,20] # normal py list
print(a+c)
z = np.array([1,2,3,4,5])
print(z*2) # ek sath puri arr mai multiply
# vectorization
print(z+10)
# ye likhne ki wajaye
for i in range(len(a)): a[i] *= 2
# ham sidha likhege
a *= 2
# basic stats
a = np.array([10,20,30,40,50])
ispoint = t.time()
print(np.sum(a))
print("time taken by code to get compiled: ", t.time()- ispoint)
yahapar = t.time()
print(np.mean(a))
print("time taken by code to get compiled : ", t.time()-yahapar)
print(np.min(a))
print(np.max(a))
# standard deviation
print(np.std(a))
print(np.var(a))
# concept of axis
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(a,axis=0)) # sum along col
print(np.sum(a,axis=1)) # sum along rows
# Reshaping
a = np.arange(1,7)
b = a.reshape(2,3)
print(b)
a.reshape(3,2)
print(a)
# flatten a 2D array karne ka method
b = a.flatten()
print(b)
# Boolean Filtering 
a = np.array([10,15,20,25,30])
print(a > 20)
# print filter lagake element
print(a[a>20])
# to get even numbers
print(a[a%2 == 0])
# Random number generator syntax
print(np.random.rand(5))
np.random.rand(1,10,5) # (st,end,amount)
# random integers
np.random.randint(1,10,5)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = A @ B
print(C)
# alternate tarika
# sawal 
marks = np.array([[80,90,70],[60,75,85],[90,95,92]])
print(marks.shape)
print(np.mean(marks,axis = 1))
print(np.mean(marks,axis=0))
print(np.max(marks))
avg = np.mean(marks,axis = 1)
# students jinka avg 80 se jyada hai
print(avg[avg>80])









