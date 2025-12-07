def calc_multiple(num1, num2, num3=1):
    print(f"this function calculate num1 multiple by num2 and num3")
    if num1 > 0 and num2 > 0:
        result = num1 * num2 * num3
    print(f"the value of num1 multiple by num2 and num3 is: {result}")
    return result

var1 = 4
var2 = 5
calc_multiple(var1, var2, 8)
# example of define a default value (the default value is num3=1, but when we call the function and enter a different number, num3 will change to the new number)


def check_price(price):
    if price >= 0 and price <= 100:
        print(f"price {price} is between 0 and 100")
    elif price >= 100 and price <= 1000:
        add1=price+20
        print(f"price {price} is between 100 and 1000, new price is {add1}")
    elif price >= 1000:
        add2=price+50
        print(f"price {price} is higher than 1000, new price is {add2}")
    else:
        print(f"{price} is invalid price")
    return price

check_price(-2)
new_price = check_price(99)  # example of using the value that is returned to the function check_price
if new_price % 2 == 0:
    print(f"price {new_price} is even")
else:
    print(f"price {new_price} is odd")
check_price(138)
check_price(1003)





