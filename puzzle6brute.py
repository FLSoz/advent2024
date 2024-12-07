with open("puzzle6_input.txt", "r") as f:
	lines = [list(line.strip()) for line in f.readlines()]

curr_i = 0
curr_j = 0
for i in range(len(lines)):
	line = lines[i]
	for j in range(len(line)):
		if line[j] == '^':
			curr_i = i
			curr_j = j
			line[j] = 'X'
			break

start_i = curr_i
start_j = curr_j

from enum import Enum

direction = 0
# up 0
# right 1
# down 2
# left 3


def rotate():
	global direction
	if direction == 3:
		direction = 0
	else:
		direction += 1

acc = 0

import time
start = time.time()
import copy
steps = 0
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] != '#' and lines[i][j] != '^':
			lines[i][j] = '#'
			curr_i = start_i
			curr_j = start_j
			hits = set()
			direction = 0
			while True:
				next_j = curr_j
				next_i = curr_i
				if direction == 0:
					next_i -= 1
				elif direction == 1:
					next_j += 1
				elif direction == 2:
					next_i += 1
				else:
					next_j -= 1
				
				if 0 <= next_i < len(lines) and 0 <= next_j < len(line):
					next_cell = lines[next_i][next_j]
					if next_cell == '#':
						# blocked
						if (next_i, next_j, direction) in hits:
							acc += 1
							break
						hits.add((next_i, next_j, direction))
						rotate()
					else:
						curr_i = next_i
						curr_j = next_j
				else:
					break
			lines[i][j] = '.'
		steps += 1
		if not steps - ((steps // 100) * 100):
			print(f"step {steps} / 4580")
			print(acc)

print(acc)
end = time.time()
print(end - start)