"""
    6502指令集
    资料来自https://github.com/dustpg/StepFC/blob/master/step2/'6502.c
"""

# 将指令存放在一个字典中，key是指令编码，value为一个元组，包含指令名与寻址方式两项

op_data = {
    0x0: ('BRK', 'AM_IMP'),
    0x1: ('ORA', 'AM_INX'),
    0x2: ('STP', 'AM_UNK'),
    0x3: ('SLO', 'AM_INX'),
    0x4: ('NOP', 'AM_ZPG'),
    0x5: ('ORA', 'AM_ZPG'),
    0x6: ('ASL', 'AM_ZPG'),
    0x7: ('SLO', 'AM_ZPG'),
    0x8: ('PHP', 'AM_IMP'),
    0x9: ('ORA', 'AM_IMM'),
    0xa: ('ASL', 'AM_ACC'),
    0xb: ('ANC', 'AM_IMM'),
    0xc: ('NOP', 'AM_ABS'),
    0xd: ('ORA', 'AM_ABS'),
    0xe: ('ASL', 'AM_ABS'),
    0xf: ('SLO', 'AM_ABS'),
    0x10: ('BPL', 'AM_REL'),
    0x11: ('ORA', 'AM_INY'),
    0x12: ('STP', 'AM_UNK'),
    0x13: ('SLO', 'AM_INY'),
    0x14: ('NOP', 'AM_ZPX'),
    0x15: ('ORA', 'AM_ZPX'),
    0x16: ('ASL', 'AM_ZPX'),
    0x17: ('SLO', 'AM_ZPX'),
    0x18: ('CLC', 'AM_IMP'),
    0x19: ('ORA', 'AM_ABY'),
    0x1a: ('NOP', 'AM_IMP'),
    0x1b: ('SLO', 'AM_ABY'),
    0x1c: ('NOP', 'AM_ABX'),
    0x1d: ('ORA', 'AM_ABX'),
    0x1e: ('ASL', 'AM_ABX'),
    0x1f: ('SLO', 'AM_ABX'),
    0x20: ('JSR', 'AM_ABS'),
    0x21: ('AND', 'AM_INX'),
    0x22: ('STP', 'AM_UNK'),
    0x23: ('RLA', 'AM_INX'),
    0x24: ('BIT', 'AM_ZPG'),
    0x25: ('AND', 'AM_ZPG'),
    0x26: ('ROL', 'AM_ZPG'),
    0x27: ('RLA', 'AM_ZPG'),
    0x28: ('PLP', 'AM_IMP'),
    0x29: ('AND', 'AM_IMM'),
    0x2a: ('ROL', 'AM_ACC'),
    0x2b: ('ANC', 'AM_IMM'),
    0x2c: ('BIT', 'AM_ABS'),
    0x2d: ('AND', 'AM_ABS'),
    0x2e: ('ROL', 'AM_ABS'),
    0x2f: ('RLA', 'AM_ABS'),
    0x30: ('BMI', 'AM_REL'),
    0x31: ('AND', 'AM_INY'),
    0x32: ('STP', 'AM_UNK'),
    0x33: ('RLA', 'AM_INY'),
    0x34: ('NOP', 'AM_ZPX'),
    0x35: ('AND', 'AM_ZPX'),
    0x36: ('ROL', 'AM_ZPX'),
    0x37: ('RLA', 'AM_ZPX'),
    0x38: ('SEC', 'AM_IMP'),
    0x39: ('AND', 'AM_ABY'),
    0x3a: ('NOP', 'AM_IMP'),
    0x3b: ('RLA', 'AM_ABY'),
    0x3c: ('NOP', 'AM_ABX'),
    0x3d: ('AND', 'AM_ABX'),
    0x3e: ('ROL', 'AM_ABX'),
    0x3f: ('RLA', 'AM_ABX'),
    0x40: ('RTI', 'AM_IMP'),
    0x41: ('EOR', 'AM_INX'),
    0x42: ('STP', 'AM_UNK'),
    0x43: ('SRE', 'AM_INX'),
    0x44: ('NOP', 'AM_ZPG'),
    0x45: ('EOR', 'AM_ZPG'),
    0x46: ('LSR', 'AM_ZPG'),
    0x47: ('SRE', 'AM_ZPG'),
    0x48: ('PHA', 'AM_IMP'),
    0x49: ('EOR', 'AM_IMM'),
    0x4a: ('LSR', 'AM_ACC'),
    0x4b: ('ASR', 'AM_IMM'),
    0x4c: ('JMP', 'AM_ABS'),
    0x4d: ('EOR', 'AM_ABS'),
    0x4e: ('LSR', 'AM_ABS'),
    0x4f: ('SRE', 'AM_ABS'),
    0x50: ('BVC', 'AM_REL'),
    0x51: ('EOR', 'AM_INY'),
    0x52: ('STP', 'AM_UNK'),
    0x53: ('SRE', 'AM_INY'),
    0x54: ('NOP', 'AM_ZPX'),
    0x55: ('EOR', 'AM_ZPX'),
    0x56: ('LSR', 'AM_ZPX'),
    0x57: ('SRE', 'AM_ZPX'),
    0x58: ('CLI', 'AM_IMP'),
    0x59: ('EOR', 'AM_ABY'),
    0x5a: ('NOP', 'AM_IMP'),
    0x5b: ('SRE', 'AM_ABY'),
    0x5c: ('NOP', 'AM_ABX'),
    0x5d: ('EOR', 'AM_ABX'),
    0x5e: ('LSR', 'AM_ABX'),
    0x5f: ('SRE', 'AM_ABX'),
    0x60: ('RTS', 'AM_IMP'),
    0x61: ('ADC', 'AM_INX'),
    0x62: ('STP', 'AM_UNK'),
    0x63: ('RRA', 'AM_INX'),
    0x64: ('NOP', 'AM_ZPG'),
    0x65: ('ADC', 'AM_ZPG'),
    0x66: ('ROR', 'AM_ZPG'),
    0x67: ('RRA', 'AM_ZPG'),
    0x68: ('PLA', 'AM_IMP'),
    0x69: ('ADC', 'AM_IMM'),
    0x6a: ('ROR', 'AM_ACC'),
    0x6b: ('ARR', 'AM_IMM'),
    0x6c: ('JMP', 'AM_IND'),
    0x6d: ('ADC', 'AM_ABS'),
    0x6e: ('ROR', 'AM_ABS'),
    0x6f: ('RRA', 'AM_ABS'),
    0x70: ('BVS', 'AM_REL'),
    0x71: ('ADC', 'AM_INY'),
    0x72: ('STP', 'AM_UNK'),
    0x73: ('RRA', 'AM_INY'),
    0x74: ('NOP', 'AM_ZPX'),
    0x75: ('ADC', 'AM_ZPX'),
    0x76: ('ROR', 'AM_ZPX'),
    0x77: ('RRA', 'AM_ZPX'),
    0x78: ('SEI', 'AM_IMP'),
    0x79: ('ADC', 'AM_ABY'),
    0x7a: ('NOP', 'AM_IMP'),
    0x7b: ('RRA', 'AM_ABY'),
    0x7c: ('NOP', 'AM_ABX'),
    0x7d: ('ADC', 'AM_ABX'),
    0x7e: ('ROR', 'AM_ABX'),
    0x7f: ('RRA', 'AM_ABX'),
    0x80: ('NOP', 'AM_IMM'),
    0x81: ('STA', 'AM_INX'),
    0x82: ('NOP', 'AM_IMM'),
    0x83: ('SAX', 'AM_INX'),
    0x84: ('STY', 'AM_ZPG'),
    0x85: ('STA', 'AM_ZPG'),
    0x86: ('STX', 'AM_ZPG'),
    0x87: ('SAX', 'AM_ZPG'),
    0x88: ('DEY', 'AM_IMP'),
    0x89: ('NOP', 'AM_IMM'),
    0x8a: ('TAX', 'AM_IMP'),
    0x8b: ('XXA', 'AM_IMM'),
    0x8c: ('STY', 'AM_ABS'),
    0x8d: ('STA', 'AM_ABS'),
    0x8e: ('STX', 'AM_ABS'),
    0x8f: ('SAX', 'AM_ABS'),
    0x90: ('BCC', 'AM_REL'),
    0x91: ('STA', 'AM_INY'),
    0x92: ('STP', 'AM_UNK'),
    0x93: ('AHX', 'AM_INY'),
    0x94: ('STY', 'AM_ZPX'),
    0x95: ('STA', 'AM_ZPX'),
    0x96: ('STX', 'AM_ZPY'),
    0x97: ('SAX', 'AM_ZPY'),
    0x98: ('TYA', 'AM_IMP'),
    0x99: ('STA', 'AM_ABY'),
    0x9a: ('TXS', 'AM_IMP'),
    0x9b: ('TAS', 'AM_ABY'),
    0x9c: ('SHY', 'AM_ABX'),
    0x9d: ('STA', 'AM_ABX'),
    0x9e: ('SHX', 'AM_ABY'),
    0x9f: ('AHX', 'AM_ABY'),
    0xa0: ('LDY', 'AM_IMM'),
    0xa1: ('LDA', 'AM_INX'),
    0xa2: ('LDX', 'AM_IMM'),
    0xa3: ('LAX', 'AM_INX'),
    0xa4: ('LDY', 'AM_ZPG'),
    0xa5: ('LDA', 'AM_ZPG'),
    0xa6: ('LDX', 'AM_ZPG'),
    0xa7: ('LAX', 'AM_ZPG'),
    0xa8: ('TAY', 'AM_IMP'),
    0xa9: ('LDA', 'AM_IMM'),
    0xaa: ('TAX', 'AM_IMP'),
    0xab: ('LAX', 'AM_IMM'),
    0xac: ('LDY', 'AM_ABS'),
    0xad: ('LDA', 'AM_ABS'),
    0xae: ('LDX', 'AM_ABS'),
    0xaf: ('LAX', 'AM_ABS'),
    0xb0: ('BCS', 'AM_REL'),
    0xb1: ('LDA', 'AM_INY'),
    0xb2: ('STP', 'AM_UNK'),
    0xb3: ('LAX', 'AM_INY'),
    0xb4: ('LDY', 'AM_ZPX'),
    0xb5: ('LDA', 'AM_ZPX'),
    0xb6: ('LDX', 'AM_ZPY'),
    0xb7: ('LAX', 'AM_ZPY'),
    0xb8: ('CLV', 'AM_IMP'),
    0xb9: ('LDA', 'AM_ABY'),
    0xba: ('TSX', 'AM_IMP'),
    0xbb: ('LAS', 'AM_ABY'),
    0xbc: ('LDY', 'AM_ABX'),
    0xbd: ('LDA', 'AM_ABX'),
    0xbe: ('LDX', 'AM_ABY'),
    0xbf: ('LAX', 'AM_ABY'),
    0xc0: ('CPY', 'AM_IMM'),
    0xc1: ('CMP', 'AM_INX'),
    0xc2: ('NOP', 'AM_IMM'),
    0xc3: ('DCP', 'AM_INX'),
    0xc4: ('CPY', 'AM_ZPG'),
    0xc5: ('CMP', 'AM_ZPG'),
    0xc6: ('DEC', 'AM_ZPG'),
    0xc7: ('DCP', 'AM_ZPG'),
    0xc8: ('INY', 'AM_IMP'),
    0xc9: ('CMP', 'AM_IMM'),
    0xca: ('DEX', 'AM_IMP'),
    0xcb: ('AXS', 'AM_IMM'),
    0xcc: ('CPY', 'AM_ABS'),
    0xcd: ('CMP', 'AM_ABS'),
    0xce: ('DEC', 'AM_ABS'),
    0xcf: ('DCP', 'AM_ABS'),
    0xd0: ('BNE', 'AM_REL'),
    0xd1: ('CMP', 'AM_INY'),
    0xd2: ('STP', 'AM_UNK'),
    0xd3: ('DCP', 'AM_INY'),
    0xd4: ('NOP', 'AM_ZPX'),
    0xd5: ('CMP', 'AM_ZPX'),
    0xd6: ('DEC', 'AM_ZPX'),
    0xd7: ('DCP', 'AM_ZPX'),
    0xd8: ('CLD', 'AM_IMP'),
    0xd9: ('CMP', 'AM_ABY'),
    0xda: ('NOP', 'AM_IMP'),
    0xdb: ('DCP', 'AM_ABY'),
    0xdc: ('NOP', 'AM_ABX'),
    0xdd: ('CMP', 'AM_ABX'),
    0xde: ('DEC', 'AM_ABX'),
    0xdf: ('DCP', 'AM_ABX'),
    0xe0: ('CPX', 'AM_IMM'),
    0xe1: ('SBC', 'AM_INX'),
    0xe2: ('NOP', 'AM_IMM'),
    0xe3: ('ISB', 'AM_INX'),
    0xe4: ('CPX', 'AM_ZPG'),
    0xe5: ('SBC', 'AM_ZPG'),
    0xe6: ('INC', 'AM_ZPG'),
    0xe7: ('ISB', 'AM_ZPG'),
    0xe8: ('INX', 'AM_IMP'),
    0xe9: ('SBC', 'AM_IMM'),
    0xea: ('NOP', 'AM_IMP'),
    0xeb: ('SBC', 'AM_IMM'),
    0xec: ('CPX', 'AM_ABS'),
    0xed: ('SBC', 'AM_ABS'),
    0xee: ('INC', 'AM_ABS'),
    0xef: ('ISB', 'AM_ABS'),
    0xf0: ('BEQ', 'AM_REL'),
    0xf1: ('SBC', 'AM_INY'),
    0xf2: ('STP', 'AM_UNK'),
    0xf3: ('ISB', 'AM_INY'),
    0xf4: ('NOP', 'AM_ZPX'),
    0xf5: ('SBC', 'AM_ZPX'),
    0xf6: ('INC', 'AM_ZPX'),
    0xf7: ('ISB', 'AM_ZPX'),
    0xf8: ('SED', 'AM_IMP'),
    0xf9: ('SBC', 'AM_ABY'),
    0xfa: ('NOP', 'AM_IMP'),
    0xfb: ('ISB', 'AM_ABY'),
    0xfc: ('NOP', 'AM_ABX'),
    0xfd: ('SBC', 'AM_ABX'),
    0xfe: ('INC', 'AM_ABX'),
    0xff: ('ISB', 'AM_ABX'),
}

if __name__ == '__main__':
    print('6502 cpu instructions!')
    for i in range(255):
        print(op_data[i])
