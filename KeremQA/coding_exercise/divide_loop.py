for i in range (51):
    if i % 15 == 0:
        print(f"{i} divided by 15")
    elif i % 5 == 0:
        print(f"{i} divided by 5")
    elif i % 3 == 0:
        print(f"{i} divided by 3")
    else:
        print(f"{i} didn't divided by any number")