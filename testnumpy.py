"""
    测试numpy特性的临时文件
"""
import numpy as np


def test_int():
    """
    测试int类型超过最大值的行为
    :return:
    """
    n = np.zeros(5,dtype=np.uint8)
    n[0]= 254
    for i in range(3):
        print(n[0])
        n[0] += 1



if __name__ == '__main__':
    test_int()