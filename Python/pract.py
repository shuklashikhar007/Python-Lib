# hashing in python
mp = {}
name = "ShikharShukla"
for c in name:
    mp[c] = mp.get(c, 0) + 1
for c in mp:
    print(c, mp[c])
# prefix sum
diff = [[1, 2], [3, 4], [5, 6]]
n = 8
a = [0] * n
for l, r in diff:
    a[l] += 1
    if r + 1 < n:
        a[r + 1] -= 1
for i in range(1, n):
    a[i] = a[i] + a[i - 1]
print(a)
arr = [10,20,30,40,50]
pref = [0] * len(arr) # imp syntax pehle se size assing karne ke liye
pref[0] = arr[0]
for i in range(1,len(arr),1) : 
    pref[i] = arr[i]  + pref[i-1]
print(pref)
#house robber 1 in python
arr = [10,3,45,6,90]
dp = [0] * len(arr)
dp[0] = arr[0]
if(arr[0] > arr[1]) : dp[1] = arr[0]
if(arr[1] >= arr[0]) : dp[1] = arr[1]
for i in range(2,len(arr),1) : 
    dp[i] = max(arr[i] + dp[i-2], dp[i-1])
print(dp)
