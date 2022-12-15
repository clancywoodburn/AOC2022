f = open("input.txt").read().strip().split("\n")
fs = {"/" : {}}
pos = ["/"]
_ = 1
reading = False
while _ < len(f):
	l = f[_].strip().split(" ")
	
	if l[0] == "$":
		if l[1] == "ls":
			pass
		elif l[1] == "cd":
			if l[2] == "..":
				pos = pos[:-1]
			elif l[2] == "/":
				pos = ["/"]
			else:
				pos += [l[2]]
	else:
		currentspace = fs
		for i in pos:
			currentspace = currentspace[i]
		if l[0] == "dir":
			currentspace[l[1]] = {}
		else:
			currentspace[l[1]] = int(l[0])
	_ += 1

total = 0
mini = 1e9
target = 30000000 - (70000000 - 42805968)
print(target)
def calc_size(a):
	global total
	global mini
	global target
	if type(a) is int: return a
	val = sum([calc_size(a[i]) for i in a])
	if val <= 100000: total += val
	if val <= mini and val >= target: mini = val
	return val
print(calc_size(fs), total, mini)