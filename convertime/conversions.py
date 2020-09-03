from convertime import constants


def hours_to_seconds(hours):
    """Computes the number of seconds in the number of hours provided"""
    return hours * constants.MINUTES_IN_HOUR * constants.SECONDS_IN_MINUTE


def days_to_seconds(days):
    """Computes the number of seconds in the number of days provided"""
    hours = days * constants.HOURS_IN_DAY
    return hours_to_seconds(hours)


def hours_to_weeks(hours):
    """Computes the number of weeks in the number of hours given"""
    days = hours / constants.HOURS_IN_DAY
    return days / constants.DAYS_IN_WEEK


if __name__ == "__main__":
    print(
        f"If you were curious, there are {hours_to_seconds(4.2)} seconds in 4.2 hours"
    )
