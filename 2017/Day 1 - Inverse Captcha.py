# Part 1

nums = []

with open('2017/data/day1.txt') as file:
    for line in file:
        nums += list(line.strip())

nums = [int(x) for x in nums]
sum = 0

for i in range(len(nums) - 1):
    opposite = int((i + len(nums) / 2) % len(nums))
    if nums[i] == nums[opposite]:
        sum += nums[i]

print(sum)