import csv

data_to_write = [
    ['name', 'age', 'percentage'],
    ['Arun', 24, 80],
    ['Bala', 39, 36],
    ['Ceril', 49, 88],
    ['Dineesh', 14, 92],
    ['prakash', 27, 43]
]
# write a csv file
def write_csv_file(data, filename):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)






