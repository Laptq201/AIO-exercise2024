import math
def approx_sin(x, n):
    x = math.radians(x)
    sin_x = 0
    for i in range(n):
        sin_x += ((-1)**i)*(x**(2*i + 1))/math.factorial(2*i + 1)
    return sin_x


if __name__=="main":
    assert math.isclose(round(approx_sin(x=1, n=10), 4), 0.8415, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_sin(x=3.14, n=10), 4))