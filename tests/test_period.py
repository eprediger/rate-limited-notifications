import unittest

from app.domain.period import Period


class TestPeriod(unittest.TestCase):
    def test_valid_period_should_return_seconds(self):
        for (period_name, expected_seconds) in [
            ("SECONDS", 1),
            ("MINUTES", 60),
            ("HOURS", 3600),
            ("DAYS", 86400),
            ("WEEKS", 604800)
        ]:
            with self.subTest():
                period = Period(period_name)
                self.assertEqual(period.to_seconds().total_seconds(), expected_seconds)

    def test_invalid_period_should_raise_exception(self):
        with self.assertRaises(ValueError):
            Period("INVALID_PERIOD")
