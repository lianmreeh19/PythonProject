date = "28-Nov-2025"
index_1 = date.index("-")
day = date[:index_1]
index_2 = len(date)-5
month = date[index_1+1:index_2]
final_date = f"{month}-{day}-2025"
print(final_date)

