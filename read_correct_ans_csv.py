import csv


def read_csv():
    with open('csv_file_kamran.csv', 'r') as csvfile:
        # readCSV = csv.reader(csvfile, delimiter=',')
        data = list(csv.reader(csvfile))
        return data

