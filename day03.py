f = open("input.txt").read().strip().split("\n")
items = []
for i in f:
	a = set(list(i[:len(i)//2]))
	b = set(list(i[len(i)//2:]))
	items += list(a.intersection(b))
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum([priority.index(i) + 1 for i in items]))

# PART 2
badges = []
for i in range(0,len(f),3):
	a = set(f[i])
	b = set(f[i+1])
	c = set(f[i+2])
	badges += list(a.intersection(b).intersection(c))
print(sum([priority.index(i) + 1 for i in badges]))