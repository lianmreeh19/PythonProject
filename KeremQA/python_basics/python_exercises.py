# sum = 0
# for i in range (1000,5001,4):
#     if i%3 == 0:
#         sum += i
# print(f"sum is {sum}")


# shtroudel_count = 0
# mail = input("Enter your mail address: ")
# end_mail = mail[len(mail)-4 : len(mail)]
# for i in mail:
#     if i == "@":
#         shtroudel_count += 1
#
# if shtroudel_count == 1 and end_mail == ".com":
#     print("valid email")
# else:
#     print("invalid email")

# for i in range (11):
#     for j in range (11):
#        multiple_table =  i * j
#        print(multiple_table)

# for i in range (100,501):
#     if i == 373:
#         break
#     print(i)

# for i in range (10, 78):
#     if i == 32 or i == 50 or i == 70:
#         continue
#     print(i)

# num_range = int(input("Enter a range: "))
# sum = 1
# for i in range(1, num_range + 1):
#     print(f"{i}*{sum}=", end= " ")
#     sum *= i
#     print(f"{sum}")

# num_range = int(input("Enter a range: "))
# num1 = 1
# num2 = 1
# for i in range(num_range):
#     num1 = num2-num1
#     num2 = num1 + num2
#     print(num2)

# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
# calc1 = b * b - 4 * a * c
# if calc1 > 0:
#     sqrt_sum = math.sqrt(calc1)
# else:
#     print("illegal input")
# calc2 = -b + calc1 / (2 * a)
# calc3 = -b - calc1 / (2 * a)
# print(f"the answers is: {calc2}, {calc3}")

# prices = input("enter price or 'stop' for exit: ")
# sum = 0
# while prices.lower() != "stop":
#     sum += float(prices)
#     prices = input("enter price: ")
# print(f"sum of shopping is {sum}")
# print(f"average of shopping is {sum/len(prices)}")

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# sum = 1
# for i in range(num2):
#     sum *= num1
# print(f"answer is {sum}")

# num = input("Enter a number: ")
# for i in range (2, num):
#     if num % i == 0:
#         break
#         print("the number is valid")

# ls = [19,3,0,7]
# count = 0
# for i in ls:
#     count += 1
# print(count)

# ls = [23,11,4,16,55]
# for i in ls:
#     if i % 2 == 0:
#         print(i)

# ls = [30,5,43,100,3]
# count = 0
# for i in ls:
#     if i > 10:
#         count += 1
# print(count)
    
# ls = [30,5,43,100,3]
# count = 0
# for i in ls:
#     count += i
# avg = count / len(ls)
# print(avg)

# ls = [-2, 6, 7, -20, -46]
# new_ls = []
# for i in ls:
#     if i >= 0:
#         new_ls.append(i)
# print(new_ls)

# ls = [-2, 6, 7, -20, -46]
# max_num = 0
# for num in ls:
#     if num > max_num:
#         max_num = num
# print(max_num)

# ls = [-2, 6, 7, -20, -46, 1, 2, 3]
# help_ls = []
# final_ls = []
# counter = 0
# for i in ls:
#     counter += 1
#     if i > 0:
#         help_ls.append(i)
#     elif i < 0 and len(help_ls) > 0:
#         final_ls.append(help_ls)
#         help_ls = []
#     if counter == len(ls) - 1:
#         final_ls.append(help_ls)
# longer_substring = 0
# for i in final_ls:
#     if len(i) > longer_substring:
#         last_ls = i
# print(last_ls)
# sum = 0
# for i in last_ls:
#     sum += i
# print(sum)

# ls = [15,22,-9,39,-45]
# for i in ls:
#     if i < 0:
#         location = ls.index(i)
#         del ls[location]
# print(ls)

# ls = [2,3,1,1,1,13,4,4,4,4]
# max_length = 0
# local_max = 1
# for i in range(len(ls) - 1):
#     if ls[i] == ls[i + 1]:
#         local_max += 1
#     elif local_max > max_length:
#         max_length = local_max
#         local_max = 1
# print(max_length)

# grades = []
# max_grade = 0
# min_grade = 100
# sum_grades = 0
# len_grades_between_70_and_90 = 0
# for i in range(10):
#     grade = int(input("please enter a grade: "))
#     grades.append(grade)
# for grade in grades:
#     if grade > max_grade:
#         max_grade = grade
# print (f"max grade is: {max_grade}")
# for grade in grades:
#     if grade < min_grade:
#         min_grade = grade
# print(f"min grade is: {min_grade}")
# for grade in grades:
#     sum_grades += grade
#     avg = sum_grades / len(grades)
# print(f"avg grade is: {avg}")
# for grade in grades:
#     if 70<grade<90:
#         len_grades_between_70_and_90 += 1
# print(f"amount grades between 70 and 90 is: {len_grades_between_70_and_90}")

# student = {
#     "name": "moshe",
#     "course": "AI",
#     "grades": [95, 43, 100, 32, 98, 99]
# }
# max = 0
# # grades_ls = student["grades"]
# for value in student["grades"]:
#     if value > max:
#         max = value
# print(f"max grade is:{max}")

# ls = [4,7,19,19,3]
# new_ls = []
# for i in ls:
#     if i not in new_ls:
#         new_ls.append(i)
# print(new_ls)

# ls = [13, 5, 3,12]
# multiple = 1
# for i in ls:
#     multiple *= i
# print(multiple)

# student = {"id":1, "age":18, "name":"lian", "grades":[90,98,100,87]}
# for x in student.keys():
#     print(x)
# for x in student.values():
#     print(x)

# students =[{"id":1, "age":18, "name":"lian", "grades":[90,98,100,87]},
#            {"id":2, "age":18, "name":"liraz", "grades":[77,83,99,86]}]
# max_grade = 0
# sum_grade = 0
# for student in students:
#     for grade in student["grades"]:
#         if grade > max_grade:
#             max_grade = grade
#     print(max_grade)
#     max_grade = 0
# for student in students:
#     for grade in student["grades"]:
#        sum_grade += grade
#        avg = sum_grade / len(student["grades"])
#     print(avg)
#     sum_grade = 0
# for student in students:
#     print(len(student["name"]))

# students =[{"id":1, "age":18, "name":"lian", "grades":[90,98,100,87]},
#            {"id":2, "age":18, "name":"liraz", "grades":[77,83,99,86]},
#            {"id":3, "age":18, "name":"noor", "grades":[77,80,99,90]},
#            {"id":4, "age":18, "name":"natal", "grades":[70,96,99,88]},
#            {"id":5, "age":18, "name":"rawan", "grades":[66,83,94,86]}]
#
# sum_grade = 0
# sum_avg_grades = 0
# for student in students:
#     for grade in student["grades"]:
#         sum_grade += grade
#     avg_grade = sum_grade / len(student["grades"])
#     sum_avg_grades += avg_grade
#     sum_grade = 0
# avg_all_grades = sum_avg_grades / len(students)
# print(avg_all_grades)
# longer_name = 0
# for student in students:
#     if len(student["name"]) > longer_name:
#         longer_name = len(student["name"])
# print(f"longer name is: {student['name']}")

names = ["lian", "lora", "yaqeen","jezail"]
longer_name = names[0]
shortest_name = names[0]
for name in names:
    if len(name) > len(longer_name):
        longer_name = name
    elif len(name) < len(shortest_name):
        shortest_name = name
print(longer_name)
print(shortest_name)





