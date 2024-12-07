with open("puzzle6_input.txt", "r") as f:
	lines = [list(line.strip()) for line in f.readlines()]

curr_i = 0
curr_j = 0
for i in range(len(lines)):
	line = lines[i]
	for j in range(len(line)):
		if '^' in line[j]:
			curr_i = i
			curr_j = j
			break

start_i = curr_i
start_j = curr_j

from enum import Enum

# up 0
# right 1
# down 2
# left 3


def rotate(direction):
	if direction == 3:
		return 0
	else:
		return direction + 1

dir_chars = ['^', '>', 'V', '<',]

def get_deltas(direction):
	delta_i = 0
	delta_j = 0
	if direction == 0:
		delta_i -= 1
	elif direction == 1:
		delta_j += 1
	elif direction == 2:
		delta_i += 1
	else:
		delta_j -= 1
	return (delta_i, delta_j)

import copy

import pickle

acceptable = set()
rejected = set()


direction = 0
delta_i, delta_j = get_deltas(direction)
steps = 0
prior_steps = 0
hits = set()
import time
start = time.time()
while True:
	next_j = curr_j + delta_j
	next_i = curr_i + delta_i
	
	if 0 <= next_i < len(lines) and 0 <= next_j < len(line):
		next_cell = lines[next_i][next_j]
		if '#' in next_cell:
			# blocked
			hits.add((next_i, next_j, direction))
			direction = rotate(direction)
			delta_i, delta_j = get_deltas(direction)
		else:
			# test
			if (next_i, next_j) not in rejected and (next_i, next_j) not in acceptable:
				succeeded = False
				if 0 <= next_i < len(lines) and 0 <= next_j < len(line) and lines[next_i][next_j] == '.':
					clean_hits = set(list(hits))
					hyp_i = curr_i
					hyp_j = curr_j
					hyp_rotate = rotate(direction)
					hyp_delta_i, hyp_delta_j = get_deltas(hyp_rotate)
					lines[next_i][next_j] ='#'
					clean_hits.add((next_i, next_j, direction))
					while True:
						hyp_next_j = hyp_j + hyp_delta_j
						hyp_next_i = hyp_i + hyp_delta_i
						if 0 <= hyp_next_i < len(lines) and 0 <= hyp_next_j < len(line):
							if '#' in lines[hyp_next_i][hyp_next_j]:
								if (hyp_next_i, hyp_next_j, hyp_rotate) in clean_hits:
									acceptable.add((next_i, next_j))
									succeeded = True
									break
								clean_hits.add((hyp_next_i, hyp_next_j, hyp_rotate))
								hyp_rotate = rotate(hyp_rotate)
								hyp_delta_i, hyp_delta_j = get_deltas(hyp_rotate)
							else:
								hyp_i = hyp_next_i
								hyp_j = hyp_next_j
						else:
							break
					lines[next_i][next_j] = '.'
				if not succeeded:
					rejected.add((next_i, next_j))

			curr_i = next_i
			curr_j = next_j
		steps += 1
		if not steps - ((steps // 100) * 100):
			print(f"step {steps} / 4580")
			print(len(acceptable))
	else:
		break
end = time.time()
print(len(acceptable))
print(end - start)
