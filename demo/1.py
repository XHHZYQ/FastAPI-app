# print(bool([]))      # False
# print(bool([0]))     # True
# print(bool(""))      # False
# print(bool("0"))     # True
# print(bool(0))        # False
# print(bool(None))    # False


# 用法一:判断"没有/是空的"
# tasks = [0]
# if not tasks:
#     print("暂无任务")

# # 用法二:判断"某个条件不成立"
# is_done = False
# if not is_done:
#     print("任务还没完成")

# fruits = ["苹果", "香蕉", "橙子"]
# for index, fruit in enumerate(fruits, 1):
#   print(index, fruit)

# print(enumerate(fruits))
# print(list(enumerate(fruits)))


# print(True == 1)   # True
# print(False == 0)  # True
# print(True + True) # 2,因为 True 会被当作 1 参与运算


# priority=1 其实就是默认值
# def create_task(title, priority=1, done=False):
#     return {"title": title, "priority": priority, "done": done}

# # 位置参数写法(容易搞混顺序,尤其参数多的时候)
# print(create_task("写作文", 2, True))

# # 关键字参数写法(一目了然)
# print(create_task("写代码", priority=3, done=False))
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

# cond = False
# a = 1
# b = 2

# result = a if cond else b
# print(result)


# class Foo:
#     def __init__(self, x):
#         self.x = x



# class Bar(Foo):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y
#     @staticmethod
#     def method():

#     def f(a: int) -> int:


# class Bar extends Foo {
#   constructor(x, y) {
#     super(x);
#     this.y = y;
#   }
# }


# class Foo:
#     def __init__(self):
#         self.x = 61

# class Bar(Foo):
#     pass   # 子类什么都不写

# b = Bar()
# print(b.x)   # 1，正常继承到了 Foo 的属性


# class Foo:
#     def __init__(self):
#         self.x = 1
#     def say_hello(self):
#         print("hello")

# class Bar(Foo):
#     def __init__(self, y):
#         self.y = y
#         # 注意：这里没调用 super().__init__()
#         super().__init__();

# b = Bar(69)
# print('11', b.x)   # 2，正常
# print('22', b.say_hello())
# print('33', b.y)   # ❌ AttributeError，因为 Foo.__init__ 根本没被执行，x 从来没被设置过


# try:
#     result = 10 / 0
# except Exception as e:
#     print(f"出错了: {e}")


# try:
#     result = 10 / 0
# except ZeroDivisionError as e:      # 精确捕获"除以零"这一种异常
#     print(f"除零错误: {e}")
# except ValueError as e:              # 精确捕获"值错误"
#     print(f"值错误: {e}")
# except Exception as e:               # 兜底，放最后，捕获其他没预料到的异常
#     print(f"未知错误: {e}")


def some_function():
    # TODO: implement later   ← 这样写会报错！注释不算语句，块里还是空的
    pass