with open("puzzle1_input.txt", "r") as f:
	lines = f.readlines()

list1 = []
list2 = []

for line in lines:
	nums = line.strip().split("   ")
	list1.append(int(nums[0]))
	list2.append(int(nums[1]))

list1.sort()
list2.sort()

acc = 0

for i in range(len(list1)):
	acc += abs(list1[i] - list2[i])

print(acc)