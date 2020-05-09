"""
    nes模拟器
    20200429，就是从今天开始自讨苦吃
"""
import pygame
from pygame import time
from yynescpu import YyNesCpu
from nesloader import NesLoader
import zerafael_joypad as joypad


def main():
    rom_path = 'whwfc/nestest.nes'

    cartridge = NesLoader(rom_path)
    if cartridge.open_success:
        cartridge.chrRomData = cartridge.chr_rom
        cartridge.prgRomData = cartridge.prg_rom
    else:
        print('fail to open nes rom.')
        return

    nes_cpu = YyNesCpu(cartridge)
    # nes_ppu = ppu(nes_cpu, cartridge)

    # 初始化pygame，为使用硬件做准备
    pygame.init()
    # 创建一个窗口
    screen: pygame.Surface = pygame.display.set_mode((256, 240))
    # 设置窗口标题
    pygame.display.set_caption("Yy nes emulator")

    nes_cpu.ppu.set_screen(screen)

    clock = time.Clock()

    font_fps = pygame.font.SysFont('KaiTi', 20)
    # 游戏主循环
    while True:
        # 每帧读取一次输入
        pygame.event.poll()
        joypad.keys = pygame.key.get_pressed()

        if joypad.keys[pygame.K_ESCAPE] == 1:
            exit()
        # 每帧261条扫描线，每条扫描线首先运行cpu固定周期，然后画一条扫描线
        for i in range(261):
            t1 = time.get_ticks()
            nes_cpu.run_cycles(113)
            t2 = time.get_ticks()
            nes_cpu.ppu.do_scan_line()
        t3 = time.get_ticks()
        fps = clock.get_fps()
        text = font_fps.render(u'fps=%d,time:cpu=%d,ppu=%d' % (fps, (t2 - t1), (t3 - t2)), True, (255, 0, 0),
                               (0, 255, 0))
        nes_cpu.ppu.screen.blit(text, (10, 5))

        # 刷新画面
        pygame.display.flip()
        clock.tick(120)


if __name__ == '__main__':
    main()
