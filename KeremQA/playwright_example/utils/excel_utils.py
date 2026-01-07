import csv

class excelUtils:
    def get_excel_column_data(self, row_number, file_name):
        data = []
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for column in reader:
                data.append(column[row_number])
        return data

    def set_excel_data(self, data, file_name):
        field_names = ['ID', 'Price']
        data_to_excel = [
            {field_names[0]: 'price1', field_names[1]: data[0]},
            {field_names[0]: 'price2', field_names[1]: data[1]},
            {field_names[0]: 'price3', field_names[1]: data[2]},
            {field_names[0]: 'price4', field_names[1]: data[3]},
            {field_names[0]: 'price5', field_names[1]: data[4]},
            {field_names[0]: 'price6', field_names[1]: data[5]},
        ]
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data_to_excel)