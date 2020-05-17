"""
    github 上zerafael的指令实现
"""
import zerafael_addressing_mode as addressingMode


# TODO: Verificar se nao existem enderecamentos maiores que 1 byte
def rel_addr(value):
    if value & 0b10000000:
        value &= 0b1111111
        value -= 128

    return value

def setN(cpu, value):
    if value & (1 << 7) == 1 << 7:
        cpu.setStatus(cpu.statusFlags['n'], 1)
    else:
        cpu.setStatus(cpu.statusFlags['n'], 0)


def setZ(cpu, value):
    if value == 0:
        cpu.setStatus(cpu.statusFlags['z'], 1)
    else:
        cpu.setStatus(cpu.statusFlags['z'], 0)


def setO(cpu, value):
    cpu.setStatus(cpu.statusFlags['v'], value)


def setC(cpu, value):
    cpu.setStatus(cpu.statusFlags['c'], value)


# Feito!
def ADC_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ADC_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 255)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def AND_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.registers_a & cpu.readMemory(cpu.registers_pc + 1)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def AND_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def AND_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    return nCycles


# Feito!
def ASL_Accumulator(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_a = value
    return nCycles


# Feito!
def ASL_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ASL_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ASL_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ASL_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def BCC_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['c']) == False:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BCS_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['c']) == True:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BEQ_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['z']) == True:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BIT_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value & cpu.registers_a)
    setO(cpu, (value >> 6) & 1)
    return nCycles


# Feito!
def BIT_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value & cpu.registers_a)
    setO(cpu, (value >> 6) & 1)
    return nCycles


# Feito!
def BMI_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['n']) == True:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BNE_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['z']) == False:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BPL_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['n']) == False:
        nCycles += 1
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 1
        # cpu.registers_pc += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BRK_Implied(cpu):
    size = 1
    nCycles = 7

    cpu.registers_pc += 2
    cpu.pushStack((cpu.registers_pc >> 8) & 0xFF)
    cpu.pushStack(cpu.registers_pc & 0xFF)
    cpu.setStatus(cpu.statusFlags['b'], 1)
    cpu.pushStack(cpu.registers_p)
    cpu.setStatus(cpu.statusFlags['i'], 1)
    cpu.registers_pc = (cpu.readMemory(0xFFFE) | (cpu.readMemory(0xFFFF) << 8))
    cpu.registers_pc += size
    return nCycles


# Feito!
def BVC_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['v']) == False:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def BVS_Relative(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = rel_addr(value)
    if cpu.getStatus(cpu.statusFlags['v']) == True:
        if (cpu.registers_pc & 0xFF00) != ((cpu.registers_pc + value) & 0xFF00):
            nCycles += 2
        else:
            nCycles += 1
        cpu.registers_pc += value
    cpu.registers_pc += size
    return nCycles


# Feito!
def CLC_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['c'], 0)
    cpu.registers_pc += size
    return nCycles


# Feito!
def CLD_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['d'], 0)
    cpu.registers_pc += size
    return nCycles


# Feito!
def CLI_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['i'], 0)
    cpu.registers_pc += size
    return nCycles


# Feito!
def CLV_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['v'], 0)
    cpu.registers_pc += size
    return nCycles


# Feito!
def CMP_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CMP_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPX_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = cpu.registers_x - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPX_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_x - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPX_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_x - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPY_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value = cpu.registers_y - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPY_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_y - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def CPY_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = cpu.registers_y - value
    cpu.registers_pc += size
    setC(cpu, 1 if value >= 0 else 0)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)
    return nCycles


# Feito!
def DEC_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def DEC_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def DEC_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def DEC_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def DEX_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_x
    value = (value - 1) & 0xFF
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def DEY_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_y
    value = (value - 1) & 0xFF
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def EOR_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    value ^= cpu.registers_a
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INC_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INC_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INC_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INC_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INX_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_x
    value = (value + 1) & 0xFF
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def INY_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_y
    value = (value + 1) & 0xFF
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def JMP_Absolute(cpu):
    size = 3
    nCycles = 3

    address = addressingMode.Absolute(cpu)
    cpu.registers_pc += size
    cpu.registers_pc = address
    return nCycles


# Feito!
def JMP_Indirect(cpu):
    size = 3
    nCycles = 5

    address = addressingMode.Indirect(cpu)
    cpu.registers_pc += size
    cpu.registers_pc = address
    return nCycles


# Feito!
def JSR_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    cpu.registers_pc += 2
    cpu.pushStack((cpu.registers_pc >> 8) & 0xFF)
    cpu.pushStack(cpu.registers_pc & 0xFF)
    cpu.registers_pc = address
    return nCycles


