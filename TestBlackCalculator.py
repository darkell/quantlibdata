from unittest import TestCase
import QuantLib as ql
from utils import *


class TestBlackCalculator(TestCase):
    def setUp(self):
        self.option_types = [-1, 1]
        self.forwards = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        self.std_devs = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        self.discounts = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        self.day_counters = [ql.Actual365Fixed(), ql.ActualActual()]
        self.spots = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        self.maturities = [0.10, 0.11, 0.12, 0.13, 0.14, 0.15]

    def test_value(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.value()
                            }
                        )

        t_write_results("BlackCalculator_value.json", results)

    def test_delta(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for spot in self.spots:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "spot": spot,
                                    "expected": black_calculator.delta(spot)
                                }
                            )

        t_write_results("BlackCalculator_delta.json", results)

    def test_deltaForward(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.deltaForward()
                            }
                        )

        t_write_results("BlackCalculator_deltaForward.json", results)

    def test_elasticity(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for spot in self.spots:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "spot": spot,
                                    "expected": black_calculator.elasticity(spot)
                                }
                            )

        t_write_results("BlackCalculator_elasticity.json", results)

    def test_elasticityForward(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.elasticityForward()
                            }
                        )

        t_write_results("BlackCalculator_elasticityForward.json", results)

    def test_gamma(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for spot in self.spots:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "spot": spot,
                                    "expected": black_calculator.gamma(spot)
                                }
                            )

        t_write_results("BlackCalculator_gamma.json", results)

    def test_gammaForward(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.gammaForward()
                            }
                        )

        t_write_results("BlackCalculator_gammaForward.json", results)

    def test_theta(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for spot in self.spots:
                            for maturity in self.maturities:
                                striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                                black_calculator = ql.BlackCalculator(
                                    striked_type_payoff,
                                    forward,
                                    std_dev,
                                    discount
                                )

                                results.append(
                                    {
                                        "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                        "forward": forward,
                                        "stdDev": std_dev,
                                        "discount": discount,
                                        "spot": spot,
                                        "maturity": maturity,
                                        "expected": black_calculator.theta(spot, maturity)
                                    }
                                )

        t_write_results("BlackCalculator_theta.json", results)

    def test_thetaPerDay(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for spot in self.spots:
                            for maturity in self.maturities:
                                striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                                black_calculator = ql.BlackCalculator(
                                    striked_type_payoff,
                                    forward,
                                    std_dev,
                                    discount
                                )

                                results.append(
                                    {
                                        "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                        "forward": forward,
                                        "stdDev": std_dev,
                                        "discount": discount,
                                        "spot": spot,
                                        "maturity": maturity,
                                        "expected": black_calculator.thetaPerDay(spot, maturity)
                                    }
                                )

        t_write_results("BlackCalculator_thetaPerDay.json", results)

    def test_vega(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for maturity in self.maturities:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "maturity": maturity,
                                    "expected": black_calculator.vega(maturity)
                                }
                            )

        t_write_results("BlackCalculator_vega.json", results)

    def test_rho(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for maturity in self.maturities:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "maturity": maturity,
                                    "expected": black_calculator.rho(maturity)
                                }
                            )

        t_write_results("BlackCalculator_rho.json", results)

    def test_dividendRho(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        for maturity in self.maturities:
                            striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                            black_calculator = ql.BlackCalculator(
                                striked_type_payoff,
                                forward,
                                std_dev,
                                discount
                            )

                            results.append(
                                {
                                    "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                    "forward": forward,
                                    "stdDev": std_dev,
                                    "discount": discount,
                                    "maturity": maturity,
                                    "expected": black_calculator.dividendRho(maturity)
                                }
                            )

        t_write_results("BlackCalculator_dividendRho.json", results)

    def test_itmCashProbability(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.itmCashProbability()
                            }
                        )

        t_write_results("BlackCalculator_itmCashProbability.json", results)

    def test_itmAssetProbability(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.itmAssetProbability()
                            }
                        )

        t_write_results("BlackCalculator_itmAssetProbability.json", results)

    def test_strikeSensitivity(self):
        results = []

        for option_type in self.option_types:
            for forward in self.forwards:
                for std_dev in self.std_devs:
                    for discount in self.discounts:
                        striked_type_payoff = ql.PlainVanillaPayoff(option_type, 0.5)
                        black_calculator = ql.BlackCalculator(
                            striked_type_payoff,
                            forward,
                            std_dev,
                            discount
                        )

                        results.append(
                            {
                                "strikedTypePayoff": t_striked_type_payoff(striked_type_payoff),
                                "forward": forward,
                                "stdDev": std_dev,
                                "discount": discount,
                                "expected": black_calculator.strikeSensitivity()
                            }
                        )

        t_write_results("BlackCalculator_strikeSensitivity.json", results)
