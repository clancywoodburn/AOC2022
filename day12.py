f = open("input.txt").read().strip().split("\n")

visited = {}
start = (0,0)
goal = (0,0)

for i in range(len(f)):
	f[i] = "#" + f[i].strip() + "#"
	if (n := f[i].find("S")) != -1:
		start = (i+1, n)
		f[i] = f[i].replace("S", "a")
	if (n := f[i].find("E")) != -1:
		goal = (i+1, n)
		f[i] = f[i].replace("E", "z")
f = ["#" * len(f[0])] + f + ["#" * len(f[0])]

def traverse(pos):
	vs = [pos]
	visited[pos] = 0
	while len(vs) > 0:
		pos = vs.pop(0)
		d = visited[pos]
		vals = [(pos[0], pos[1] + 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])]
		for nw in vals:
			if f[nw[0]][nw[1]] != "#" and ord(f[nw[0]][nw[1]]) +1 >= ord(f[pos[0]][pos[1]]) and visited.get(nw, -1) == -1:
				visited[nw] = d+1
				vs.append(nw)
	
traverse(goal)
print(f"Part 1: {visited[start]}")

best = 1e6
for x in range(len(f)):
	for y in range(len(f[0])):
		if f[x][y] == "a":
			best = min(visited.get((x,y), 1e6), best)

print(f"Part 2: {best}")
