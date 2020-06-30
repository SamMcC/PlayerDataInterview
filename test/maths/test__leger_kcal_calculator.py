from unittest import TestCase, main, mock
from maths import leger_kcal_calculator


class TestLegerCalculations(TestCase):
    def test_calculate_velocity_returns_20_for_input_20km_1h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 1)
        expected = 20
        self.assertEqual(expected, actual)

    def test_calculate_velocity_returns_none_for_input_0h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 0)
        self.assertIsNone(actual)

    def test_calculate_velocity_returns_10_for_input_20km_2h(self):
        actual = leger_kcal_calculator.calculate_velocity(20, 2)
        expected = 10
        self.assertEqual(expected, actual)

    def test_calculate_vo2max_returns_correct_value_for_input_1kph(self):
        actual = leger_kcal_calculator.calculate_vo2_max(1)
        expected = 5.3723
        self.assertEqual(expected, actual)

    def test_calculate_vo2max_returns_None_for_input_0kph(self):
        actual = leger_kcal_calculator.calculate_vo2_max(0)
        self.assertIsNone(actual)

    def test_calculate_kcal_per_min_returns_None_for_input_mass_0kg(self):
        actual = leger_kcal_calculator.calculate_kcal_per_min(0, 20)
        self.assertIsNone(actual)

    def test_calculate_kcal_per_min_returns_None_for_input_vo2max_0(self):
        actual = leger_kcal_calculator.calculate_kcal_per_min(20, 0)
        self.assertIsNone(actual)

    def test_calculate_kcal_per_min_returns_correct_value_for_input_20kg_vo2max_1(self):
        actual = leger_kcal_calculator.calculate_kcal_per_min(20, 1)
        expected = 0.09720000000000001
        self.assertEqual(expected, actual)

    def test_calculate_kcal_total_returns_None_for_input_0_kcal_per_min(self):
        actual = leger_kcal_calculator.calculate_kcal_total(0, 1)
        self.assertIsNone(actual)

    def test_calculate_kcal_total_returns_None_for_input_0_time_h(self):
        actual = leger_kcal_calculator.calculate_kcal_total(1, 0)
        self.assertIsNone(actual)

    def test_calculate_kcal_total_returns_correct_value_for_input_1_1(self):
        actual = leger_kcal_calculator.calculate_kcal_total(1, 1)
        expected = 60
        self.assertEqual(expected, actual)

    def test_calculate_kcal_total_returns_correct_value_for_input_1_2(self):
        actual = leger_kcal_calculator.calculate_kcal_total(1, 2)
        expected = 120
        self.assertEqual(expected, actual)

    def test_calculate_kcal_returns_correct_value_for_input_1_1_1(self):
        actual = leger_kcal_calculator.calculate_kcal(1, 1, 1)
        expected = (1.56656268, 0.026109378000000003)
        self.assertEqual(expected, actual)

    def test_calculate_kcal_returns_correct_value_for_input_1_1_2(self):
        actual = leger_kcal_calculator.calculate_kcal(1, 1, 2)
        expected = (2.21070708, 0.018422559)
        self.assertEqual(expected, actual)

    @mock.patch('maths.leger_kcal_calculator.calculate_velocity', side_effect=ZeroDivisionError)
    def test_calculate_kcal_returns_None_on_ZeroDivisionError(self, _):
        actual = leger_kcal_calculator.calculate_kcal(1, 1, 2)
        self.assertIsNone(actual)

    @mock.patch('maths.leger_kcal_calculator.calculate_velocity', side_effect=TypeError)
    def test_calculate_kcal_returns_None_on_TypeError(self, _):
        actual = leger_kcal_calculator.calculate_kcal(1, 1, 2)
        self.assertIsNone(actual)

if __name__ == '__main__':
    main()
