from unittest import TestCase, main
from maths import leger_kcal_calculator


class TestLegerCalculations(TestCase):
    def test_calculate_velocity_returns_20_for_input_20km_1h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 1)
        expected = 20
        self.assertEqual(actual, expected)

    def test_calculate_velocity_returns_none_for_input_0h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 0)
        self.assertIsNone(actual)

    def test_calculate_velocity_returns_10_for_input_20km_2h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 2)
        expected = 10
        self.assertEqual(actual, expected)

    def test_calculate_vo2max_returns_correct_value_for_input_1kph(self):
        actual = leger_kcal_calculator.calculate_vo2_max(1)
        expected = 5.3723
        self.assertEqual(actual, expected)

    def test_calculate_vo2max_returns_None_for_input_0kph(self):
        actual = leger_kcal_calculator.calculate_vo2_max(0)
        self.assertIsNone(actual)


if __name__ == '__main__':
    main()
