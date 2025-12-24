for i in range(10):
    result = i*i
    print(result)
    if result > 50:
        print (f"{i} is the first squared number that it's result is above 50")
        break