cities = ["TelAviv", "Haifa", "Barcelona", "Rome"]
temp_long = 0
temp_long_city = ""
for city in cities:
    l = len(city)
    print(l)
    if l > temp_long:
        temp_long = l
        temp_long_city = city
print(f"{temp_long_city} is the longer city name from the list")

