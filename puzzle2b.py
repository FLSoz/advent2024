with open("puzzle2_input.txt", "r") as f:
	lines = f.readlines()


def check_failed(nums):
	check_increase = True
	last_num = nums[0]
	for i in range(1, len(nums)):
		curr_num = nums[i]
		diff = abs(curr_num - last_num)
		if diff == 0 or diff > 3:
			return True
		if curr_num < last_num and check_increase:
			if i == 1:
				check_increase = False
			else:
				return True
		if curr_num > last_num and not check_increase:
			return True
		last_num = curr_num
	return False

import time

start = time.time()
safe = 0
for j in range(len(lines)):
	line = lines[j]
	nums = [int(token) for token in line.strip().split(" ")]
	failed = check_failed(nums)
	if not failed:
		safe += 1
	else:
		for i in range(0, len(nums)):
			if not check_failed(nums[:i] + nums[i+1:]):
				safe += 1
				break
end = time.time()
print(safe)
print(end - start)