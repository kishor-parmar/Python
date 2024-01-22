import csv

peak_rate = 29.78
offpeak_rate = 7.5
standing_charge = 48.66

try:
    f = open("/Users/kishor/Downloads/consumption.csv", encoding="utf8")
    csv_reader = csv.reader(f)
    for line in csv_reader:
        units = line[0]
        start = line[1][0:20]
        end = line[2][0:20]
        start_date = start[0:11]
        start_time = start[12:21]
        end_time = end[12:21]

        if start_time == "":
            continue

        if start_time == "00:00:00":
            offpeak = True
            peak = False

        if start_time == "05:30:00":
            offpeak = False
            peak = True

        if start_time == "23:30:00":
            offpeak = True
            peak = False

        print(line)
        print(
            f"Units = {units}, Date = {start_date}, Start Time = {start_time}, End Time = {end_time}"
        )

except:
    print("Cannot open consumption.csv in the Downloads Directory")
finally:
    f.close
