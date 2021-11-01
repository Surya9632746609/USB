

# def addition(a,b):
#     return a+b
#
# def subtraction(a,b):
#     return a-b
#
# def multiplication(a,b):
#     return a*b
#
#
# def test_addition():
#     result = addition(5,5)
#     assert result == 10
#
# def test_subtraction():
#     result = subtraction(9,5)
#     assert result == 4
#
# def test_multiplication():
#     result = multiplication(5,5)
#     assert result == 25

import pytest

def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1, input2, output",[(2,3,5),(3,3,6),(5,5,10)])
def test_calc_sum_1(input1, input2, output):
    result = sum(input1,input2)
    assert result == output