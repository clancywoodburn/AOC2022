from numpy import sign

f = open("input.txt").read().strip().split("\n")
segs = []
for i in range(10):
	segs.append([0,0])

visi = []
for i in f:
	d, n = i.strip().split(" ")
	n = int(n)
	a = [0,0]
	if d == "U":
		a = [0,1]
	elif d == "D":
		a = [0,-1]
	elif d == "L":
		a = [-1,0]
	else:
		a = [1,0]
	for _ in range(n):
		segs[0][0] += a[0]
		segs[0][1] += a[1]
		for j in range(1,len(segs)):
			if not (segs[j][0] in range(segs[j-1][0]-1,segs[j-1][0]+2) and segs[j][1] in range(segs[j-1][1]-1,segs[j-1][1]+2)):
				segs[j][0] += sign(segs[j-1][0]-segs[j][0])
				segs[j][1] += sign(segs[j-1][1]-segs[j][1])
		if tuple(segs[-1]) not in visi:
				visi.append(tuple(segs[-1]))
print(len(visi))