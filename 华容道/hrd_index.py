import pygame
windowwidth = 640    # 设置窗口宽度
windowhigh = 500     # 设置窗口高度
color1 = "white" # 设置背景颜色   也可以使用color1=(255,255,255)    0-255之间的数值调制颜色
color2 = (135,206,235)  # 天蓝色
zt_color = (56,94,15)  # 字体颜色
zt_bg_color=(255,125,64)  # 字体背景颜色
qz_color = (255,255,0)  # 棋子颜色
qz_bk_color = (11,23,70)  # 棋子边框颜色
zt_size = 20  # 字体大小
zt_format = "freesansbold.ttf"  #  字体格式，要求文件类型是.ttf
qizi_width = 80  #  棋子宽
qizi_length = 80  #  棋子长
qizi_hang = 4  # 棋盘行数
qizi_lie = 4  # 棋盘列数

def main():
    global chuangkou,basicFont  # chuangkou变量全局化
    pygame.init()  # 初始化pygame使用初始数据，以免未对数据进行初始化报错
    chuangkou = pygame.display.set_mode((windowwidth, windowwidth))   # 创建窗口，利用元祖进行窗口大小设置
    pygame.display.set_caption("zfy-华容道")  # 设置窗口标题
    drawBoard(color2) # 调用设置背景颜色的函数
    basicFont = pygame.font.Font(zt_format, zt_size)  # 设置字体格式对象，相当于一个字体格式，以后写的字的字体和大小都一致，字体的初始化
    writeTxt("Reset",zt_color,zt_bg_color,500,500) # 把reset写出展示在窗口上
    writeTxt("Newgame",zt_color,zt_bg_color,500,550)
    writeTxt("Come and play, pretty boy", zt_color, zt_bg_color,10,20)
    pygame.draw.rect(chuangkou,zt_bg_color,(100,100,400,400),10)   # 绘制矩形draw.rect(窗口对象，颜色，位置，宽度)
    pygame.display.update()  # 局部刷新一下
    while True:
        pygame.time.wait(99999)

def drawBoard(color):  # 设置背景颜色的函数
    chuangkou.fill(color)  # 用fill（）设置背景颜色
    pygame.display.flip()  # 刷新界面


def writeTxt(text,color,bgcolor,x,y):   # 写字需要设置的内容  文字内容（字符串）；文字位置（原点为左上角，坐标方向，单位长度）   坐标用元祖表示
    writetext=basicFont.render(text,True,color,bgcolor)  # 设置字体是否原滑，字体的颜色，字体背景颜色
    chuangkou.blit(writetext,(x,y))  # 将字体展示在窗口上,并且设置坐标
    pygame.display.update()  # 写字后需要用update刷新，是局部刷新，与背景颜色flip()刷新不一样

def qizi_num():
    lis=[]
    a=1
    for a in range(int(qizi_lie)):

        for a in range(int(qizi_hang)):
            if a <= int(qizi_hang):
                lis.append(a)
                a += 1
        lis.append(a)
    return lis
a = qizi_num()
print(a)

if __name__ == "__main__":
    main()