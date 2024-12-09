with open("puzzle8_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

from collections import defaultdict
frequencies = defaultdict(list)

for i in range(len(lines)):
	line = lines[i]
	for j in range(len(line)):
		char = line[j]
		if char != '.':
			frequencies[char].append((i,j))

size_i = len(lines)
size_j = len(lines[0])

antinodes = set()

def get_antinodes(loc_list):
	# every 2 pairs
	global antinodes
	for i in range(len(loc_list)):
		curr = loc_list[i]
		if len(loc_list) > 1:
			antinodes.add(curr)
		for j in range(i+1,len(loc_list)):
			test = loc_list[j]
			diff = (test[0] - curr[0], test[1] - curr[1])
			z = 1
			while True:
				if 0 <= (new_i := curr[0] - diff[0] * z) < size_i and 0 <= (new_j := curr[1] - diff[1] * z) < size_i:
					antinodes.add((new_i, new_j))
					z += 1
				else:
					break
			z = 1
			while True:
				if 0 <= (new_i := test[0] + diff[0] * z) < size_i and 0 <= (new_j := test[1] + diff[1] * z) < size_j:
					antinodes.add((new_i, new_j))
					z += 1
				else:
					break

for lists in frequencies.values():
	get_antinodes(lists)

print(len(antinodes))