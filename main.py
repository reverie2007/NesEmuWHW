"""
    nes模拟器
    20200429，就是从今天开始自讨苦吃
"""
import pygame
from pygame.locals import *
from pygame import time
from random import randint


def main():
    # 初始化pygame，为使用硬件做准备
    pygame.init()
    # 创建一个窗口
    screen: pygame.Surface = pygame.display.set_mode((640, 480), 0, 32)

    # 设置窗口标题
    pygame.display.set_caption("hello,world!")
    clock = time.Clock()
    fps = clock.get_fps()

    print(fps)
    fontObj3 = pygame.font.SysFont('宋体', 20)
    rc = [(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(100)]
    rp = [(randint(0, 600), randint(0, 400)) for i in range(100)]
    rr = [randint(0, 200) for i in range(100)]

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出时间后退出程序
                exit()

        # 将背景图画上去
        screen.fill([255, 255, 255])
        for i in range(100):
            pygame.draw.circle(screen, rc[i], rp[i], rr[i])
        fps = clock.get_fps()
        text = fontObj3.render(u'fps=%d' % fps, True, (255, 0, 0), (0, 255, 0))
        screen.blit(text, (200, 10))
        # 刷新画面
        pygame.display.update()
        clock.tick(120)


if __name__ == '__main__':
    main()
