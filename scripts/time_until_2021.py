"""
Computes how much time is left until 2020 is over
"""

import argparse
import datetime

from convertime import constants, conversions


def convert(diff, units="days"):
    # convert to whatever format is needed
    if units == "days":
        return diff.days

    if units == "hours":
        time_left = diff.days * constants.HOURS_IN_DAY
    elif units == "seconds":
        time_left = conversions.days_to_seconds(diff.days) + diff.seconds
    elif units == "weeks":
        time_left = conversions.hours_to_weeks(diff.days * constants.HOURS_IN_DAY)
    else:
        raise ValueError(
            "Sorry, we can only convert to 'seconds', 'days', 'hours' or 'weeks' at this time"
        )
    return time_left


def main():
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--units", type=str, default="seconds", help="units for time remaining"
    )
    ARGS, _ = parser.parse_known_args()

    # compute days left to 2021
    now = datetime.datetime.now()
    first_day_of_2021 = datetime.datetime(2021, 1, 1, 0, 0, 0)
    diff = first_day_of_2021 - now

    time_left = convert(diff, ARGS.units)

    # print time left
    print(f"There are {time_left:.2f} {ARGS.units} left in 2020!")


if __name__ == "__main__":
    main()
