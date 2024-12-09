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

def get_antinodes(loc_list):
	# every 2 pairs
	antinodes = set()
	for i in range(len(loc_list)):
		curr = loc_list[i]
		for j in range(i+1,len(loc_list)):
			test = loc_list[j]
			diff = (test[0] - curr[0], test[1] - curr[1])
			if 0 <= (new_i := curr[0] - diff[0]) < size_i and 0 <= (new_j := curr[1] - diff[1]) < size_i:
				antinodes.add((new_i, new_j))
			if 0 <= (new_i := test[0] + diff[0]) < size_i and 0 <= (new_j := test[1] + diff[1]) < size_j:
				antinodes.add((new_i, new_j))
	return antinodes

antinodes = {k: get_antinodes(v) for k,v in frequencies.items()}

import functools

def part1():
	all_nodes = functools.reduce(lambda a,b: a | b, antinodes.values(), set())
	print(len(all_nodes))

part1()