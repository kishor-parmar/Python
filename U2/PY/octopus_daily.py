import csv

peak_rate = 0.2978
offpeak_rate = 0.075
standing_charge = 0.4866
daily_peak_units = 0
daily_offpeak_units = 0
first_time = True

try:
    infile = open("/Users/kishor/Downloads/consumption.csv", encoding="utf8")

    # Write the rows data to the CSV file with quotes around each field
    outfile = open("/Users/kishor/Downloads/Daily.csv", "w", newline="")
    csvwriter = csv.writer(outfile, csv.QUOTE_NONNUMERIC)
    fields = [
        "Date",
        "Peak Units",
        "Peak Amount",
        "Off Peak Units",
        "Off Peak Amount",
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

        if first_time:
            last_date = start_date
            first_time = False

        if start_time == "00:00:00":
            offpeak = True
            peak = False

        if start_time == "05:30:00":
            offpeak = False
            peak = True

        if start_time == "23:30:00":
            offpeak = True
            peak = False

        if start_date == last_date:
            if peak:
                daily_peak_units += float(units)
            else:
                daily_offpeak_units += float(units)
        else:
            peak_amount = daily_peak_units * peak_rate
            offpeak_amount = daily_offpeak_units * offpeak_rate
            daily_total = peak_amount + offpeak_amount + standing_charge

            row = [
                last_date,
                daily_peak_units,
                peak_amount,
                daily_offpeak_units,
                offpeak_amount,
                standing_charge,
                daily_total,
            ]
            csvwriter.writerow(row)

            print(
                f"{last_date}, {daily_peak_units}, {peak_amount}, {daily_offpeak_units}, {offpeak_amount}, {standing_charge}, {daily_total}"
            )
            last_date = start_date
            daily_peak_units = 0
            daily_offpeak_units = float(units)

    peak_amount = daily_peak_units * peak_rate
    offpeak_amount = daily_offpeak_units * offpeak_rate
    daily_total = peak_amount + offpeak_amount + standing_charge

    row = [
        last_date,
        daily_peak_units,
        peak_amount,
        daily_offpeak_units,
        offpeak_amount,
        standing_charge,
        daily_total,
    ]

    csvwriter.writerow(row)
    print(row)
    print(
        f"{last_date}, {daily_peak_units}, {peak_amount}, {daily_offpeak_units}, {offpeak_amount}, {standing_charge}, {daily_total}"
    )

    infile.close()
    outfile.close()

except Exception as e:
    print(e)
