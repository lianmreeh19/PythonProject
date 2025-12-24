import csv

filename = 'excel_get_and_read.csv'
field_names = ['Year', 'avg_grade']

data = [
    {field_names[0]: 0, field_names[1]: 98},
    {field_names[0]: 0, field_names[1]: 81},
    {field_names[0]: 0, field_names[1]: 90},
    {field_names[0]: 0, field_names[1]: 100},
    {field_names[0]: 0, field_names[1]: 75}
]

counter = 0
max_year = 2000 + len(data)
for year in range(2000, max_year):
    data[counter][field_names[0]] = year
    counter += 1

with open(filename, 'w', newline='') as file_to_write:
    writer = csv.DictWriter(file_to_write, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

with open(filename, mode='r', newline='', encoding='utf-8') as file_to_read:
    csv_reader = csv.reader(file_to_read)

    print("--- Reading All Rows ---")
    index = 0
    for row in csv_reader:
        if row[1] == '90':
            print(f"avg {row[1]} found in the {index} row")
            year = row[0]
            print(f"year: {year}")
        index += 1

