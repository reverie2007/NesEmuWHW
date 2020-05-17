"""
    测试numpy特性的临时文件
"""
import numpy as np


def test_int():
    """
    测试int类型超过最大值的行为
    :return:
    """
    n = np.zeros(5, dtype=np.uint8)
    n[0] = 254
    for i in range(3):
        print(n[0])
        n[0] += 1


class C1:
    def __init__(self):
        self.num = 100

    def say(self):
        print(self.num)

    def set_say(self, func):
        self.say = func


class C2:
    def __init__(self):
        self.num = 200

    def say(self):
        print(self.num)


def test_c():
    v1 = C1()
    v1.say()
    v2 = C2()
    v2.say()
    v1.set_say(v2.say)
    v1.say()
    print(v1.num)
    print(v2)
    print(v1.say)


if __name__ == '__main__':
    test_c()
