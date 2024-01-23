import csv

try:
    file = open("/Users/kishor/Downloads/Daily.csv", "w", newline="")
    writer = csv.writer(file)
    field = ["name", "age", "country"]

    writer.writerow(field)
    writer.writerow(["Kishor Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])
except Exception as e:
    print(e)
