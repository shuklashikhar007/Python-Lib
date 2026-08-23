# tuple -> same list jesa but immutable object
point =(10,20)
print(point)
# main use -> to return multiple type of values from a function
def calculate(a,b):
    return a+b, a-b, a*b
# tuple -> (a+b,a-b,a*b)
value = calculate(10,20) # value mai tuple store hoga 
# swap 
a = 10 
b = 20
a,b = b,a
print(a)
print(b)
nums = [1,2,3,4,5,6,6,7,7,7,8,8,8,8,9,9,9]
unique = set(nums)
print(unique)
# set.remove(x) ->  error agar x nahi mila to 
# set.discard(x) -> will do nothing if x nahi mila to
aa = {1,2,3,4}
bb = {3,4,5,6}
print(aa-bb)
print(aa&bb)
print(aa|bb)
freq = {
    "key1" : 5,
    "key2" : 10
}
hash = {}
for x in nums:
    if x not in hash:
        # py mai agar x nahi hai hash mai to pehle
        # create karo fir freq badhao 
        hash[x]  = 0
    hash[x] += 1    
print(hash)
for key,val in hash.items():
    print(key,val)
def two_sum(nums, target):
    mp = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in mp:
            return [mp[need], i]
        mp[x] = i
    return []