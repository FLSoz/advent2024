from collections import defaultdict

with open("puzzle1_input.txt", "r") as f:
	lines = f.readlines()

list1 = []
list2 = []
right_count = defaultdict(lambda: 0)

for line in lines:
	nums = line.strip().split("   ")
	list1.append(int(nums[0]))
	right_num = int(nums[1])
	list2.append(right_num)
	right_count[right_num] += 1

acc = 0

for num in list1:
	acc += num * right_count[num]

print(acc)