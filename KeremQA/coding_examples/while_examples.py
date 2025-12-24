count = 0
num = 10
i = 3
is_divide = True
while is_divide == True:
    # handling case of infinity by increase the count to 100
    count += 1
    print(f"count value is {count}")
    if count == 100:
        break
    i+=1
    result = num % i
    if (result == 0):
        is_divide = False
        print(f"the result of dividing {num} in {i} is {result}")
