from collections import defaultdict

with open("puzzle5_order_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

order_before = defaultdict(set)

for line in lines:
	nums = line.split('|')
	order_before[int(nums[0])].add(int(nums[1]))

with open("puzzle5_update_input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

acc = 0

for line in lines:
	nums = [int(num) for num in line.split(',')]

	seen = set()
	failed = False
	for num in nums:
		if order_before[num] & seen:
			failed = True
			break
		seen.add(num)

	if not failed:
		acc += nums[len(nums)//2]

print(acc)