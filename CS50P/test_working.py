import unittest
from practice import convert


class test_convert(unittest.TestCase):
    def test_time_format(self):
        self.assertTrue(convert("9 AM to 5 PM"))
        self.assertTrue(convert("9:00 AM to 5:00 PM"))
        self.assertTrue(convert("8 PM to 8 AM"))
        self.assertTrue(convert("8:00 PM to 8:00 AM"))
        self.assertTrue(convert("12 AM to 12 PM"))
        self.assertTrue(convert("12:00 AM to 12:00 PM"))


def test_time_format_invalid():
    try:
        convert("8:60 AM to 4:60 PM")
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError:
        pass

    try:
        convert("9AM to 5PM")
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError:
        pass

    try:
        convert("09:00 to 17:00")
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError:
        pass

    try:
        convert("9 AM - 5 PM")
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError:
        pass

    try:
        convert("10:7 AM - 5:1 PM")
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError:
        pass


