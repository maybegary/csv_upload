import csv

def handle_uploaded_file(f):
    with open('data_set.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def data_cleaner_by_column(data_file):
    with open('data_set.csv', 'r', newline='') as csv_reader:
        reader = csv.DictReader(csv_reader)
        