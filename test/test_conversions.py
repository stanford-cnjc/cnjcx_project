import unittest
import convertime.conversions as conversions


class TestConversions(unittest.TestCase):
    def test_hours_to_seconds(self):
        seconds_in_one_hour = conversions.hours_to_seconds(1.0)
        self.assertEqual(seconds_in_one_hour, 3600)

    def test_days_to_seconds(self):
        seconds_in_two_days = conversions.days_to_seconds(2.0)
        self.assertEqual(seconds_in_two_days, 172800)

    def test_hours_to_weeks(self):
        weeks_in_336_hours = conversions.hours_to_weeks(336)
        self.assertEqual(weeks_in_336_hours, 2)


if __name__ == "__main__":
    unittest.main()
