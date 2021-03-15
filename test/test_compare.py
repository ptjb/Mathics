# -*- coding: utf-8 -*-
from test.helper import check_evaluation

def test_compare():
    for str_expr, str_expected in (
        (
            "I == I",
            "True",
        ),
        (
            "I == 0",
            "False",
        ),
        (
            "I + 0 == 1 I - 0",
            "True",
        ),
        (
            "I + 5 == I",
            "False",
        ),
        (
            "0 == 0",
            "True"
        ),
        (
            "0 == 1",
            "False"
        ),
        (
            "1/2 == 1/2",
            "True"
        ),
        (
            "1/2 == 2/4",
            "True"
        ),
        (
            "2/2 == 1",
            "True"
        ),
        (
            "1/2 == 2/3",
            "False"
        ),
        (
            "0.0 == 0.0",
            "True"
        ),
        (
            "0.0 == 0",
            "True"
        ),
        (
            "0.0 == 0/2",
            "True"
        ),
        (
            "0.0 == 1",
            "False"
        ),
        (
            "0.0 == 1.0",
            "False"
        ),
        (
            "0.0 == 1.0*I",
            "False"
        ),
        (
            "0 == 1.0*I",
            "False"
        ),
    ):
        check_evaluation(str_expr, str_expected)

if __name__ == "__main__":
    test_compare()
