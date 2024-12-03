with open("puzzle3_input.txt", "r") as f:
	lines = f.readlines()

import re
p = re.compile("mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))")
acc = 0
record = True
for line in lines:
	matches = p.findall(line)
	for match in matches:
		if match[2] == "do()":
			record = True
		elif match[3] == "don't()":
			record = False
		elif record:
			acc += int(match[0]) * int(match[1])
print(acc)