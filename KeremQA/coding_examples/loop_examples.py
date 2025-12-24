for i in range(4):
    print (i)


num = 3
for i in range (1, 11):
    print(num*i)
    summery = num*i
    if summery % 2 == 0:
        print(f"the number {summery} is even")
    else:
        print(f"the number {summery} is odd")


num_1 = 19
num_2 = 3
sum = num_1 + num_2
if sum % 2 == 0:
    print(f"the sum {sum} is even")
else:
    print(f"the sum {sum} is odd")