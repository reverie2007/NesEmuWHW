"""
    读取nes文件
"""
import logging


class NesLoader:
    def __init__(self, filename: str):
        self.logger = logging.getLogger('nes_emu/nes_loader')
        self._header = {}
        self._trainer = None
        self.prg_rom = None
        self.chr_rom = None
        self.open_success = False
        if filename:
            self.open_nes(file_name=filename)

    def open_nes(self, file_name: str):
        """
        打开nes文件
        :param file_name:
        :return:
        """
        try:
            with open(file_name, 'rb') as f:
                nes_buffer = f.read()
        except IOError as err:
            self.logger.error(str(err))
        if nes_buffer[0:4] == b'NES\x1a':
            if (nes_buffer[7] & 0x0c == 0x08) and \
                    (((nes_buffer[9] & 0x0f) << 8 + nes_buffer[4]) * 16384) < len(nes_buffer):
                # and the size taking into account byte 9 does not exceed the actual size of the ROM image,
                # then NES 2.0.
                # nes2.0第9字节有prg rom大小的部分信息，综合第9字节和第4字节得出大小如果没有大于映像大小，
                # 就是nes2.0格式
                # 如果是nes2.0格式
                self.analyzing_nes20(nes_buffer)
            elif (nes_buffer[7] & 0x0c == 0) and nes_buffer[12] == 0 and nes_buffer[13] == 0 and \
                    nes_buffer[14] == 0 and nes_buffer[15] == 0:
                # iNES格式
                self.analyzing_ines(nes_buffer)
            else:
                # 过时的或不兼容的格式
                self.analyzing_archaic_ines(nes_buffer)
        else:
            # 开始字符不是nes\x1a,那就是非法文件
            raise TypeError('iNES文件标识错误，非法文件！')

    def analyzing_archaic_ines(self, nes_buffer):
        """
        解析陈旧的iNES格式
        :return:
        """
        raise NotImplementedError

    def analyzing_nes20(self, nes_buffer):
        """
        解析NES2.0数据
        :param nes_buffer:
        :return:
        """
        raise NotImplementedError

    def analyzing_ines(self, nes_buffer):
        """
        解析iNES数据
        :param nes_buffer:
        :return:
        """
        self._header['PRG_ROM_SIZE_16KB'] = nes_buffer[4]  # 以16384(0x4000)字节作为单位的PRG-ROM大小数量
        self._header['CHR_ROM_SIZE_8KB'] = nes_buffer[5]  # 以 8192(0x2000)字节作为单位的CHR-ROM大小数量
        flag6 = nes_buffer[6]
        # flag6 = 0xf3  # 测试标志6解析情况
        self._header['MAPPER_NUM_LOW4'] = flag6 >> 4
        self._header['SYMBOL_F'] = (flag6 & 8 == 8)  # F: 4屏标志位. (如果该位被设置, 则忽略M标志)
        self._header['SYMBOL_T'] = (flag6 & 4 == 4)  # T: Trainer标志位.  1表示 $7000-$71FF加载 Trainer
        self._header['SYMBOL_B'] = (flag6 & 2 == 2)  # B: SRAM标志位 $6000-$7FFF拥有电池供电的SRAM.
        self._header['SYMBOL_M'] = (flag6 & 1 == 1)  # M: 镜像标志位.  0 = 水平, 1 = 垂直.
        flag7 = nes_buffer[7]
        self._header['MAPPER_NUM_HIGH4'] = flag7 >> 4
        # A file is a NES 2.0 ROM image file if it begins with "NES<EOF>" (same as iNES)
        # and, additionally, the byte at offset 7 has bit 2 clear and bit 3 set:
        self._header['SYMBOL_NES20'] = (flag7 & 0x0C == 0x08)
        self._header['SYMBOL_P'] = (flag7 & 2 == 2)  # P: Playchoice 10标志位. 被设置则表示为PC-10游戏
        self._header['SYMBOL_V'] = (flag7 & 1 == 1)  # V: Vs. Unisystem标志位. 被设置则表示为Vs.  游戏
        # 8-15字节暂时不读取
        # 16字节开始读取内容
        tail = len(nes_buffer)  # 总长度，用来检查读取位置是否超出，超出说明文件格式错误
        current_pos = 16
        if self._header['SYMBOL_T']:
            self._trainer = nes_buffer[current_pos: current_pos + 512]
            current_pos = current_pos + 512

        if self._header['PRG_ROM_SIZE_16KB'] > 0:
            if current_pos > tail:
                raise TypeError('读取prg rom时越界，错误的iNES文件格式！')
            length = 16384 * self._header['PRG_ROM_SIZE_16KB']
            self.prg_rom = nes_buffer[current_pos:(current_pos + length)]
            current_pos = current_pos + length
        else:
            raise TypeError('未找到prg rom，错误的iNES文件格式！')

        if self._header['CHR_ROM_SIZE_8KB'] > 0:
            if current_pos > tail:
                raise TypeError('读取chr rom时越界，错误的iNES文件格式！')
            length = 8192 * self._header['CHR_ROM_SIZE_8KB']
            self.chr_rom = nes_buffer[current_pos:(current_pos + length)]
        # 剩下的内容暂不读取

        # 读取完毕后，设置成功标志
        self.open_success = True


def test_nes_reader():
    reader = NesLoader()
    reader.open_nes('nestest.nes')


def test():
    # 临时测试一些代码结果
    a = 0xfa
    b = 1
    c = ((a & 0x0f) << 8) + b
    print(c)


if __name__ == '__main__':
    # test()
    test_nes_reader()
