# list in python -> C++ se kahi jyada functionality
nums = [10,20,30,40]
print(nums[-1])
print(nums[-2])
print(nums[-(len(nums))]) # ye print karega first wala element 
nums.append(50)
nums.append(60)
print(nums)
nums.insert(1,100)
print(nums)
# nums.remove -> will remove the first occurence only
# nums.pop -> same as stack pop feature
# slicing
arr = [1,2,3,4,5,6,7,8]
print(arr[0:5])
# step slicing 
# list[start:stop:step] -> ye syntax hota hai
print(arr[1:8:2])
# reverse arr using slice 
print(arr[  : : -1])
nums.sort()
nums.sort(reverse=True)
x = sorted(nums) # sorted will make a new list here
print(x)
print(nums)
c = nums + arr
d = [0]*5
print(d)
dp = [-1]*100
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    print(matrix[i])
matrix2 = [[0]*3 for _ in range(3)]
even = [i for i in range(10) if i%2 == 0]
print(even)
e=arr # ye copy nhi hai both point to same memory location
f = arr.copy()  # ye real copy hai since yaha nayi array banegii







