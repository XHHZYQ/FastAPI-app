# print(bool([]))      # False
# print(bool([0]))     # True
# print(bool(""))      # False
# print(bool("0"))     # True
# print(bool(0))        # False
# print(bool(None))    # False


# s = {1, 2, 2, 3}
# print(s)          # {1, 2, 3}
# print(2 in s)      # True，成员判断很快


# def add(a: int, b: int) -> int:
#     return a + b

# print(add("hello ", "world"))   # 类型标注写的是 int，但传字符串
# 结果：正常运行，返回 "helloworld"，Python 完全不管你标注了什么

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5}

# dict3 = {**dict1}
# print(dict3 == dict1)
# dict4 = {**dict1, **dict2}
# print(dict4)

# def f(**kwargs):
#   print(kwargs["a"])
#   # print(kwargs.b)

# f(a=1, b=2, c=3)
# f(d=4, e=5)

cond = False
a = 1
b = 2

result = a if cond else b
print(result)
