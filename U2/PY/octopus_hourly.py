import csv


def print_row(start_date, start_time, end_time, units, rate, amount):
    row = [
        start_date,
        start_time,
        end_time,
        units,
        rate,
        amount,
    ]

    csvwriter.writerow(row)

    return


def print_totals(start_date, daily_total, STANDING_CHARGE):
    row = [
        start_date,
        "",
        "",
        "",
        "",
        "",
        daily_total,
        STANDING_CHARGE,
        STANDING_CHARGE + daily_total,
    ]

    csvwriter.writerow(row)

    return


PEAK_RATE = 0.2978
OFFPEAK_RATE = 0.075
STANDING_CHARGE = 0.4866

daily_total = 0
first_time = True


try:
    infile = open("/Users/kishor/Downloads/consumption.csv", "r", encoding="utf8")

    # Write the rows data to the CSV file with quotes around each field
    outfile = open("/Users/kishor/Downloads/Hourly.csv", "w", newline="")
    csvwriter = csv.writer(outfile, csv.QUOTE_NONNUMERIC)
    fields = [
        "Date",
        "Start time",
        "End time",
        "Units",
        "Rate",
        "Amount",
        "Daily Amount",
        "Standing Charge",
        "Daily Total",
    ]
    csvwriter.writerow(fields)

    csv_reader = csv.reader(infile)
    for line in csv_reader:
        units = line[0]
        start = line[1][0:20]
        end = line[2][0:20]
        start_date = start[0:11]
        start_time = start[12:21]
        end_time = end[12:21]

        if start_time == "":
            continue

        if not (first_time) and start_time == "00:00:00":
            offpeak = True
            peak = False

            print_totals(last_date, daily_total, STANDING_CHARGE)
            daily_total = 0
            last_date = start_date

        if first_time and start_time == "00:00:00":
            offpeak = True
            peak = False
            first_time = False
            last_date = start_date

        if start_time == "05:30:00":
            offpeak = False
            peak = True

        if start_time == "23:30:00":
            offpeak = True
            peak = False

        if peak:
            rate = PEAK_RATE
        else:
            rate = OFFPEAK_RATE

        amount = rate * float(units)

        print_row(start_date, start_time, end_time, units, rate, amount)

        daily_total += amount

    print_totals(start_date, daily_total, STANDING_CHARGE)

    infile.close()
    outfile.close()

except Exception as e:
    print(e)
