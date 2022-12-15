f = open("input.txt").read().strip().split("\n")
cycle = 0
signal = 0
s = []
disp = "#" * 3 + " " * 37
for i in f:
	a = i.strip().split(" ")
	if a[0] == "noop":
		print(disp[cycle%40], end="")
		cycle += 1
		if cycle % 40 == 0:
			print("")
		if cycle in [20,60,100,140,180,220]:
			s.append((signal+1)*cycle)
	else:
		for _ in range(2):
			print(disp[cycle%40], end="")
			cycle += 1
			if cycle % 40 == 0:
				print("")
			if cycle in [20,60,100,140,180,220]:
				s.append((signal+1)*cycle)
		disp = disp[-int(a[1]):] + disp[:-int(a[1])]
		signal += int(a[1])
print(sum(s))