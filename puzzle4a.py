with open("puzzle4_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

acc = 0

corr = ['M', 'A', 'S']


def get_match(i, j, step_i=0, step_j=0):
	for z in range(3):
		if lines[i+(step_i*(z+1))][j+(step_j*(z+1))] != corr[z]:
			return 0
	return 1


for i in range(len(lines)):
	line = lines[i]
	for j in range(len(line)):
		char = line[j]
		if char == 'X':
			if j >= 3:
				# go left
				acc += get_match(i, j, step_j=-1)
				if i >= 3:
					# go up left
					acc += get_match(i, j, step_i=-1, step_j=-1)
				if i <= len(lines) - 4:
					# go down left
					acc += get_match(i, j, step_i=1, step_j=-1)
			if j <= len(line) - 4:
				# go right
				acc += get_match(i, j, step_j=1)
				if i >= 3:
					# go up right
					acc += get_match(i, j, step_i=-1, step_j=1)
				if i <= len(lines) - 4:
					# go down right
					acc += get_match(i, j, step_i=1, step_j=1)
			if i >= 3:
				# go up
				acc += get_match(i, j, step_i=-1)
			if i <= len(lines) - 4:
				# go down
				acc += get_match(i, j, step_i=1)

print(acc)