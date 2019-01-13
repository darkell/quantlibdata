from unittest import TestCase
import QuantLib as ql
from utils import *


class TestCalendar(TestCase):
    def setUp(self):
        self.calendars = [ql.Australia(), ql.UnitedStates(0), ql.TARGET()]
        self.start = ql.Date(1, 1, 1990)
        self.end = ql.Date(1, 1, 2011)
        self.timeUnits = [ql.Days, ql.Weeks, ql.Months, ql.Years]
        self.businessDayConventions = [0, 1, 2, 3, 4, 5, 6]

    def test_isHoliday(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                results.append(
                    {
                        "calendar": t_to_calendar(calendar),
                        "date": t_date_to_string(date),
                        "expected": calendar.isHoliday(date)
                    }
                )

                date = date.__add__(1)

        t_write_results("Calendar_isHoliday.json", results)

    def test_isWeekend(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(ql.Date(31, 1, 1990)):

                results.append(
                    {
                        "calendar": t_to_calendar(calendar),
                        "date": t_date_to_string(date),
                        "expected": calendar.isWeekend(date.weekday())
                    }
                )

                date = date.__add__(1)

        t_write_results("Calendar_isWeekend.json", results)

    def test_isBusinessDay(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                results.append(
                    {
                        "calendar": t_to_calendar(calendar),
                        "date": t_date_to_string(date),
                        "expected": calendar.isBusinessDay(date)
                    }
                )

                date = date.__add__(1)

        t_write_results("Calendar_isBusinessDay.json", results)

    def test_isEndOfMonth(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                results.append(
                    {
                        "calendar": t_to_calendar(calendar),
                        "date": t_date_to_string(date),
                        "expected": calendar.isEndOfMonth(date)
                    }
                )

                date = date.__add__(1)

        t_write_results("Calendar_isEndOfMonth.json", results)

    def test_endOfMonth(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                results.append(
                    {
                        "calendar": t_to_calendar(calendar),
                        "date": t_date_to_string(date),
                        "expected": t_date_to_string(calendar.endOfMonth(date))
                    }
                )

                date = date.__add__(1)

        t_write_results("Calendar_endOfMonth.json", results)

    def test_adjust(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                for businessDayConvention in self.businessDayConventions:

                    results.append(
                        {
                            "calendar": t_to_calendar(calendar),
                            "date": t_date_to_string(date),
                            "businessDayConvention": t_to_businessDayConvention(businessDayConvention),
                            "expected": t_date_to_string(calendar.adjust(date, businessDayConvention))
                        }
                    )

                date = date.__add__(1)

        t_write_results("Calendar_adjust.json", results)

    def test_adjust(self):
        results = []

        for calendar in self.calendars:
            date = self.start

            while date.__lt__(self.end):

                for businessDayConvention in self.businessDayConventions:

                    results.append(
                        {
                            "calendar": t_to_calendar(calendar),
                            "date": t_date_to_string(date),
                            "businessDayConvention": t_to_businessDayConvention(businessDayConvention),
                            "expected": t_date_to_string(calendar.adjust(date, businessDayConvention))
                        }
                    )

                date = date.__add__(1)

        t_write_results("Calendar_adjust.json", results)

    def test_advance(self):
        results = []

        calendar = self.calendars[0]
        date = self.start

        while date.__lt__(self.start.__add__(60)):
            for amount in range(-60, 60):
                for time_unit in self.timeUnits:
                    for c in self.businessDayConventions:
                        for end_of_month in [True, False]:
                            results.append(
                                {
                                    "calendar": t_to_calendar(calendar),
                                    "date": t_date_to_string(date),
                                    "n": amount,
                                    "unit": t_time_unit(time_unit),
                                    "businessDayConvention": t_to_businessDayConvention(c),
                                    "endOfMonth": end_of_month,
                                    "expected": t_date_to_string(calendar.advance(date, amount, time_unit, c, end_of_month))
                                }
                            )

            date = date.__add__(1)

        t_write_results("Calendar_advance.json", results)

    def test_businessDaysBetween(self):
        results = []

        calendar = self.calendars[0]
        for start_diff in range(-50, 50):
            for end_diff in range(-50, 50):
                date_from = self.start.__add__(start_diff)
                date_to = self.start.__add__(end_diff)

                for include_first in [False, True]:
                    for include_last in [False, True]:

                        results.append(
                            {
                                "calendar": t_to_calendar(calendar),
                                "from": t_date_to_string(date_from),
                                "to": t_date_to_string(date_to),
                                "includeFirst": include_first,
                                "includeLast": include_last,
                                "expected": calendar.businessDaysBetween(date_from, date_to, include_first, include_last)
                            }
                        )

        t_write_results("Calendar_businessDaysBetween.json", results)

