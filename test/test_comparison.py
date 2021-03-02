import unittest
from mathics.core.expression import Integer, Rational, Real, Complex
from mathics.builtin.comparison import Equal

class ComparisonTest(unittest.TestCase):
    def testEqual(self):
        self.equal_instance = Equal()
        specifications = (
            _EqualityTestSpecification(Integer(1),Integer(1),True),
            _EqualityTestSpecification(Integer(1),Integer(2),False)
        )
        for specification in specifications:
            self.assertEqual(self.equal_instance.do_compare(specification.left, specification.right), specification.result)

class _EqualityTestSpecification:
    def __init__(self, left, right, result):
        self.left = left
        self.right = right
        self.result = result

if __name__ == "__main__":
    unittest.main()