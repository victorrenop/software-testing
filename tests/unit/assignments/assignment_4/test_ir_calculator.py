from assignments.assignment_4.ir_calculator import IRCalculator
import pytest


class TestSilltPascal:
    @pytest.mark.parametrize("salary", [(999.9), (999.8), (0.0)])
    def test_invalid_salary(self, salary):
        assert IRCalculator.calc_ir(salary) == 0.0

    def test_first_range_salary_limit_1(self):
        assert IRCalculator.calc_ir(1000.1) == 0.015

    def test_first_range_salary_limit_2(self):
        assert IRCalculator.calc_ir(1000.2) == 0.030

    def test_first_range_salary_limit_3(self):
        assert IRCalculator.calc_ir(1999.9) == 149.985

    def test_first_range_salary_limit_4(self):
        assert IRCalculator.calc_ir(2000.0) == 150.0

    def test_second_range_salary_limit_1(self):
        assert IRCalculator.calc_ir(2000.1) == 150.020

    def test_second_range_salary_limit_2(self):
        assert IRCalculator.calc_ir(2999.9) == 349.980

    def test_second_range_salary_limit_3(self):
        assert IRCalculator.calc_ir(3000.0) == 350.0

    def test_third_range_salary_limit_1(self):
        assert IRCalculator.calc_ir(3000.1) == 350.025

    def test_third_range_salary_limit_2(self):
        assert IRCalculator.calc_ir(4000.0) == 600.0
