# 函数注解
def add1(x: int, y: int) -> int:
    """
    :param x: int
    :param y: int
    :return: int
    """
    return x + y


print(add1.__annotations__)  # 函数注解存放在函数的属性 __annotations__ 中，字典类型
print()

# inspect模块
import inspect


def add2(x: int, /, y: int = 5, *args, m=6, n, **kwargs) -> int:
    return x + y + m + n


sig = inspect.signature(add2)  # 获取可调用对象的签名
print(sig)
print(sig.return_annotation)  # 返回值注解
print(sig.parameters)  # 所有参数的类型注解，有序字典OrderedDict，key是参数，value是Parameter中的annotation
for k, v in sig.parameters.items():
    t: inspect.Parameter = v  # inspect.Parameter里包含了关于参数的所有信息
    print(t.name, t.default, t.kind, t.annotation, sep='\n')  # name:参数名 default:缺省值 kind:类型 annotation:类型注解
print()

# 应用：参数类型检查
from functools import wraps


def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        print(args, kwargs)
        print(params)
        values = tuple(params.values())
        print(values)

        for k, v in enumerate(args):
            if values[k].annotation is not values[k].empty and isinstance(v, values[k].annotation):
                print('{}={} is ok'.format(values[k].name, v))

        for k, v in kwargs.items():
            if params[k].annotation is not inspect.Parameter.empty and isinstance(v, params[k].annotation):
                print('{}={} is ok'.format(k, v))

        ret = fn(*args, **kwargs)
        return ret

    return wrapper


@check
def add3(x: int, y: int = 7) -> int:
    return x + y


add3(1, 2)
add3(1, y=3)
