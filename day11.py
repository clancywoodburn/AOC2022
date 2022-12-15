f = open("input.txt").read().strip().split("\n\n")

class Monkey:
	def __init__(self, s):
		ls = s.split("\n")
		self.id = int(ls[0][-2])
		self.items = [int(i) for i in ls[1].strip("  Starting items: ").split(", ")]
		self.op = ls[2][19:]
		self.div = int(ls[3].split(" ")[-1])
		self.t = int(ls[4].split(" ")[-1])
		self.f = int(ls[5].split(" ")[-1])
		self.activity = 0
	
	def inspect(self):
		self.activity += 1
		a = self.items.pop(0)
		a = eval(self.op.replace("old", "a"))
		if a % self.div == 0:
			return (self.t, a % lcm)
		return (self.f, a % lcm)
	
	def has_items(self):
		return len(self.items) != 0
	
	def add_item(self, n):
		self.items.append(n)

monkeys = []
lcm = 3
for i in f:
	monkeys.append(Monkey(i))
	lcm *= monkeys[-1].div

for _ in range(10000):
	if _ in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000]:
		print(_, [i.activity for i in monkeys])
	for i in range(len(monkeys)):
		while monkeys[i].has_items():
			m, n = monkeys[i].inspect()
			monkeys[m].add_item(n)

for i in monkeys:
	print(i.activity)