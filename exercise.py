# writer：LeBron James
# 面向对象编程


class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


if __name__ == '__main__':
    tom = Cat()
    tom.name = 'Tom'
    tom.eat()
    tom.drink()
    print(tom)
    lazy_cat = Cat()
    lazy_cat.name = '大懒猫'
    lazy_cat.eat()
    lazy_cat.drink()
    print(lazy_cat)


class Cat:
    def __init__(self):
        print("这是一个初始化方法")

        # 定义用 Cat 类创建的猫对象都有一个 name 的属性
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    # 使用类名()创建对象的时候，会自动调用初始化方法 __init__


tom = Cat()
tom.eat()

print('_' * 50)


class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
print(tom.name)
lazy_cat = Cat("大懒猫")
lazy_cat.eat()

print("-" * 50)

str1 = "Hello,Python"
str2 = "Python"
print(str1.index(str2))
tmp = [1, 2, 3, 4, 5, 6]
tmp.insert(-4, 'a')
print(tmp[4])

print(type(1 / 2))
strs = 'abcd'
print(strs.center(10, '*'))

n = 1000
flag = 0
while n > 1:
    print(n)
    n = n / 2
    flag += 1
print(flag)

lists = [1, 2, 3]
lists.insert(2, [7, 8, 9])
print(lists)


def dec(f):
    n = 3

    def wrapper(*args, **kw):
        return f(*args, **kw) * n

    return wrapper


@dec
def foo(n):
    return n * 2


print('*' * 50)
for i in range(10, 1, -2):
    print(i)
print('*' * 50)
numbers = [1, 2, 3, 4]
numbers.append([5, 6, 7, 8])
print(len(numbers))
print(numbers)

strs = 'I like python'
one = strs.find('l')
print(one)
print('*' * 50)
two = strs.index('l')
print(two)
print('*' * 50)
a = [1, 2, 3, 1, 2, 4, 6]
b = list(set(a))
print(b)  # set 是去重方法
print('*' * 50)
a = [1, 2, 3, 1, 2, 4, 6]
b = {}

b = list(b.fromkeys(a))
print(b)

print('*' * 50)
a = [1, 2, 3, 1, 2, 4, 6]
a.sort()

b = []

i = 0

while i < len(a):

    if a[i] not in b:
        b.append(a[i])


    else:

      i += 1

print(b)
