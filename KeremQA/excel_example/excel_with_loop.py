import csv

filename = 'employees_salaries2.csv'
field_names = ['Full name', 'ID', 'Year', 'Salary']

data = [
    {field_names[0]: 'John Due', field_names[1]: 0, field_names[2]: 2010, field_names[3]: 10000},
    {field_names[0]: 'Lian Mreeh', field_names[1]: 0, field_names[2]: 2019, field_names[3]: 190000},
    {field_names[0]: 'Liraz Daxa', field_names[1]: 0, field_names[2]: 2025, field_names[3]: 200000},
    {field_names[0]: 'Tagreed Mreeh', field_names[1]: 0, field_names[2]: 2016, field_names[3]: 20000}
]

counter = 0
max_id = 1000 + len(data)
for i in range(1000, max_id):
    data[counter][field_names[1]] = i
    counter += 1

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

