import csv

def write_data_to_csv(month, projected_income):
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([month, projected_income])
