with open("puzzle4_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

acc = 0


for i in range(1, len(lines)-1):
	line = lines[i]
	for j in range(1, len(line)-1):
		char = line[j]
		if char == 'A':
			m = 0
			s = 0
			tl = lines[i-1][j-1]
			tr = lines[i-1][j+1]
			bl = lines[i+1][j-1]
			br = lines[i+1][j+1]
			for elem in [tl,tr,bl,br]:
				if elem == 'M':
					m += 1
				if elem == 'S':
					s += 1
			if m == 2 and s == 2 and tl != br:
				acc += 1

print(acc)