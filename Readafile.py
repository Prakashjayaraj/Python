import csv
def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

data_from_csv = read_csv_file("Student.csv")
for row in data_from_csv:
    print(row)