with open("puzzle6_input.txt", "r") as f:
	lines = [list(line.strip()) for line in f.readlines()]

acc = 1
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

try:
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
				rotate()
			else:
				if next_cell != 'X':
					lines[next_i][next_j] = 'X'
					acc += 1
				curr_i = next_i
				curr_j = next_j
		else:
			break

except Exception as e:
	print(e)
	pass

print(acc)
