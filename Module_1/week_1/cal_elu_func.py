import math 
def calc_elu(x):
    if x > 0:
        return x
    else:
        return 0.01*(math.exp(x) - 1)

if __name__=="main":
    assert round(calc_elu(1)) ==1
    print(round(calc_elu(-1), 2))