"""Python 语法速通脚本

目标：把阅读一个普通 Python 项目（比如 todo.py）需要的语法点过一遍。
运行方式：python syntax_tour.py
建议：每看完一节，回头对照 todo.py 里对应的写法。
"""

import json


def section(title):
    """打印分节标题，方便阅读输出。"""
    print(f"\n{'=' * 10} {title} {'=' * 10}")


# ---------------------------------------------------------------
# 1. 变量与基本类型
# ---------------------------------------------------------------
section("1. 变量与基本类型")

name = "小明"          # str 字符串
age = 18                # int 整数
height = 1.75           # float 浮点数
is_student = True       # bool 布尔值
nothing = None          # None 表示"空值"

# Python 是动态类型：变量不用声明类型，赋值时类型就确定了
print(name, age, height, is_student, nothing)
print(type(name), type(age), type(height))  # 用 type() 查看类型


# ---------------------------------------------------------------
# 2. 字符串操作 / f-string
# ---------------------------------------------------------------
section("2. 字符串操作")

greeting = "Hello"
target = "World"

# 字符串拼接
print(greeting + ", " + target + "!")

# f-string：最常用的格式化方式，todo.py 里的 print(f"...") 就是这个
print(f"{greeting}, {target}! 年龄是 {age} 岁")

# 常用字符串方法
s = "  Python Syntax  "
print(s.strip())        # 去除首尾空格
print(s.strip().lower())  # 转小写
print(s.strip().upper())  # 转大写
print(",".join(["a", "b", "c"]))  # 用逗号连接列表元素
print("a,b,c".split(","))         # 按逗号切分成列表


# ---------------------------------------------------------------
# 3. 列表 list（最常用的容器，对应 todo.py 里的 tasks = []）
# ---------------------------------------------------------------
section("3. 列表 list")

tasks = []
tasks.append("买菜")     # 追加元素，todo.py 的 add_task 就是这样写的
tasks.append("写代码")
tasks.append("睡觉")

print(tasks)
print(len(tasks))        # 长度
print(tasks[0])          # 索引访问，从 0 开始
print(tasks[-1])         # 负数索引 = 倒数第几个
print(tasks[0:2])        # 切片：取第 0 到第 1 个（不含索引 2）

tasks.remove("写代码")   # 按值删除
print(tasks)

# enumerate：同时拿到"序号"和"值"，todo.py 的 list_tasks 就用到了
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")


# ---------------------------------------------------------------
# 4. 元组 tuple（不可变的列表）
# ---------------------------------------------------------------
section("4. 元组 tuple")

point = (3, 4)           # 一旦创建不能修改
x, y = point              # 元组解包，很常见的写法
print(f"x={x}, y={y}")


# ---------------------------------------------------------------
# 5. 字典 dict（键值对，非常常用）
# ---------------------------------------------------------------
section("5. 字典 dict")

user = {
    "name": "小红",
    "age": 20,
    "is_vip": False,
}

print(user["name"])          # 按 key 取值
print(user.get("email", "未填写"))  # get：key 不存在时给默认值，避免报错

user["email"] = "xiaohong@example.com"  # 新增/修改键值
print(user)

for key, value in user.items():  # 遍历字典的 key 和 value
    print(f"{key}: {value}")


# ---------------------------------------------------------------
# 6. 集合 set（去重、成员判断）
# ---------------------------------------------------------------
section("6. 集合 set")

nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)
print(unique_nums)           # {1, 2, 3}，自动去重
print(2 in unique_nums)      # 成员判断，速度很快


# ---------------------------------------------------------------
# 7. 条件语句 / 循环（todo.py 的 main() 就是 while + if/elif）
# ---------------------------------------------------------------
section("7. 条件语句与循环")

score = 75
if score >= 90:
    level = "优秀"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"
print(level)

# for 循环
for i in range(3):           # range(3) = 0, 1, 2
    print(f"第 {i} 次循环")

# while 循环 + break/continue（对应 todo.py 的 main 主循环）
count = 0
while True:
    count += 1
    if count == 2:
        continue             # 跳过本次循环剩余部分
    if count > 3:
        break                 # 跳出循环
    print(f"count = {count}")


# ---------------------------------------------------------------
# 8. 列表推导式（简洁地生成列表，读代码时经常见到）
# ---------------------------------------------------------------
section("8. 列表推导式")

squares = [n * n for n in range(5)]          # 等价于用 for 循环 append
print(squares)

