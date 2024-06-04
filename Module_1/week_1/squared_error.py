def calc_se(y, y_hat):
    return (y - y_hat)**2

if __name__=="main":
    y = 4
    y_hat = 2
    assert calc_se(y, y_hat) == 4
    print(calc_se(2, 1))