# Feito!
def LDA_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDA_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDX_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDX_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDX_Zero_Y(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDX_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDX_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDY_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDY_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDY_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDY_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LDY_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_y = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LSR_Accumulator(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LSR_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LSR_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LSR_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def LSR_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def NOP_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.registers_pc += size
    return nCycles


# Feito!
def ORA_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def ORA_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    value |= cpu.registers_a
    cpu.registers_pc += size
    cpu.registers_a = value
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def PHA_Implied(cpu):
    size = 1
    nCycles = 3

    value = cpu.registers_a
    cpu.pushStack(value)
    cpu.registers_pc += size
    return nCycles


# Feito!
def PHP_Implied(cpu):
    size = 1
    nCycles = 3

    value = cpu.registers_p
    cpu.pushStack(value)
    cpu.registers_pc += size
    return nCycles


# Feito!
def PLA_Implied(cpu):
    size = 1
    nCycles = 4

    value = cpu.pullStack()
    cpu.registers_a = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    return nCycles


# Feito!
def PLP_Implied(cpu):
    size = 1
    nCycles = 4

    value = cpu.pullStack()
    # Don't set the break flag
    cpu.registers_p = (value & 0xEF)
    # Always set the non used flag
    cpu.registers_p |= (1 << 5)
    cpu.registers_pc += size
    return nCycles


# Feito!
def ROL_Accumulator(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_a = value
    return nCycles


# Feito!
def ROL_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROL_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROL_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROL_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROR_Accumulator(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    if cpu.getStatus(cpu.statusFlags['c']):
        value |= 0x100
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_a = value
    return nCycles


# Feito!
def ROR_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) + carry
    cpu.registers_pc += size
    setN(cpu, (value >> 7) & 1)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROR_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) + carry
    cpu.registers_pc += size
    setN(cpu, (value >> 7) & 1)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROR_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) + carry
    cpu.registers_pc += size
    setN(cpu, (value >> 7) & 1)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def ROR_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) + carry
    cpu.registers_pc += size
    setN(cpu, (value >> 7) & 1)
    setZ(cpu, value)
    cpu.writeMemory(address, value)
    return nCycles


# Feito!
def RTI_Implied(cpu):
    size = 1
    nCycles = 6

    value = cpu.pullStack()
    cpu.registers_p = value
    cpu.registers_p |= (1 << 5)
    value = cpu.pullStack()
    value |= (cpu.pullStack() << 8)
    cpu.registers_pc = value
    return nCycles


# Feito!
def RTS_Implied(cpu):
    size = 1
    nCycles = 6

    value = cpu.pullStack()
    value += ((cpu.pullStack()) << 8)
    cpu.registers_pc = value
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Immediate(cpu):
    size = 2
    nCycles = 2

    value = cpu.readMemory(cpu.registers_pc + 1)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    # Todo: Verificar o (1 - carry) depois
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Absolute_X(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SBC_Indirect_Y(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SEC_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['c'], 1)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SED_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['d'], 1)
    cpu.registers_pc += size
    return nCycles


