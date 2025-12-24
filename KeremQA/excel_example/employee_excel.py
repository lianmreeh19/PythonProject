import csv

data = [{'full name': 'Nikhil', 'ID': 1000, 'year': 2010, 'salary': 10000},
        {'full name': 'Sanchit', 'ID': 1001, 'year': 2010, 'salary': 8700}
    , {'full name': 'Aditya', 'ID': 1002, 'year': 2011, 'salary': 20600}
    , {'full name': 'Sagar', 'ID': 1003, 'year': 2012, 'salary': 8300}
    , {'full name': 'Prateek', 'ID': 1004, 'year': 2014, 'salary': 9450}
    , {'full name': 'Sahil', 'ID': 1005, 'year': 2025, 'salary': 7500}
    , {'full name': 'Lian', 'ID': 1006, 'year': 2013, 'salary': 30900}
    , {'full name': 'Liraz', 'ID': 1007, 'year': 2022, 'salary': 120000}
    , {'full name': 'Noor', 'ID': 1008, 'year': 2018, 'salary': 15000}
    , {'full name': 'Rawan', 'ID': 1009, 'year': 2020, 'salary': 7900}]

field_names = ['full name', 'ID', 'year', 'salary']

with open('employees_salaries.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)