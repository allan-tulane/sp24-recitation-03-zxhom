from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(10)) == 7 * 10
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0
    assert quadratic_multiply(BinaryNumber(0), BinaryNumber(1)) == 0
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1
    assert quadratic_multiply(BinaryNumber(18), BinaryNumber(2)) == 2 * 18


