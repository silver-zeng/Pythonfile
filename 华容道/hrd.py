import pygame
pygame.init() # 初始化pygame
windowwidth = 640 # 窗口宽度
windowheight = 480 # 窗口高度
basicfontsize = 20 #字体大小
 # R G B
black = (0, 0, 0)
white = (255, 255, 255)
brightblue = (0, 50, 255)
darkturquoise = (10, 100, 150)
green = (0, 200, 0)
 # 首颗棋子的左上角坐标
 # x = 100
# y = 100
tilesize = 80 # 每颗棋子的大小
# 棋盘几行几列
boardwidth = 4 # 四行
boardheight = 4 # 四列
# 首颗棋子棋子位置算不出来，就可以手动设置数字（x = 158,y = 78）
xmargin = int((windowwidth -(tilesize * boardwidth + (boardwidth - 1))) / 2)
ymargin = int((windowheight -(tilesize * boardheight + (boardheight - 1))) / 2)
print(xmargin,ymargin)
def main():
    global displaysurf,basicfont
    pygame.display.set_caption('Slide Puzzle') # 设置窗口标题
 # 字体
    basicfont = pygame.font.Font('freesansbold.ttf', basicfontsize)
# 创建窗口，利用元组进行窗口大小的设置 注意有两个括号
    displaysurf = pygame.display.set_mode((windowwidth, windowheight))
# 获取一下初始状态
    board = getStartingBoard()
    drawBoard(board)
 # 调用函数写字
    makeText('Reset', white, green,windowwidth - 120, windowheight - 90)
    makeText('New Game', white, green,windowwidth - 120, windowheight - 60)
# 调用函数画棋子,考虑不在main里面调用
# drawTile("2",0,1)
    while True: # 死循环确保窗口一直显示
        pygame.time.wait(99999999) # 程序暂停一段时间后继续，可以防卡顿
# 思考：为什么要把board作为参数，为什么要带着drawBoard进行棋子绘制？
def drawBoard(board):
    displaysurf.fill(darkturquoise) # 填充背景颜色
# 要分清楚for循环中的循环变量是什么意思
    for y in range(boardheight): # 循环范围根据行数和列数变化
        for x in range(boardwidth):
            print(x,y)
            if board[y][x] != None: # 如果对应位置不为空，才要画棋子
                drawTile(str(board[y][x]), y,x)
    pygame.display.flip() # 刷新界面
# 写字需要设置的内容
 # 文字内容（字符串）
# 文字位置（原点，坐标轴正方向，单位长度），位置的坐标一般是文字左上角，坐标用元组表示
# 颜色
# 字体 pygame支持很多字体，要求字体的文件类型是.ttf
# 写字的函数
def makeText(text, color, bgcolor, x, y):
# 写字的内容 # 字的背景颜色可以不设置，就是默认透明的
    textSurf = basicfont.render(text,True , color, bgcolor)
# 写字的位置
    displaysurf.blit(textSurf, (x, y))
    pygame.display.update() # 局部刷新
# 画棋子
# 矩形 上面有字，字是数字
# 画矩形格式
# pygame.draw.rect(窗口, 颜色, ( top, left, width, height))
# 参数 根据什么信息来画棋子（棋子上的字，棋子在棋盘上的位置）
def drawTile(text,ty,tx):
    zuobiao = getLeftTopOfTile(tx,ty) # 根据棋子在棋盘上的位置决定左上角坐标
# 先画正方形再写字，否则字会被覆盖
    pygame.draw.rect(displaysurf,green,(zuobiao[0],zuobiao[1],tilesize,tilesize))
# 先写1 方便后面for循环来改文字内容
    textSurf = basicfont.render(text,True , white, green)
    textRect = textSurf.get_rect()
# print(textRect)
# 一大把计算题，计算怎样才能让数字在棋子的中间,center 是中间的坐标（类似属性）
    textRect.center = (xmargin + int(tilesize/2) + tx * 81,
    ymargin + int(tilesize/2) + ty * 81)
# print(a)
# print(textRect.center)
# print(textRect)
    displaysurf.blit(textSurf, textRect )
    pygame.display.flip()
# 单独获取某一颗棋子的左上角坐标
 # li = [[1,2,3,4],
# [5,6,7,8],
 # [9,10,11,12],
# [13,14,15,None]]
 # 1 的索引是[0][0]
 # 2 的索引是[0][1]
# 具体变化多少可以根据索引确认，x根据第二个索引变，y根据第一个索引变
 # tx 和 ty分别表示棋子在棋盘上的位置
def getLeftTopOfTile(tx,ty):
# 初始坐标+（棋盘坐标*棋子大小）+ （缝隙） 可以删除缝隙看效果
    x = xmargin + (tx * tilesize) + (tx -1)
    y = ymargin + (ty * tilesize) + (ty -1)
    return (x,y) # 返回值为元组，那坐标就可以直接用返回值
# 准备棋盘开始的状态
def getStartingBoard():
    c = 1
    board = []
    # 可以试下单纯的创建一个双重列表
    for y in range(boardheight):
        col = [] # 小列表最开始也是空的
        for x in range(boardwidth):
            col.append(c)
            c = c + 1
        board.append(col)
    board[boardheight-1][boardwidth - 1] = None
    print(board)
    return board
# getStartingBoard()
if __name__ == '__main__':
    main()