"""
    fc模拟器，2A03cpu模拟
"""
import numpy as np
from nesloader import NesLoader
import zerafael_instructions as instructions
import cpu6502
from ppu import PPU


class Cpu:
    """
    红白机2A03（6502） cpu模拟，
    一、实现全部指令，通过一个字典，指令代码为key，需要调用的函数为value（函数doc字符串能否用于反汇编？？没必要）
    二、16位寻址最高支持64k内存，地址0x0000-0xffff，没有专用io指令，对外设的访问通过读写特定段内存实现
    三、某模拟器同步方法，cpu运行113个周期，调用ppu更新一条扫描线，cpu运行约1000周期，读取一次按键
        指令周期的作用，一个指令实际需要n个周期完成，代码模拟直接得到结果，那本次循环就相当于执行了n个周期
    四、b站搬运youtube视频中带总线是如何模拟的？是否模拟更精确？

    """

    def __init__(self, nes_data):
        # 外部依赖，暂时用ppu，实际应该与总线打交道
        self.ppu = PPU()

        # 寄存器
        self.registers = {'PC': 0,  # Program Counter，16位，
                          'SP': 0xFD,  # Stack Pointer,原代码是0xFF，好像应该是0xfd
                          'A': 0,  # Accumulator
                          'X': 0,  # Register X
                          'Y': 0,  # Register Y
                          'P': 0b00100000}  # Processor Status
        # 状态标志，有些标志硬件自动设置，模拟时要完成对应功能
        # cpu使用1 bit表示一个标志，软件模拟就不必了吧？  ——压栈要用
        # 有一个将标志寄存器8位压栈操作，不模拟该寄存器，分开保存状态，如何保存所有状态？
        self.statusFlags = {'c': 0,  # Carry Flag
                            'z': 1,  # Zero Flag
                            'i': 2,  # Interrupt Disable
                            'd': 3,  # Decimal Mode
                            'b': 4,  # Break Command
                            'v': 6,  # Overflow Flag
                            'n': 7}  # Negative Flag

        # 模拟64k内存
        self.memory = [0] * 0x10000

        # 记录cpu共运行了多少周期，用于测试
        self.all_cycles = 0
        # 临时载入一个nes用于测试
        self.cart = nes_data
        self.init_memory()

        # 暂时使用zerafael的指令实现
        self.instructions = {0x00: instructions.BRK_Implied,
                             0x01: instructions.ORA_Indirect_X,
                             0x05: instructions.ORA_Zero,
                             0x06: instructions.ASL_Zero,
                             0x08: instructions.PHP_Implied,
                             0x09: instructions.ORA_Immediate,
                             0x0A: instructions.ASL_Accumulator,
                             0x0D: instructions.ORA_Absolute,
                             0x0E: instructions.ASL_Absolute,
                             0x10: instructions.BPL_Relative,
                             0x11: instructions.ORA_Indirect_Y,
                             0x15: instructions.ORA_Zero_X,
                             0x16: instructions.ASL_Zero_X,
                             0x18: instructions.CLC_Implied,
                             0x19: instructions.ORA_Absolute_Y,
                             0x1D: instructions.ORA_Absolute_X,
                             0x1E: instructions.ASL_Absolute_X,
                             0x20: instructions.JSR_Absolute,
                             0x21: instructions.AND_Indirect_X,
                             0x24: instructions.BIT_Zero,
                             0x25: instructions.AND_Zero,
                             0x26: instructions.ROL_Zero,
                             0x28: instructions.PLP_Implied,
                             0x29: instructions.AND_Immediate,
                             0x2A: instructions.ROL_Accumulator,
                             0x2C: instructions.BIT_Absolute,
                             0x2D: instructions.AND_Absolute,
                             0x2E: instructions.ROL_Absolute,
                             0x30: instructions.BMI_Relative,
                             0x31: instructions.AND_Indirect_Y,
                             0x35: instructions.AND_Zero_X,
                             0x36: instructions.ROL_Zero_X,
                             0x38: instructions.SEC_Implied,
                             0x39: instructions.AND_Absolute_Y,
                             0x3D: instructions.AND_Absolute_X,
                             0x3E: instructions.ROL_Absolute_X,
                             0x40: instructions.RTI_Implied,
                             0x41: instructions.EOR_Indirect_X,
                             0x45: instructions.EOR_Zero,
                             0x46: instructions.LSR_Zero,
                             0x48: instructions.PHA_Implied,
                             0x49: instructions.EOR_Immediate,
                             0x4A: instructions.LSR_Accumulator,
                             0x4C: instructions.JMP_Absolute,
                             0x4D: instructions.EOR_Absolute,
                             0x4E: instructions.LSR_Absolute,
                             0x50: instructions.BVC_Relative,
                             0x51: instructions.EOR_Indirect_Y,
                             0x55: instructions.EOR_Zero_X,
                             0x56: instructions.LSR_Zero_X,
                             0x58: instructions.CLI_Implied,
                             0x59: instructions.EOR_Absolute_Y,
                             0x5D: instructions.EOR_Absolute_X,
                             0x5E: instructions.LSR_Absolute_X,
                             0x60: instructions.RTS_Implied,
                             0x61: instructions.ADC_Indirect_X,
                             0x65: instructions.ADC_Zero,
                             0x66: instructions.ROR_Zero,
                             0x68: instructions.PLA_Implied,
                             0x69: instructions.ADC_Immediate,
                             0x6A: instructions.ROR_Accumulator,
                             0x6C: instructions.JMP_Indirect,
                             0x6D: instructions.ADC_Absolute,
                             0x6E: instructions.ROR_Absolute,
                             0x70: instructions.BVS_Relative,
                             0x71: instructions.ADC_Indirect_Y,
                             0x75: instructions.ADC_Zero_X,
                             0x76: instructions.ROR_Zero_X,
                             0x78: instructions.SEI_Implied,
                             0x79: instructions.ADC_Absolute_Y,
                             0x7D: instructions.ADC_Absolute_X,
                             0x7E: instructions.ROR_Absolute_X,
                             0x81: instructions.STA_Indirect_X,
                             0x84: instructions.STY_Zero,
                             0x85: instructions.STA_Zero,
                             0x86: instructions.STX_Zero,
                             0x88: instructions.DEY_Implied,
                             0x8A: instructions.TXA_Implied,
                             0x8C: instructions.STY_Absolute,
                             0x8D: instructions.STA_Absolute,
                             0x8E: instructions.STX_Absolute,
                             0x90: instructions.BCC_Relative,
                             0x91: instructions.STA_Indirect_Y,
                             0x94: instructions.STY_Zero_X,
                             0x95: instructions.STA_Zero_X,
                             0x96: instructions.STX_Zero_Y,
                             0x98: instructions.TYA_Implied,
                             0x99: instructions.STA_Absolute_Y,
                             0x9A: instructions.TXS_Implied,
                             0x9D: instructions.STA_Absolute_X,
                             0xA0: instructions.LDY_Immediate,
                             0xA1: instructions.LDA_Indirect_X,
                             0xA2: instructions.LDX_Immediate,
                             0xA4: instructions.LDY_Zero,
                             0xA5: instructions.LDA_Zero,
                             0xA6: instructions.LDX_Zero,
                             0xA8: instructions.TAY_Implied,
                             0xA9: instructions.LDA_Immediate,
                             0xAA: instructions.TAX_Implied,
                             0xAC: instructions.LDY_Absolute,
                             0xAD: instructions.LDA_Absolute,
                             0xAE: instructions.LDX_Absolute,
                             0xB0: instructions.BCS_Relative,
                             0xB1: instructions.LDA_Indirect_Y,
                             0xB4: instructions.LDY_Zero_X,
                             0xB5: instructions.LDA_Zero_X,
                             0xB6: instructions.LDX_Zero_Y,
                             0xB8: instructions.CLV_Implied,
                             0xB9: instructions.LDA_Absolute_Y,
                             0xBA: instructions.TSX_Implied,
                             0xBC: instructions.LDY_Absolute_X,
                             0xBD: instructions.LDA_Absolute_X,
                             0xBE: instructions.LDX_Absolute_Y,
                             0xC0: instructions.CPY_Immediate,
                             0xC1: instructions.CMP_Indirect_X,
                             0xC4: instructions.CPY_Zero,
                             0xC5: instructions.CMP_Zero,
                             0xC6: instructions.DEC_Zero,
                             0xC8: instructions.INY_Implied,
                             0xC9: instructions.CMP_Immediate,
                             0xCA: instructions.DEX_Implied,
                             0xCC: instructions.CPY_Absolute,
                             0xCD: instructions.CMP_Absolute,
                             0xCE: instructions.DEC_Absolute,
                             0xD0: instructions.BNE_Relative,
                             0xD1: instructions.CMP_Indirect_Y,
                             0xD5: instructions.CMP_Zero_X,
                             0xD6: instructions.DEC_Zero_X,
                             0xD8: instructions.CLD_Implied,
                             0xD9: instructions.CMP_Absolute_Y,
                             0xDD: instructions.CMP_Absolute_X,
                             0xDE: instructions.DEC_Absolute_X,
                             0xE0: instructions.CPX_Immediate,
                             0xE1: instructions.SBC_Indirect_X,
                             0xE4: instructions.CPX_Zero,
                             0xE5: instructions.SBC_Zero,
                             0xE6: instructions.INC_Zero,
                             0xE8: instructions.INX_Implied,
                             0xE9: instructions.SBC_Immediate,
                             0xEA: instructions.NOP_Implied,
                             0xEC: instructions.CPX_Absolute,
                             0xED: instructions.SBC_Absolute,
                             0xEE: instructions.INC_Absolute,
                             0xF0: instructions.BEQ_Relative,
                             0xF1: instructions.SBC_Indirect_Y,
                             0xF5: instructions.SBC_Zero_X,
                             0xF6: instructions.INC_Zero_X,
                             0xF8: instructions.SED_Implied,
                             0xF9: instructions.SBC_Absolute_Y,
                             0xFD: instructions.SBC_Absolute_X,
                             0xFE: instructions.INC_Absolute_X,

                             # Unofficial OpCodes
                             0x03: instructions.SLO_Indirect_X,
                             0x04: instructions.DOP_Zero,
                             0x07: instructions.SLO_Zero,
                             0x0C: instructions.TOP_Absolute,
                             0x0F: instructions.SLO_Absolute,
                             0x13: instructions.SLO_Indirect_Y,
                             0x14: instructions.DOP_Zero_X,
                             0x17: instructions.SLO_Zero_X,
                             0x1A: instructions.NOP_Implied,
                             0x1B: instructions.SLO_Absolute_Y,
                             0x1C: instructions.TOP_Absolute_X,
                             0x1F: instructions.SLO_Absolute_X,
                             0x23: instructions.RLA_Indirect_X,
                             0x27: instructions.RLA_Zero,
                             0x2F: instructions.RLA_Absolute,
                             0x33: instructions.RLA_Indirect_Y,
                             0x34: instructions.DOP_Zero_X,
                             0x37: instructions.RLA_Zero_X,
                             0x3A: instructions.NOP_Implied,
                             0x3B: instructions.RLA_Absolute_Y,
                             0x3C: instructions.TOP_Absolute_X,
                             0x3F: instructions.RLA_Absolute_X,
                             0x43: instructions.SRE_Indirect_X,
                             0x44: instructions.DOP_Zero,
                             0x47: instructions.SRE_Zero,
                             0x4F: instructions.SRE_Absolute,
                             0x53: instructions.SRE_Indirect_Y,
                             0x54: instructions.DOP_Zero_X,
                             0x57: instructions.SRE_Zero_X,
                             0x5A: instructions.NOP_Implied,
                             0x5B: instructions.SRE_Absolute_Y,
                             0x5C: instructions.TOP_Absolute_X,
                             0x5F: instructions.SRE_Absolute_X,
                             0x63: instructions.RRA_Indirect_X,
                             0x64: instructions.DOP_Zero,
                             0x67: instructions.RRA_Zero,
                             0x6F: instructions.RRA_Absolute,
                             0x73: instructions.RRA_Indirect_Y,
                             0x74: instructions.DOP_Zero_X,
                             0x77: instructions.RRA_Zero_X,
                             0x7A: instructions.NOP_Implied,
                             0x7B: instructions.RRA_Absolute_Y,
                             0x7C: instructions.TOP_Absolute_X,
                             0x7F: instructions.RRA_Absolute_X,
                             0x80: instructions.DOP_Immediate,
                             0x82: instructions.DOP_Immediate,
                             0x83: instructions.SAX_Indirect_X,
                             0x87: instructions.SAX_Zero,
                             0x89: instructions.DOP_Immediate,
                             0x8F: instructions.SAX_Absolute,
                             0x97: instructions.SAX_Zero_Y,
                             0xA3: instructions.LAX_Indirect_X,
                             0xA7: instructions.LAX_Zero,
                             0xAF: instructions.LAX_Absolute,
                             0xB3: instructions.LAX_Indirect_Y,
                             0xB7: instructions.LAX_Zero_Y,
                             0xBF: instructions.LAX_Absolute_Y,
                             0xC2: instructions.DOP_Immediate,
                             0xC3: instructions.DCP_Indirect_X,
                             0xC7: instructions.DCP_Zero,
                             0xCF: instructions.DCP_Absolute,
                             0xD3: instructions.DCP_Indirect_Y,
                             0xD4: instructions.DOP_Zero_X,
                             0xD7: instructions.DCP_Zero_X,
                             0xDA: instructions.NOP_Implied,
                             0xDB: instructions.DCP_Absolute_Y,
                             0xDC: instructions.TOP_Absolute_X,
                             0xDF: instructions.DCP_Absolute_X,
                             0xE2: instructions.DOP_Immediate,
                             0xE3: instructions.ISB_Indirect_X,
                             0xE7: instructions.ISB_Zero,
                             0xEB: instructions.SBC_Immediate,
                             0xEF: instructions.ISB_Absolute,
                             0xF3: instructions.ISB_Indirect_Y,
                             0xF4: instructions.DOP_Zero_X,
                             0xF7: instructions.ISB_Zero_X,
                             0xFA: instructions.NOP_Implied,
                             0xFB: instructions.ISB_Absolute_Y,
                             0xFC: instructions.TOP_Absolute_X,
                             0xFF: instructions.ISB_Absolute_X
                             }

        # 一切准备好之后，设置启动地址
        # 设置开始指令所处的地址存放在0xFFFC,0xFFFD两个字节，将这两个地址存入程序计数器，
        # 开始时cpu从程序计数器获取地址，从获取的地址开始执行，
        # 小端模式低位存低位，高位存高位。
        self.registers['PC'] = self.memory[0xFFFC] | (self.memory[0xFFFD] << 8) & 0xffff
        self.clock_count = 0

        # 开始禁止中断标志是1？？？
        self.registers['P'] |= 0b00000100

    def doNMI(self):
        self.pushStack((self.registers['PC'] >> 8) & 0xFF)
        self.pushStack(self.registers['PC'] & 0xFF)
        self.pushStack(self.registers['P'])
        self.registers['PC'] = self.memory[0xFFFA] | (self.memory[0xFFFB] << 8)
        self.z = 1

    def writeMemory(self, address, value):
        if address < 0x2000:
            address &= 0x7FF
            self.memory[address] = value
        elif address < 0x4000:
            # PPU Registers
            address &= 0x2007
            self.memory[address] = value
            if address == 0x2000:
                self.ppu.processControlReg1(value)
            elif address == 0x2001:
                self.ppu.processControlReg2(value)
            elif address == 0x2003:
                self.ppu.spriteRamAddr = value
            elif address == 0x2004:
                self.ppu.writeSprRam(value)
            elif address == 0x2005:
                self.ppu.processPPUSCROLL(value)
            elif address == 0x2006:
                self.ppu.processPPUADDR(value)
            elif address == 0x2007:
                self.ppu.writeVRAM(value)
        elif address < 0x4020:
            if address == 0x4014:
                self.ppu.writeSprRamDMA(value)
            elif address == 0x4016:
                if joypad.LastWrote___ == 1 and value == 0:
                    joypad.ReadNumber__ = 0
                joypad.LastWrote___ = value
            self.memory[address] = value
        elif address < 0x8000:
            pass
        else:
            self.memory[address] = value

    def readMemory(self, address):
        value = 0x00
        if address < 0x2000:
            address &= 0x7FF
            value = self.memory[address]
        elif address < 0x4000:
            address &= 0x2007
            if address == 0x2002:
                value = self.ppu.readStatusFlag()
            elif address == 0x2007:
                value = self.ppu.readVRAM()
            self.memory[address] = value
        elif address < 0x4020:
            if address == 0x4016:
                joypad.Strobe()
                value = joypad.KeysBuffer__
            else:
                value = self.memory[address]
        else:
            value = self.memory[address]

        return value

    def setStatus(self, flag, value):
        if value:
            self.registers['P'] |= 1 << flag
        else:
            self.registers['P'] &= ~(1 << flag)

    def getStatus(self, flag):
        if (self.registers['P'] & (1 << flag)) == 0:
            return 0
        else:
            return 1

    def pushStack(self, value):
        self.writeMemory(0x100 + self.registers['SP'], value)
        self.registers['SP'] -= 1

    def pullStack(self):
        self.registers['SP'] += 1
        value = self.readMemory(0x100 + self.registers['SP'])
        return value

    def init_memory(self):
        """
        初始化内存，根据mapper有不同的初始化方法。
        目前只完成mapper0
        :return:
        """
        # 检查mapper，暂未实现

        # 将prg rom放入内存对应位置，一般从0x8000开始
        if len(self.cart.prg_rom) == 0x4000:
            for i in range(len(self.cart.prg_rom)):
                self.memory[i + 0x8000] = self.cart.prg_rom[i]
                self.memory[i + 0xC000] = self.cart.prg_rom[i]
        else:
            for i in range(len(self.cart.prg_rom)):
                self.memory[i + 0x8000] = self.cart.prg_rom[i]

        for i in range(0x20):
            self.memory[i + 0x4000] = 0xFF

        start = self.memory[0xFFFC] | (self.memory[0xFFFD] << 8) & 0xffff
        print('开始地址：', hex(start))

    def run_cycles(self, cycle_count):
        """
        cpu运行指定周期次数，每次cycle_count减去指令周期，小于0之后就停止运行
        初步想法是使用指定周期模拟原机器速度，控制游戏速度。
        原机器cpu运行速度1.7M，画面60帧/秒，创建一个计时器，每秒触发60次，
        每次为cpu_count增加固定次数，cpu运行次数用完就停止，能否实现计时器控制刷新及运行速度？？
        :param cycle_count:
        :return:
        """
        self.clock_count += cycle_count
        while self.clock_count > 0:
            self.check_log()
            op = self.memory[self.registers['PC']]
            cycles = self.instructions[op](self)
            self.all_cycles += cycles
            self.clock_count -= cycles

    def check_log(self):
        """
        检查指令及寄存器状态，是否与另一模拟器（公认模拟准确）一致。
        :return:
        """
        op = self.memory[self.registers['PC']]
        # 检查指令与寄存器状态是否与已有log一致
        exist_log = self.nes_log_file.readline()
        logs = exist_log.split()
        log_addr = int('0x' + logs[0], 16)
        log_op = int('0x' + logs[1], 16)
        for i in range(len(logs)):
            if 'A:' in logs[i]:
                log_A = int('0x' + logs[i][2:], 16)
                log_X = int('0x' + logs[i + 1][2:], 16)
                log_Y = int('0x' + logs[i + 2][2:], 16)
                log_P = int('0x' + logs[i + 3][2:], 16)
                log_SP = int('0x' + logs[i + 4][3:], 16)
                break
        # 当前执行指令，以及本指令  执行完  之后的寄存器状态
        print(hex(self.registers['PC']), ':', hex(op), cpu6502.op_data[op], 'A:',
              hex(self.registers['A']), hex(self.registers['X']), hex(self.registers['Y']),
              hex(self.registers['P']), hex(self.registers['SP']))
        print(hex(log_addr), ':', hex(log_op), cpu6502.op_data[op], 'A:',
              hex(log_A), hex(log_X), hex(log_Y),
              hex(log_P), hex(log_SP))
        print()
        if (self.registers['PC'] != log_addr) or (self.registers['A'] != log_A) or (
                self.registers['X'] != log_X) or (self.registers['Y'] != log_Y) or (
                self.registers['P'] != log_P) or (self.registers['SP'] != log_SP):
            input('bu yi zhi ')

    def read_log(self):
        self.nes_log = False
        self.nes_log_file = open('nestest.log', 'r')
        # self.nes_log_file.readline()


def test_cpu():
    """
    测试代码
    :return:
    """
    nes = NesLoader('nestest.nes')
    if nes.open_success:
        cpu = Cpu(nes_data=nes)
        cpu.read_log()
        while True:
            cpu.run_cycles(100)
            text = input('按q退出，其他任意键继续')
            if text == 'q':
                break
        cpu.nes_log_file.close()


if __name__ == '__main__':
    test_cpu()
