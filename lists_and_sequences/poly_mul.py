import numpy
from numpy.fft import fft, ifft


def poly_mul(p1, p2):
    """Multiply two polynomials.

    p1 and p2 are numpy arrays of coefficients in degree-increasing order.
    """
    deg1 = p1.shape[0] - 1
    deg2 = p1.shape[0] - 1
    # Would be 2*(deg1 + deg2) + 1, but the next-power-of-2 handles the +1
    total_num_pts = 2 * (deg1 + deg2)
    next_power_of_2 = 1 << (total_num_pts - 1).bit_length()

    ff_p1 = fft(numpy.pad(p1, (0, next_power_of_2 - p1.shape[0])))
    ff_p2 = fft(numpy.pad(p2, (0, next_power_of_2 - p2.shape[0])))
    product = ff_p1 * ff_p2
    inverted = ifft(product)
    rounded = numpy.round(numpy.absolute(inverted)).astype(numpy.int32)
    return numpy.trim_zeros(rounded)


if __name__ == "__main__":
    p1 = numpy.array([1, 2, 3, 4, 1], dtype=numpy.int32)
    p2 = numpy.array([2, 3, 4, 5], dtype=numpy.int32)

    output = poly_mul(p1, p2)
    expected = numpy.array([2, 7, 16, 30, 36, 34, 24, 5])

    # the actual output would need to be zero-truncated
    print(f"output=\t\t{output}")
    print(f"expected=\t{expected}")
