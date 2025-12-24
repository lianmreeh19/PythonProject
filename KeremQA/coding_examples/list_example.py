nums = [3,5,6,3,6,7,12,11]
# list commands:
# l = len(nums)
# nums.append(2)
# nums.index(6)
# nums[2]
# nums_update = nums[2:4]

for num in nums:
    new_num = num+2
    print (new_num)

even_numbers = []
for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
        even_numbers.append(num)
        print(f"even numbers: {even_numbers}")
    else:
        print(f"{num} is odd")

sum = 0
for num in nums:
    sum = num+sum
    print(f"sum: {sum}")
print(sum)