import math 
def approx_sinh(x, n):
    x = math.radians(x)
    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i + 1))/math.factorial(2*i + 1)
    return sinh_x

if __name__=="main":
    assert round(approx_sinh(x=1, n=10), 2)==1.18
    print(round(approx_sinh(x=3.14, n=10), 2))