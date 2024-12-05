from collections import defaultdict
from functools import cmp_to_key

with open("puzzle5_order_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

order = defaultdict(set)

for line in lines:
	nums = line.split('|')
	order[int(nums[0])].add(int(nums[1]))

with open("puzzle5_update_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

acc = 0

for line in lines:
	nums = [int(num) for num in line.split(',')]

	seen = set()
	failed = False
	for num in nums:
		if order[num] & seen:
			failed = True
			break
		seen.add(num)

	if failed:
		acc += sorted(nums, key=cmp_to_key(lambda item1, item2: 1 if item2 in order[item1] else -1 if item1 in order[item2] else 0))[len(nums)//2]

print(acc)