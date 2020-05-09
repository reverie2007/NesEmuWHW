"""
    nes cpu 总线模拟
"""
import numpy as np


class YyNesBus:
    """
    cpu 总线模拟，连接cpu，ppu，内存，卡带，手柄等，cpu和ppu能读写数据
    """
    def __init__(self, cpu, ppu):
        self.cpu = cpu
        self.ppu = ppu
        self.memory = np.zeros(0x10000, dtype=np.uint8)

    def insert_cartridge(self, cart):
        """
        插入卡带，读取相应数据，做好保存
        :param cart:
        :return:
        """

    def cpu_read(self, address):
        """
        cpu 读取指定位置数据
        :param address:
        :return:
        """
        pass

    def cpu_write(self, address):
        """
        cpu 写入数据
        :param address:
        :return:
        """
        pass

    def ppu_read(self, address):
        """
        ppu读取数据
        :param address:
        :return:
        """
        pass

    def ppu_write(self, address):
        """
        ppu写入数据，主要是告诉cpu VBlank
        :param address:
        :return:
        """
        pass
