import csv

peak_rate = 0.2978
offpeak_rate = 0.075
standing_charge = 0.4866
daily_total = 0

try:
    infile = open("/Users/kishor/Downloads/consumption.csv", encoding="utf8")
    csv_reader = csv.reader(infile)
    for line in csv_reader:
        units = line[0]
        start = line[1][0:20]
        end = line[2][0:20]
        start_date = start[0:11]
        start_time = start[12:21]
        end_time = end[12:21]

        if start_time == "":
            last_date = "2024-01-01"
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

        if peak:
            daily_total += float(peak_rate) * float(units)
        else:
            daily_total += float(offpeak_rate) * float(units)

        if start_date != last_date:
            print(f"{start_date} = {daily_total}")
            last_date = start_date
            daily_total = 0

        #        print(line)
        #        print(
        #            f"Units = {units}, Date = {start_date}, Start Time = {start_time}, End Time = {end_time}, Period = {peak}"
        #        )
        infile.close

    print(f"{start_date} = {daily_total}")

except Exception as e:
    print(e)
