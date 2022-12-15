from math import prod

f = [[int(j) for j in list(i)] for i in open("input.txt").read().strip().split("\n")]

def check_visible(x, y):
	v = f[x][y]
	views = []
	views.append([f[i][y] for i in range(x)][::-1])
	views.append([f[i][y] for i in range(x+1, len(f))])
	views.append([f[x][i] for i in range(y)][::-1])
	views.append([f[x][i] for i in range(y+1, len(f))])
	a = any([all([j<f[x][y] for j in i]) for i in views])
	b = prod([next((c+1 for c in range(len(i)) if i[c] >= v), len(i)) for i in views])
	return a,b

part1 = 0
part2 = 0

for i in range(len(f)):
	for j in range(len(f[i])):
		p1,p2 = check_visible(i,j)
		part1 += p1
		if p2 > part2: part2 = p2
print(part1, part2)