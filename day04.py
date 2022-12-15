f = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in open("input.txt").read().strip().split("\n")]

part1 = 0
part2 = 0
for i in f:
	a = set(range(i[0][0], i[0][1]+1))
	b = set(range(i[1][0], i[1][1]+1))
	c = a & b
	part1 += len(c) in [len(a), len(b)]
	part2 += len(c) > 0
print(part1, part2)