from unittest import TestCase
import QuantLib as ql
from utils import *


class TestDayCounter(TestCase):
    def setUp(self):
        self.day_counters = [ql.Actual365Fixed(), ql.ActualActual(2), ql.ActualActual(5), ql.Thirty360(0),
                             ql.Thirty360(2), ql.Thirty360(4)]
        self.starts = [ql.Date(1, 1, 2004), ql.Date(1, 2, 2004), ql.Date(28, 2, 2004), ql.Date(29, 2, 2004),
                       ql.Date(15, 8, 2004), ql.Date(31, 12, 2004), ql.Date(1, 1, 2005), ql.Date(28, 2, 2005)]

    def test_dayCount(self):
        results = []

        for day_counter in self.day_counters:
            for start in self.starts:

                for j in range(-350, 350):
                    end = start.__add__(j)

                    day_count = day_counter.dayCount(start, end)

                    results.append(
                        {
                            "dayCounter": t_to_day_counter(day_counter),
                            "start": t_date_to_string(start),
                            "end": t_date_to_string(end),
                            "expected": day_count
                        }
                    )

        t_write_results("DayCounter_dayCount.json", results)

    def test_yearFraction(self):
        results = []

        for day_counter in self.day_counters:
            for start in self.starts:

                for j in range(-350, 350):
                    end = start.__add__(j)

                    day_count = day_counter.yearFraction(start, end)

                    results.append(
                        {
                            "dayCounter": t_to_day_counter(day_counter),
                            "start": t_date_to_string(start),
                            "end": t_date_to_string(end),
                            "expected": day_count
                        }
                    )

        t_write_results("DayCounter_yearFraction.json", results)
