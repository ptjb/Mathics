import unittest
from mathics.core.expression import Integer, Rational, Real, Complex, SymbolTrue, SymbolFalse
from mathics.builtin.comparison import Equal
from mathics.core.definitions import Definitions
from mathics.core.evaluation import Evaluation

class ComparisonTest(unittest.TestCase):
    def setUp(self):
        self.evaluation = Evaluation(Definitions(True))

    def testEqual(self):
        specifications = (
            _EqualityTestSpecification(Integer(1),Integer(1),True),
            _EqualityTestSpecification(Integer(1),Integer(2),False),
            _EqualityTestSpecification(Rational(1,1),Integer(1),True),
            _EqualityTestSpecification(Rational(1,1),Rational(2,2),True),
            _EqualityTestSpecification(Rational(1,1),Rational(1,2),False),
            _EqualityTestSpecification(Rational(1,1),Rational(2,1),False),
            _EqualityTestSpecification(Rational(1,2),Integer(2),False),
            _EqualityTestSpecification(Real(1.0),Integer(1),True),
            _EqualityTestSpecification(Real(1.0),Rational(1,1),True),
            _EqualityTestSpecification(Real(1.0),Real(1.0),True),
            _EqualityTestSpecification(Real(1.0),Real(1.0),True),
            _EqualityTestSpecification(Real(1.0),Real(2.0),False),
            _EqualityTestSpecification(Complex(1.0,0.0),Integer(1),True),
            _EqualityTestSpecification(Complex(1.0,0.0),Rational(1),True),
            _EqualityTestSpecification(Complex(1.0,0.0),Real(1.0),True),
            _EqualityTestSpecification(Complex(0.0,1.0),Integer(1),False),
            _EqualityTestSpecification(Complex(0.0,1.0),Rational(1,1),False),
            _EqualityTestSpecification(Complex(0.0,1.0),Real(1.0),False),
            _EqualityTestSpecification(Complex(1.0,1.0),Complex(1.0,1.0),True),
            _EqualityTestSpecification(Complex(1.0,1.0),Complex(1.0,2.0),False),
            _EqualityTestSpecification(Complex(1.0,1.0),Complex(2.0,1.0),False),
            _EqualityTestSpecification(Complex(1.0,1.0),Complex(2.0,3.0),False)
        )
        for specification in specifications:
            temp = Equal(specification.left, specification.right).evaluate(self.evaluation)
            self.assertEqual(temp, specification.result)

class _EqualityTestSpecification:
    def __init__(self, left, right, result):
        self.left = left
        self.right = right
        self.result = SymbolTrue if result else SymbolFalse

if __name__ == "__main__":
    unittest.main()