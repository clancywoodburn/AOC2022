from functools import cmp_to_key

f = [[eval(j) for j in i.split("\n")] for i in open("input.txt").read().strip().split("\n\n")]

def compare(a,b):
	# print(f'Compare {a} and {b}')
	match a,b:
		case int(), int():
			return a - b
		case list(), list():
			for i in range(min(len(a),len(b))):
				if (r := compare(a[i],b[i])) != 0: return r
			return len(a) - len(b)
		case _:
			if type(a) is int:
				return compare([a], b)
			return compare(a, [b])
part1 = 0
for i in range(len(f)):
	if compare(f[i][0], f[i][1]) < 0:
		part1 += 1 + i
print(part1)

n = [[[2]], [[6]]]
for i in f: n += i
n = sorted(n, key=cmp_to_key(compare))
print((n.index([[2]]) + 1) * (n.index([[6]]) + 1))