from unittest import TestCase
import QuantLib as ql
from utils import *


class TestInterestRate(TestCase):
    def setUp(self):
        self.rates = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        self.day_counters = [ql.Actual365Fixed(), ql.ActualActual()]
        self.compoundings = [ql.Simple, ql.Compounded, ql.Continuous, ql.SimpleThenCompounded]
        self.frequencies = [ql.Annual, ql.Semiannual, ql.EveryFourthMonth, ql.Quarterly, ql.Bimonthly,
                            ql.Monthly, ql.EveryFourthWeek, ql.Biweekly, ql.Weekly, ql.Daily]
        self.times = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]

    def test_compoundFactor_time(self):
        results = []

        for rate in self.rates:
            for day_counter in self.day_counters:
                for compounding in self.compoundings:
                    for frequency in self.frequencies:
                        interest_rate = ql.InterestRate(
                            rate,
                            day_counter,
                            compounding,
                            frequency
                        )

                        for time in self.times:
                            result = interest_rate.compoundFactor(time)

                            results.append(
                                {
                                    "interestRate": t_interest_rate(interest_rate),
                                    "time": time,
                                    "expected": result
                                }
                            )

        t_write_results("InterestRate_compoundFactor_time.json", results)

    def test_discountFactor_time(self):
        results = []

        for rate in self.rates:
            for day_counter in self.day_counters:
                for compounding in self.compoundings:
                    for frequency in self.frequencies:
                        interest_rate = ql.InterestRate(
                            rate,
                            day_counter,
                            compounding,
                            frequency
                        )

                        for time in self.times:
                            results.append(
                                {
                                    "interestRate": t_interest_rate(interest_rate),
                                    "time": time,
                                    "expected": interest_rate.discountFactor(time)
                                }
                            )

        t_write_results("InterestRate_discountFactor_time.json", results)

    def test_equivalentRate_time(self):
        results = []

        for rate in self.rates:
            for day_counter in self.day_counters:
                for compounding in self.compoundings:
                    for frequency in self.frequencies:
                        interest_rate = ql.InterestRate(
                            rate,
                            day_counter,
                            compounding,
                            frequency
                        )

                        for compounding2 in self.compoundings:
                            for frequency2 in self.frequencies:
                                for time in self.times:
                                    results.append(
                                        {
                                            "interestRate": t_interest_rate(interest_rate),
                                            "compounding": t_to_compounding(compounding2),
                                            "frequency": t_to_frequency(frequency2),
                                            "time": time,
                                            "expected": t_interest_rate(interest_rate.equivalentRate(compounding2, frequency2, time))
                                        }
                                    )

        t_write_results("InterestRate_equivalentRate_time.json", results)

    def test_impliedRate_time(self):
        results = []

        for compound in [1.0, 0.9, 0.8]:
            for day_counter in self.day_counters:
                for compounding in self.compoundings:
                    for frequency in self.frequencies:
                        for time in filter(lambda t: t>0, self.times):

                            results.append(
                                {
                                    "compound": compound,
                                    "dayCounter": t_to_day_counter(day_counter),
                                    "compounding": t_to_compounding(compounding),
                                    "frequency": t_to_frequency(frequency),
                                    "time": time,
                                    "expected": t_interest_rate(ql.InterestRate.impliedRate(compound, day_counter, compounding, frequency, time))
                                }
                            )

        t_write_results("InterestRate_impliedRate_time.json", results)
