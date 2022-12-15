f = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in open("input.txt").read().strip().split("\n")]
max_y = 0
grid = {}
for i in f:
	for j in range(len(i)-1):
		start = i[j]
		end = i[j+1]
		if end[0] < start[0] or end[1] < start[1]:
			start, end = end, start
		if end[1] > max_y: max_y = end[1]
		for x in range(start[0], end[0]+1):
			for y in range(start[1], end[1]+1):
				grid[(x,y)] = True
max_y += 2
for _ in range(0,1000): grid[(_,max_y)] = True

def place_sand(x, y):
	# if y == max_y: return None
	if not grid.get((x,y+1), False):
		return place_sand(x,y+1)
	elif not grid.get((x-1,y+1), False):
		return place_sand(x-1,y+1)
	elif not grid.get((x+1,y+1), False):
		return place_sand(x+1,y+1)
	return (x,y)

sand_count = 0
while True:
	s = place_sand(500,0)
	if s == None or grid.get((500,0), False): break
	grid[s] = True
	sand_count += 1
print(sand_count)