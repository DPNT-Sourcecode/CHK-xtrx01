
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib'))
from solutions.SUM.sum_solution import SumSolution

class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

if __name__ == '__main__':
    test = TestSum()
    test.test_sum()
    print('Test passed')