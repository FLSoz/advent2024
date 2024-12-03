with open("puzzle2_input.txt", "r") as f:
	lines = f.readlines()


def check_failed(curr_num, last_num, check_increase):
	diff = abs(curr_num - last_num)
	violation_found = False
	if diff == 0 or diff > 3:
		violation_found = True
	if curr_num < last_num and check_increase:
		violation_found = True
	if curr_num > last_num and not check_increase:
		violation_found = True
	return violation_found

import time

start = time.time()
safe = 0
for j in range(len(lines)):
	line = lines[j]
	nums = [int(token) for token in line.strip().split(" ")]
	check_increase = True
	failed = False

	diff0 = abs(nums[0] - nums[1])
	diff1 = abs(nums[1] - nums[2])
	diffg = abs(nums[0] - nums[2])
	removed_ind = -1
	if diff0 not in range(1,4):
		# is good
		if diff1 not in range(1,4) and diffg not in range(1,4):
			failed = True
		else:
			if diff1 not in range(1,4):
				# remove 1
				check_increase = nums[2] > nums[0]
				removed_ind = 1
			elif diffg not in range(1,4):
				# remove 0
				check_increase = nums[2] > nums[1]
				removed_ind = 0
			else:
				# both work, need to choose
				if not check_failed(nums[3], nums[2], nums[2] > nums[0]):
					check_increase = nums[2] > nums[0]
					removed_ind = 1
				elif not check_failed(nums[3], nums[2], nums[2] > nums[1]):
					check_increase = nums[2] > nums[1]
					removed_ind = 0
				else:
					failed = True
	elif diff1 not in range(1,4):
		if diffg in range(1,4):
			# remove 1
			check_increase = nums[2] > nums[0]
			removed_ind = 1
		else:
			# remove 2
			removed_ind = 2
			check_increase = nums[1] > nums[0]
	else:
		if (nums[1] > nums[0]) != (nums[2] > nums[1]):
			# different directions, pick one
			if (nums[3] > nums[2]) == (nums[2] > nums[1]):
				# next = last segment ==> drop first
				# we know this one is in range
				removed_ind = 0
				check_increase = nums[2] > nums[1]
			else:
				# next != last segment ==> drop one in the mmiddle
				# overall trendd must be maintained
				if nums[2] in range(nums[0], nums[3]) and diffg in range(1,4):
					removed_ind = 1
					check_increase = nums[3] > nums[0]
				elif nums[1] in range(nums[0], nums[3]) and abs(nums[1] - nums[3]) in range(1,4):
					removed_ind = 2
					check_increase = nums[3] > nums[0]
				else:
					failed = True
		else:
			check_increase = nums[2] > nums[0]
	last_num = nums[1]
	if removed_ind == 1:
		last_num = nums[0]
	if not failed:
		for i in range(2 if removed_ind < 2 else 3, len(nums)):
			curr_num = nums[i]
			violation_found = check_failed(curr_num, last_num, check_increase)
			if violation_found:
				if removed_ind < 0:
					if i < len(nums) - 1:
						# remove curr, use grace
						violation_found = check_failed(nums[i+1], nums[i-1], check_increase)
						if not violation_found:
							removed_ind = i
						else:
							failed = True
							break
					else:
						removed_ind = i
				else:
					failed = True
					break
			if removed_ind == i:
				last_num = nums[i-1]
			else:
				last_num = curr_num
	if not failed:
		safe += 1

end = time.time()
print(safe)
print(end - start)