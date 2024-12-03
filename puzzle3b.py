with open("puzzle3_input.txt", "r") as f:
	lines = f.readlines()

import re
p = re.compile('mul\(([0-9]+),([0-9]+)\)')
acc = 0
for line in lines:
	matches = p.findall(line)
	for match in matches:
		acc += int(match[0]) * int(match[1])

print(acc)