
import csv
"""

считываем данные из файла csv, по умолчанию row в файле делятся запятой. Работает с любым количеством значений
"""

def load_test_data(file_path):
    with open(file_path, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        test_data = []
        for row in file_data:
            test_data.append(row)
    return test_data