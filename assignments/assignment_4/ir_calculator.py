class IRCalculator:
    @staticmethod
    def calc_ir(salary: float) -> float:
        ret = 0.0
        if salary > 1000.0 and salary <= 2000.0:
            ret += (salary - 1000.0) * 0.15
        if salary > 2000.0:
            ret += 150 + (salary - 2000.0) * 0.2
        if salary > 3000.0:
            ret += (salary - 3000.0) * 0.05

        return float("{:.3f}".format(ret))