# Feito!
def SEI_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.setStatus(cpu.statusFlags['i'], 1)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Absolute_X(cpu):
    size = 3
    nCycles = 5

    address = addressingMode.Absolute_X(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Absolute_Y(cpu):
    size = 3
    nCycles = 5

    address = addressingMode.Absolute_Y(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STA_Indirect_Y(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_Y(cpu)
    cpu.writeMemory(address, cpu.registers_a)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STX_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    cpu.writeMemory(address, cpu.registers_x)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STX_Zero_Y(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_Y(cpu)
    cpu.writeMemory(address, cpu.registers_x)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STX_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    cpu.writeMemory(address, cpu.registers_x)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STY_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    cpu.writeMemory(address, cpu.registers_y)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STY_Zero_X(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_X(cpu)
    cpu.writeMemory(address, cpu.registers_y)
    cpu.registers_pc += size
    return nCycles


# Feito!
def STY_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    cpu.writeMemory(address, cpu.registers_y)
    cpu.registers_pc += size
    return nCycles


# Feito!
def TAX_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_x = value
    cpu.registers_pc += size
    return nCycles


# Feito!
def TAY_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_a
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_y = value
    cpu.registers_pc += size
    return nCycles


# Feito!
def TSX_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_sp
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_x = value
    cpu.registers_pc += size
    return nCycles


# Feito!
def TXA_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_x
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_a = value
    cpu.registers_pc += size
    return nCycles


# Feito!
def TXS_Implied(cpu):
    size = 1
    nCycles = 2

    cpu.registers_sp = cpu.registers_x
    cpu.registers_pc += size
    return nCycles


# Feito!
def TYA_Implied(cpu):
    size = 1
    nCycles = 2

    value = cpu.registers_y
    setN(cpu, value)
    setZ(cpu, value)
    cpu.registers_a = value
    cpu.registers_pc += size
    return nCycles


# Unofficial Opcodes
def DCP_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DCP_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    value = (value - 1) & 0xFF
    cpu.writeMemory(address, value)
    value = cpu.registers_a - value
    cpu.registers_pc += size
    setC(cpu, ~value >> 8 & 0x1)
    setN(cpu, value)
    setZ(cpu, value & 0xFF)

    return nCycles


def DOP_Immediate(cpu):
    size = 2
    nCycles = 2

    cpu.registers_pc += size
    return nCycles


def DOP_Zero(cpu):
    size = 2
    nCycles = 3

    cpu.registers_pc += size
    return nCycles


def DOP_Zero_X(cpu):
    size = 2
    nCycles = 4

    cpu.registers_pc += size
    return nCycles


def ISB_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def ISB_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    value = (value + 1) & 0xFF
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = cpu.registers_a - value - (1 - carry)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    setO(cpu, (((cpu.registers_a ^ tmp) & 0x80) != 0 and ((cpu.registers_a ^ value) & 0x80) != 0))
    setC(cpu, 0 if tmp < 0 else 1)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def LAX_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def LAX_Zero_Y(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def LAX_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def LAX_Absolute_Y(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def LAX_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def LAX_Indirect_Y(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    cpu.registers_a = value
    cpu.registers_x = value
    cpu.registers_pc += size
    setN(cpu, value)
    setZ(cpu, value)

    return nCycles


def RLA_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RLA_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    setC(cpu, (value >> 7) & 1)
    value = ((value << 1) & 0xFF) + carry
    cpu.registers_a &= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)
    cpu.writeMemory(address, value)

    return nCycles


def RRA_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def RRA_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    carry = (cpu.getStatus(cpu.statusFlags['c']) << 7)
    setC(cpu, value & 0x01)
    value = (value >> 1) | carry
    cpu.writeMemory(address, value)
    carry = cpu.getStatus(cpu.statusFlags['c'])
    tmp = value + cpu.registers_a + carry
    setO(cpu, not (((cpu.registers_a ^ value) & 0x80) != 0) and (((cpu.registers_a ^ tmp) & 0x80)))
    setC(cpu, tmp > 0xFF)
    setN(cpu, tmp)
    setZ(cpu, tmp & 0xFF)
    cpu.registers_a = (tmp & 0xFF)
    cpu.registers_pc += size

    return nCycles


def SAX_Zero(cpu):
    size = 2
    nCycles = 3

    address = addressingMode.Zero(cpu)
    value = cpu.registers_x & cpu.registers_a
    cpu.writeMemory(address, value)
    cpu.registers_pc += size

    return nCycles


def SAX_Zero_Y(cpu):
    size = 2
    nCycles = 4

    address = addressingMode.Zero_Y(cpu)
    value = cpu.registers_x & cpu.registers_a
    cpu.writeMemory(address, value)
    cpu.registers_pc += size

    return nCycles


def SAX_Absolute(cpu):
    size = 3
    nCycles = 4

    address = addressingMode.Absolute(cpu)
    value = cpu.registers_x & cpu.registers_a
    cpu.writeMemory(address, value)
    cpu.registers_pc += size

    return nCycles


def SAX_Indirect_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Indirect_X(cpu)
    value = cpu.registers_x & cpu.registers_a
    cpu.writeMemory(address, value)
    cpu.registers_pc += size

    return nCycles


def SLO_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SLO_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x80)
    value <<= 1
    value &= 0xFF
    cpu.writeMemory(address, value)
    cpu.registers_a |= value
    cpu.registers_pc += size
    setN(cpu, cpu.registers_a)
    setZ(cpu, cpu.registers_a)

    return nCycles


def SRE_Zero(cpu):
    size = 2
    nCycles = 5

    address = addressingMode.Zero(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Zero_X(cpu):
    size = 2
    nCycles = 6

    address = addressingMode.Zero_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Absolute(cpu):
    size = 3
    nCycles = 6

    address = addressingMode.Absolute(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Absolute_X(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Absolute_Y(cpu):
    size = 3
    nCycles = 7

    address = addressingMode.Absolute_Y(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Indirect_X(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_X(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def SRE_Indirect_Y(cpu):
    size = 2
    nCycles = 8

    address = addressingMode.Indirect_Y(cpu)
    value = cpu.readMemory(address)
    setC(cpu, value & 0x01)
    value >>= 1
    cpu.registers_a ^= value
    cpu.writeMemory(address, value)
    cpu.registers_pc += size
    setZ(cpu, cpu.registers_a)
    setN(cpu, cpu.registers_a)

    return nCycles


def TOP_Absolute(cpu):
    size = 3
    nCycles = 4

    cpu.registers_pc += size
    return nCycles


def TOP_Absolute_X(cpu):
    size = 3
    nCycles = 4

    cpu.registers_pc += size
    return nCycles
