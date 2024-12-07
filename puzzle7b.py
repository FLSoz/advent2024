with open("puzzle7_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

acc = 0

import math


def matches(total, vals):
	if not vals:
		return total == 0
	if total == 0:
		return not vals
	if total < 0:
		return False
	last = vals[-1]
	if len(vals) == 1:
		return total == last
	factor = int(math.pow(10, math.ceil(math.log10(last + 1))))
	if total % last == 0:
		# divisible
		if matches(total // last, vals[:-1]):
			return True
		elif len(vals) > 1 and total % factor == last and matches((total - last) // factor, vals[:-1]):
			return True
		elif matches(total - last, vals[:-1]):
			return True
	elif total < last:
		return False
	elif len(vals) > 1 and total % factor == last and matches((total - last) // factor, vals[:-1]):
		return True
	elif matches(total - last, vals[:-1]):
		return True
	return False


for line in lines:
	sp1 = line.split(':')
	total = int(sp1[0])
	vals = [int(f) for f in sp1[1].strip().split(' ')]
	if matches(total, vals):
		acc += total

print(acc)