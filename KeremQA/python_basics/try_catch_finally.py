# block to sample:
try:
    a = 10
    b = 5
    num1 = 20
    num2 = a - b
    summery = num1/num2

# what I'm looking for:
# examples of except:
# example 1: except NoSuchElementException:
# example 2: except Exception as e:

# what I'm looking for:
except ZeroDivisionError:
    print ("Division by zero event found ")
    num2 =1
    summery = num1/num2

# will be done anyway:
finally:
    summery = summery + 5

print (summery)