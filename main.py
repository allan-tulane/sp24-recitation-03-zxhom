"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.


def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def quadratic_multiply(x, y):
  # this just converts the result from a BinaryNumber to a regular int
  return _quadratic_multiply(x, y).decimal_val  #-- OG
  #return _quadratic_multiply(x, y)


# X and Y are STRINGS
def _quadratic_multiply(x, y):
  ### TODO
  xvec = x.binary_vec
  yvec = y.binary_vec

  padded = pad(xvec, yvec)
  xvec = padded[0]
  yvec = padded[1]

  # (above) Obtain xvec and yvec, the binary_vec values of x and y

  if (x.decimal_val and y.decimal_val) <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  n = len(xvec)
  # n is the length of the padded BinaryNumbers - determines coefficent 2^n

  # Split_number returns a tuple of BinaryNumbers which can be indexed
  split1 = split_number(xvec)
  split2 = split_number(yvec)

  x_left = split1[0]
  x_right = split1[1]
  y_left = split2[0]
  y_right = split2[1]

  # Bit_shift and split_number use binary2int so output is a BinaryNumber
  sum1 = bit_shift(_quadratic_multiply(x_left, y_left), n)

  tmp1 = _quadratic_multiply(x_left, y_right)
  tmp2 = _quadratic_multiply(x_right, y_left)
  sum2 = bit_shift(BinaryNumber(tmp1.decimal_val + tmp2.decimal_val), (n // 2))
  #Troubleshoot fix: had to cast sum of tmp1 and tmp2 to BinaryNumber for bit_shift to work

  sum3 = _quadratic_multiply(x_right, y_right)

  # binary_val is a BinaryNumber
  binary_val = BinaryNumber(sum1.decimal_val + sum2.decimal_val +
                            sum3.decimal_val)

  return binary_val
  #return sum1 + sum2 + sum3
  # Output should be a BinaryNumber bc quadratic_multiply converts output from _quadratic_multiply to a decimal


# Finally, you have to do three sums to get the final answer. For this assignment, you can just use the decimal_vals of each number to do this


def test_quadratic_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  f(x, y)

  return (time.time() - start) * 1000


#print(test_quadratic_multiply(BinaryNumber(1000), BinaryNumber(3188), _quadratic_multiply))


def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
  assert quadratic_multiply(BinaryNumber(7), BinaryNumber(10)) == 7 * 10
  assert quadratic_multiply(BinaryNumber(0), BinaryNumber(0)) == 0
  assert quadratic_multiply(BinaryNumber(0), BinaryNumber(1)) == 0
  assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1
  assert quadratic_multiply(BinaryNumber(18), BinaryNumber(2)) == 2 * 18


test_multiply()

# Not sure if f should be quadratric_multiply or _quadratic_multiply ????

#print(test_quadratic_multiply("01", "11", _quadratic_multiply))
