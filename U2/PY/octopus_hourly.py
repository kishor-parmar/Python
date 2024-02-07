import csv
from io import TextIOWrapper

from octopus_const import *


def open_infile() -> TextIOWrapper:
    infile = open(FILE_PATH + INFILE_NAME, "r", encoding="utf8")

    return infile


def open_outfile() -> TextIOWrapper:
    outfile = open(FILE_PATH + HOURLY_NAME, "w", newline="")

    return outfile


def print_header(csvwriter) -> None:
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

    return


def print_row(csvwriter, start_date, start_time, end_time, units, rate, amount) -> None:
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


def print_totals(csvwriter, start_date, daily_total, STANDING_CHARGE) -> None:
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


def main():
    daily_total = 0
    first_time = True

    try:
        infile = open_infile()
        outfile = open_outfile()

        csvwriter = csv.writer(outfile, csv.QUOTE_NONNUMERIC)

        print_header(csvwriter)

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

                print_totals(csvwriter, last_date, daily_total, STANDING_CHARGE)
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

            print_row(csvwriter, start_date, start_time, end_time, units, rate, amount)

            daily_total += amount

        print_totals(csvwriter, start_date, daily_total, STANDING_CHARGE)

        infile.close()
        outfile.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
