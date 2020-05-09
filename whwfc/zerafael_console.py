from zerafael_romloader import romLoader
from zerafael_cpu import cpu
import sys


class Console:

    def __init__(self):
        romPath = 'nestest.nes'

        self.cartridge = romLoader(romPath)
        self.cartridge.load()

        CPU = cpu(self.cartridge)
        CPU.run()


Console()
