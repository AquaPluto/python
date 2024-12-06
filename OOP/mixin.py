# 需求：为Document的子类提供打印功能
# 思路1：在Document中提供print方法，让子类去实现，这时候Document就是一个抽象基类，即只提供方法而不实现
# 问题1：基类提供的方法不一定适合所有的子类，那么子类就需要覆盖重写，再者，不一定所有的子类都需要这个打印功能
# class Document:  # 抽象基类，在其他语言中，抽象基类不能实例化，但是Python没有限制，但也遵守约定
#
#     def __init__(self, content):
#         self.content = content
#
#     def print(self):  # 抽象方法
#         raise NotImplementedError()
#
#
# class Word(Document): pass  # 其他功能略去
#
#
# class Pdf(Document): pass  # 其他功能略去


# 思路2：在需要打印的子类上增加打印功能
# 问题2：需要一种功能，有多少子类需要，就要增加多少类，就要增加多次继承，并且功能太多，A类需要某几样功能，B类需要另几样功能，它们需要的是多个功能的自由组合
# class Document:
#     def __init__(self, content):
#         self.content = content
#
#
# class Word(Document): pass
#
#
# class Pdf(Document): pass
#
#
# class PrintableWord(Word):
#     def print(self):
#         print(self.content)


# 思路3：实现一个通用的负责实现该功能的混入类，需要这个功能的子类就去继承这个混入类，既可以让不需要这些功能的子类不用去实现，也可以自由组合功能
class Document:
    def __init__(self, content):
        self.content = content


class Word(Document): pass


class Pdf(Document): pass


class PrintableMixin:
    def print(self):
        print(self.content, 'Mixin')


class PrintableWord(PrintableMixin, Word): pass


class PrintablePdf(PrintableMixin, Pdf): pass