even_squares = [n * n for n in range(10) if n % 2 == 0]  # 带条件过滤
print(even_squares)


# ---------------------------------------------------------------
# 9. 函数：默认参数 / 可变参数 / 关键字参数 / lambda
# ---------------------------------------------------------------
section("9. 函数进阶")


def greet(name, greeting="你好"):   # greeting 有默认值，调用时可以不传
    return f"{greeting}, {name}!"


print(greet("小明"))
print(greet("小红", greeting="早上好"))


def add_all(*numbers):              # *numbers 收集任意数量的位置参数为元组
    return sum(numbers)


print(add_all(1, 2, 3, 4))


def show_info(**info):              # **info 收集任意数量的关键字参数为字典
    for k, v in info.items():
        print(f"{k} = {v}")


show_info(city="北京", job="工程师")

square_fn = lambda n: n * n         # lambda：一行的匿名函数
print(square_fn(5))


# ---------------------------------------------------------------
# 10. 异常处理 try/except/finally
# ---------------------------------------------------------------
section("10. 异常处理")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"出错了: {e}")
finally:
    print("不管有没有出错，这里都会执行")


# ---------------------------------------------------------------
# 11. 类与面向对象（todo.py 目前是函数式写法，很多项目会用类来组织）
# ---------------------------------------------------------------
section("11. 类与面向对象")


class TodoList:
    """一个用类实现的待办事项列表，对比 todo.py 的函数式写法。"""

    def __init__(self, owner):      # 构造方法，创建对象时自动调用
        self.owner = owner          # self.xxx 是这个对象的"属性"
        self.tasks = []

    def add_task(self, title):      # 方法：第一个参数固定是 self
        self.tasks.append(title)
        print(f"[{self.owner}] 已添加任务: {title}")

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def __str__(self):              # 魔术方法：print(对象) 时会调用它
        return f"TodoList(owner={self.owner}, count={len(self.tasks)})"


my_list = TodoList("小明")          # 创建对象（实例化）
my_list.add_task("学习 Python")
my_list.add_task("看项目代码")
my_list.list_tasks()
print(my_list)                      # 会调用 __str__


class UrgentTodoList(TodoList):     # 继承：复用 TodoList 的能力
    def add_task(self, title):      # 重写(override)父类方法
        super().add_task(f"[紧急] {title}")  # super() 调用父类方法


urgent_list = UrgentTodoList("小红")
urgent_list.add_task("修复线上 bug")


# ---------------------------------------------------------------
# 12. with 语句 / 上下文管理器（常用于文件、资源操作）
# ---------------------------------------------------------------
section("12. with 语句与文件读写")

data = {"tasks": ["买菜", "写代码"]}

with open("demo_tasks.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# with 代码块结束后，文件会自动关闭，不需要手动 f.close()

with open("demo_tasks.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)


# ---------------------------------------------------------------
# 13. 常用内置函数：map / filter / zip / sorted
# ---------------------------------------------------------------
section("13. 常用内置函数")

nums = [4, 1, 3, 2]
print(sorted(nums))                          # 排序（生成新列表，不改变原列表）
print(sorted(nums, reverse=True))            # 倒序

doubled = list(map(lambda n: n * 2, nums))   # map：对每个元素做处理
print(doubled)

filtered = list(filter(lambda n: n > 2, nums))  # filter：按条件筛选
print(filtered)

names = ["小明", "小红"]
ages = [18, 20]
paired = list(zip(names, ages))              # zip：把多个列表按位置打包
print(paired)


# ---------------------------------------------------------------
# 14. 类型注解（type hints）——现代 Python 项目里很常见
# ---------------------------------------------------------------
section("14. 类型注解")


def add(a: int, b: int) -> int:
    """参数和返回值的类型注解只是给人看/给工具检查的提示，
    Python 运行时并不会强制检查类型。"""
    return a + b


print(add(1, 2))


# ---------------------------------------------------------------
# 15. 模块入口写法：if __name__ == "__main__"
# ---------------------------------------------------------------
section("15. 模块入口写法")

# 这就是 todo.py 结尾那句的含义：
#   直接运行本文件时，__name__ 的值是 "__main__"，if 条件成立，main() 会被调用；
#   如果本文件被其他文件 import，__name__ 会是模块名（比如 "syntax_tour"），
#   if 条件不成立，main() 不会自动执行——这样既能被运行，也能被安全地导入复用。


def main():
    print("这是脚本的主入口，只有直接运行本文件时才会执行到这里。")


if __name__ == "__main__":
    main()
