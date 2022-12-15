f = [i.split(" ") for i in open("input.txt").read().strip().split("\n")]


# PART 1
score = 0
for i in f:
	scores = {"X": 1, "Y": 2, "Z": 3}
	score += scores[i[1]]
	if i in [["A", "Y"], ["B", "Z"], ["C", "X"]]: score += 6
	if i in [["A", "X"], ["B", "Y"], ["C", "Z"]]: score += 3
print(score)

# PART 2
score = 0
for i in f:
	scores = {"X": 0, "Y": 3, "Z": 6}
	score += scores[i[1]]
	if i in [["A", "X"], ["B", "Z"], ["C", "Y"]]: score += 3
	if i in [["A", "Z"], ["B", "Y"], ["C", "X"]]: score += 2
	if i in [["A", "Y"], ["B", "X"], ["C", "Z"]]: score += 1
print(score)