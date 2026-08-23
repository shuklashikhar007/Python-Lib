# Q1
def is_even(n):
    return n % 2 == 0
print(is_even(10))
def calculate(a, b):
    return a + b, a - b, a * b
s, d, p = calculate(10, 5)
print(s)  # 15
print(d)  # 5
print(p)  # 50
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
# Binary search 
n = len(nums)
l = 0
h = n-1
ans = -1
tar = 15
while l <= h:
    mid = l + (h-l)//2
    if nums[mid] == tar : 
        ans = mid 
        break
    elif nums[mid] > tar:
        h = mid - 1
    else: l = mid + 1
print(ans)




