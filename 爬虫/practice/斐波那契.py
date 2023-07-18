# def fb(): # 生成斐波那契数列 [0,1,1,2,3,5,8......]
#     a=0
#     b=1
#     yield a
#     while a<80:
#         c=b
#         b=a+b
#         a=c
#         yield a
#         #a,b=b,a+b  #与上述赋值等同
# lis = fb()
# list = []
# try:
#
#     while True:
#         list.append(next(lis))
# except:
#     pass
# print(list)
# li = [1,2,3,2,1,3,4,5,6,6,7,8,9,8,7,6,5,4]
# res=0
# for i in range(18):
#     res=li[i]+res
# print(res)
# li = [1,2,3,2,1,3,4,5,6,6,7,8,9,8,7,6,5,4]
# index=0
# re=0
# while index<18:
#     num=li[index]
#     index += 1
#     re=re + num
# print(re)
#在数学中n边形的内角和为(n-2)*180，其中n>2。
# 在控制台输入两次多边形的边数，并通过函数计算这两个多边形的内角和
# def hsjs(num):
#     if num<=2:
#         print("变数需要大于2！")
#     else:
#         res=(num-2)*180
#     return res
# i=0
# while i<2:
#     num=int(input("请输入边数："))
#     hsjs(num)
#     i+=1
#     print(f"内角之和是{hsjs(num)}")

"""
4.创建一个人类（human），要求如下：（20分）
    2个属性：身高（height），单位m；体重（weight），单位kg
    1个方法：BMI() 用于判断一个人的体重是否健康
     计算公式为：
体重除以身高的平方，得到的结果即为bmi指数
判断依据为：
低于18.5偏瘦；18.5-23.9正常；23.9-27偏胖；超过27则过胖
 BMI的计算示例：
身高为1.8m，体重为75kg，计算后bmi指数为23.1481，正常
"""
class human():
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight

    def BMI(self):
        BMI=self.weight/self.height**2
        return BMI
h1=human(float(input("请输入身高，单位m：")),float(input("请输入体重，单位kg：")))
BMI=h1.BMI()
if BMI < 18.5:
    print("这个人啊偏瘦，BMI值为%.2f"%BMI)
elif 18.5 <= BMI < 23.9:
    print(f"这个人啊健康的很，BMI值为{BMI}，点个赞")
elif 23.9 <= BMI < 27:
    print(f"大兄弟啊偏胖了，BMI值为{BMI}")
else:
    print(f"大兄弟过于肥胖了，BMI值为{BMI}，再不健身就废了~~")
