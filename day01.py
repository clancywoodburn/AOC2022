f = [[int(j) for j in i.split("\n")] for i in open("input.txt").read().strip().split("\n\n")]
print(max([sum(i) for i in f]))
print(sorted([sum(i) for i in f]))