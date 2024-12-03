def add1(x, y):
    return x + y


add1(1, 2)


# 柯里化
def add2(x):
    def _add2(y):
        return x + y

    return _add2


add2(1)(2)
