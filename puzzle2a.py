with open("puzzle2_input.txt", "r") as f:
	lines = f.readlines()

safe = 0
for line in lines:
	nums = [int(token) for token in line.strip().split(" ")]
	check_increase = True
	last_num = nums[0]
	failed = False
	for i in range(1, len(nums)):
		curr_num = nums[i]
		diff = abs(curr_num - last_num)
		if diff == 0 or diff > 3:
			failed = True
			break
		if curr_num < last_num and check_increase:
			if i == 1:
				check_increase = False
			else:
				failed = True
				break
		if curr_num > last_num and not check_increase:
			failed = True
			break
		last_num = curr_num
	if not failed:
		safe += 1
print(safe)