a = [1, 2, 3, 2, 1, 2, 4, 3, 1]
map = {}
for x in a : map[x] = map.get(x,0) + 1
print(sorted(map))
