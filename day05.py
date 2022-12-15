f = [i.split("\n") for i in open("input.txt").read().strip("\n").split("\n\n")]
stacks = {}
for i in f[0][:-1]:
	for j in range(1,len(i), 4):
		if i[j] != " ": stacks[(j+3)//4] = [i[j]] + stacks.get((j+3)//4, [])
for i in f[1]:
	a = [int(j) for j in i.replace("move ", "").replace(" from ", ",").replace(" to ", ",").strip().split(",")]
	# for _ in range(a[0]):
	# 	stacks[a[2]] += [stacks[a[1]].pop()]
	stacks[a[2]] += stacks[a[1]][-a[0]:]
	stacks[a[1]] = stacks[a[1]][:-a[0]]
print("".join([stacks[i][-1] for i in range(1,10)]))