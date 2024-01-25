import csv

global PEAK_RATE
global OFFPEAK_RATE
global STANDING_CHARGE
global FILE_PATH
global INFILE_NAME
global OUTFILE_NAME

PEAK_RATE = 0.2978
OFFPEAK_RATE = 0.075
STANDING_CHARGE = 0.4866

FILE_PATH = "/Users/kishor/Downloads/"
INFILE_NAME = "consumption.csv"
OUTFILE_NAME = "Daily.csv"


def open_infile():
    infile = open(FILE_PATH + INFILE_NAME, "r", encoding="utf8")

    return infile


def open_outfile():
    outfile = open(FILE_PATH + OUTFILE_NAME, "w", newline="")

    return outfile


def print_header(csvwriter):
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

    return


def print_row(
    csvwriter,
    last_date,
    daily_peak_units,
    peak_amount,
    daily_offpeak_units,
    offpeak_amount,
    STANDING_CHARGE,
    daily_total,
):
    row = [
        last_date,
        daily_peak_units,
        peak_amount,
        daily_offpeak_units,
        offpeak_amount,
        STANDING_CHARGE,
        daily_total,
    ]

    csvwriter.writerow(row)

    return


def get_peak_amount(daily_peak_units):
    x = daily_peak_units * PEAK_RATE

    return x


def get_offpeak_amount(daily_offpeak_units):
    x = daily_offpeak_units * OFFPEAK_RATE

    return x


def get_daily_total(peak_amount, offpeak_amount):
    x = peak_amount + offpeak_amount + STANDING_CHARGE

    return x


def main():
    daily_peak_units = 0
    daily_offpeak_units = 0
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
                peak_amount = get_peak_amount(daily_peak_units)
                offpeak_amount = get_offpeak_amount(daily_offpeak_units)
                daily_total = get_daily_total(peak_amount, offpeak_amount)

                print_row(
                    csvwriter,
                    last_date,
                    daily_peak_units,
                    peak_amount,
                    daily_offpeak_units,
                    offpeak_amount,
                    STANDING_CHARGE,
                    daily_total,
                )

                last_date = start_date
                if peak:
                    daily_peak_units = float(units)
                    daily_offpeak_units = 0
                else:
                    daily_peak_units = 0
                    daily_offpeak_units = float(units)

            peak_amount = get_peak_amount(daily_peak_units)
            offpeak_amount = get_offpeak_amount(daily_offpeak_units)
            daily_total = get_daily_total(peak_amount, offpeak_amount)

        print_row(
            csvwriter,
            last_date,
            daily_peak_units,
            peak_amount,
            daily_offpeak_units,
            offpeak_amount,
            STANDING_CHARGE,
            daily_total,
        )

        infile.close()
        outfile.close()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
