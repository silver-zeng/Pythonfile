import re
#变量名有数字字母下划线组成
#变量名不能由纯数字组成，也不能由数字开头
str=input("请输入变量名：")
blm=re.findall("^[a-zA-Z_]\w+$",str)
if blm:
    print("{}是有效变量名".format(str))
else:
    print("{}变量名无效".format(str))
print(blm)


