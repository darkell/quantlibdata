from unittest import TestCase
import QuantLib as ql
from utils import *


class TestFlatForward(TestCase):
    def setUp(self):
        self.settlement_date = ql.Date(17, 5, 1998)
        self.dividend_yields = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11]
        self.day_counter = ql.Actual365Fixed()
        self.compoundings = [ql.Compounded, ql.Simple, ql.Continuous, ql.SimpleThenCompounded]
        self.frequencies = [ql.Daily, ql.Annual]

    def test_discount_date(self):
        dates = [ql.Date(17, 6, 1998), ql.Date(17, 7, 1998), ql.Date(17, 8, 1998),
                 ql.Date(17, 9, 1998), ql.Date(17, 10, 1998), ql.Date(17, 11, 1998),
                 ql.Date(17, 12, 1998), ql.Date(17, 5, 1999)]

        results = []

        for dividend_yield in self.dividend_yields:
            for compounding in self.compoundings:
                for frequency in self.frequencies:
                    flat_forward = ql.FlatForward(
                        self.settlement_date,
                        dividend_yield,
                        self.day_counter,
                        compounding,
                        frequency
                    )

                    for date in dates:
                        results.append(
                            {
                                "flatForward": t_flat_forward(self.settlement_date, self.day_counter, dividend_yield, compounding, frequency),
                                "date": t_date_to_string(date),
                                "expected": flat_forward.discount(date)
                            }
                        )

        t_write_results("FlatForward_discount_date.json", results)

    def test_discount_time(self):
        times = [0.08493150684931507, 0.16712328767123288, 0.25205479452054796, 0.336986301369863,
                 0.4191780821917808, 0.5041095890410959, 0.5863013698630137, 1.0]

        results = []

        for dividend_yield in self.dividend_yields:
            for compounding in self.compoundings:
                for frequency in self.frequencies:
                    flat_forward = ql.FlatForward(
                        self.settlement_date,
                        dividend_yield,
                        self.day_counter,
                        compounding,
                        frequency
                    )

                    for time in times:
                        results.append(
                            {
                                "flatForward": t_flat_forward(self.settlement_date, self.day_counter, dividend_yield, compounding, frequency),
                                "time": time,
                                "expected": flat_forward.discount(time)
                            }
                        )

        t_write_results("FlatForward_discount_time.json", results)
