from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待  WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(元素xpath),message="报错信息")
from selenium.webdriver.common.keys import Keys # 处理键盘事件的类
from selenium.webdriver.support import expected_conditions as EC   #显示等待条件
from random import randint # 导入随机函数
import time
import csv

def main():
    start(r"https://test.yiscs.cn/index")  # 门户地址
    drivers.find_element(By.XPATH, r'/html/body/div/div/div/div[1]/div/nav/div[3]/div/div').click()  # 点击登录
    time.sleep(1)
    drivers.find_element(By.XPATH, "//form/div[1]/div/div[1]/input").send_keys(
        "18707994417")  # 输入用户名
    drivers.find_element(By.XPATH, "//form/div[2]/div/div/input").send_keys(
        "1")  # 输入验证码
    drivers.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/button").click()  # 点击登录
    time.sleep(1)
    drivers.find_element(By.XPATH, r'//*[@id="app"]/div/div/div[1]/div/nav/div[2]/div[2]').click()  # 点击产品中心
    time.sleep(1)
    drivers.find_element(By.XPATH, r'//*[@id="app"]/div/div/section/div/nav/div/div[2]/div[2]/div[1]').click()  # 点击煤炭业务
    time.sleep(1)
    drivers.find_element(By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/button').click()  # d 点击电厂项目申请
    # 解析测试数据文档
    date=read_csv('D:\Pythonfile\yrt_auto\自动化测试.csv')
    print("文件数据：",date)
    # wd是webdriver对象，5是最长等待时间，0.5是每0.5秒去查询对应的元素。until后面跟的等待具体条件，EC是判断条件，检查元素是否存在于页面的 DOM 上。
    xm_name=(By.XPATH, "//form/div[2]/div[1]/div/div/div/input")  # 项目名称元素
    WebDriverWait(drivers, 5, 0.5).until(EC.presence_of_element_located(xm_name),message="元素没有定位到")  # 隐式等待

    # 录入项目准入数据
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/input').send_keys(date[0][1]+str(get_time())) # 输入项目名称+当前时间
    time.sleep(1)
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input').send_keys(date[1][1])  # 输入购买方
    time.sleep(2)
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input').send_keys(Keys.DOWN)  # 输入购买方后，向下选择值,模拟键盘操作
    time.sleep(2)
    drivers.find_element(By.XPATH, '//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input').send_keys(Keys.ENTER) #  模拟选择后按下回车
    drivers.find_element(By.XPATH,'/html/body/div[1]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/input').send_keys(date[2][1])  # 输入终端交货周期
    time.sleep(2)
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[4]/div/div/div/div/input').click() # 触发物流选择列表
    time.sleep(2)
    wl_way=date[3][1]
    #  选择物流方式
    wl_ele=drivers.find_element(By.XPATH,'//form/div[2]/div[4]/div/div/div/div/input')
    if wl_way=='汽车-直达':
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.ENTER)
    elif wl_way=='火车-直达':
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.ENTER)
    elif wl_way=='火车转汽车直达':
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.ENTER)
    else:
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.DOWN)
        wl_ele.send_keys(Keys.ENTER)

    time.sleep(1)
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[5]/div/div/div/textarea').send_keys(date[4][1])  # 输入违约责任
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[3]/div[1]/div[2]/div[1]/div/div/div[1]/div/input').click()  # 触发企业主体选择列表
    sq_qy=date[5][1]  # 赋值申请企业
    time.sleep(2)
    drivers.find_element(By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[text()='+"'"+sq_qy+"'"+']').click()  # 选择申请企业
    bank_button='//input[@placeholder="请先选择企业主体再做选择"]'
    drivers.find_element(By.XPATH,bank_button).click() # 触发账户选择列表
    time.sleep(1)
    drivers.find_element(By.XPATH,bank_button).send_keys(Keys.DOWN) # 默认选择第一个账户
    drivers.find_element(By.XPATH, bank_button).send_keys(Keys.ENTER) # 按下回车
    drivers.find_element(By.XPATH,'//div[@class="el-col el-col-10"]/div[1]/div[1]/div[1]/input[@type="text" and @maxlength="25"]').send_keys(date[6][1]) # 输入实控人项姓名
    drivers.find_element(By.XPATH,'//form/div[4]/div[1]/div/div[2]/div/div/div/input').send_keys(date[7][1]) # 输入实控人电话
    drivers.find_element(By.XPATH,'//form/div[5]/div[1]/div/div/div/div/div[1]/input').send_keys(r"C:\Users\59872\Desktop\工作数据\发票.png")  # 上传项目实控人证件
    drivers.find_element(By.XPATH,'//form/div[5]/div[2]/div/div/div/div/div[1]/input').send_keys(r"C:\Users\59872\Desktop\工作数据\范家云.png") # 上传项目实控人征信
    drivers.find_element(By.XPATH, '//form/div[5]/div[3]/div/div/div/div/div[1]/input').send_keys(r"C:\Users\59872\Desktop\工作数据\锦邦国际物流有限公司.jpg")  # 上传项目材料
    drivers.find_element(By.XPATH, '//form/div[6]/div[1]/div/div/div/div/div[1]/input').send_keys(r"C:\Users\59872\Desktop\工作数据\范家云.png")  # 上传投标信息
    time.sleep(5)
    # 下一步后的操作
    drivers.find_element(By.XPATH,'//div[@class="flex justify-center mt-10"]/button[2]').click() # 点击下一步
    time.sleep(1)
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/input').send_keys(date[8][1]) # 收货方输入企业名称
    time.sleep(2)
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/input').send_keys(Keys.DOWN)  # 按方向键向下，确认选择
    time.sleep(1)
    drivers.find_element(By.XPATH, '//form/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/input').send_keys(Keys.ENTER) # 按回车，确认选择
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div/div[1]/input').send_keys(date[9][1]) # 输入收货地址
    drivers.find_element(By.XPATH,'//form/div[3]/div[1]/div/div/div/input').send_keys(randint(2000,5000))  # 2000-5000内随机输入结算数量
    drivers.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div/input').send_keys(1000) # 输入结算单价
    drivers.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/div[1]/input').click() # 触发结算方式下拉列表
    time.sleep(1)
    # 输入结算方式
    js_way=date[10][1]
    js_ele=drivers.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/div[1]/input')
    if js_way=='一票制':
        js_ele.send_keys(Keys.DOWN)
        js_ele.send_keys(Keys.ENTER)
    else:
        js_ele.send_keys(Keys.DOWN)
        js_ele.send_keys(Keys.DOWN)
        js_ele.send_keys(Keys.ENTER)

    time.sleep(1)
    drivers.find_element(By.XPATH,'//div[2]/form/div[4]/div[3]/div/div/div[1]/input').send_keys(randint(1,30)) # 随机输入结算周期1-30
    drivers.find_element(By.XPATH,'//form/div[4]/div[4]/div/div/div/div[1]/div/div[1]/div/div/div/div/input').click() # 触发结算节点选择列表
    time.sleep(3)

    jsjd_way=date[11][1]
    jsjd_ele=drivers.find_element(By.XPATH,'//form/div[4]/div[4]/div/div/div/div[1]/div/div[1]/div/div/div/div/input')
    if jsjd_way=='见结算单结算':
        jsjd_ele.send_keys(Keys.UP)
        jsjd_ele.send_keys(Keys.UP)
        jsjd_ele.send_keys(Keys.UP)
        jsjd_ele.send_keys(Keys.ENTER)
    else:
        jsjd_ele.send_keys(Keys.UP)
        jsjd_ele.send_keys(Keys.ENTER)

    drivers.find_element(By.XPATH,"//input[@placeholder='请输入结算比例,总结算比例之和不能超过100']").send_keys(100) # 输入结算比例
    time.sleep(2)
    drivers.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div[3]/div[3]/button[3]').click() # 点击下一步
    # 供应商信息输入
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/input').send_keys(date[12][1]) # 输入供应商企业
    time.sleep(2)
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/input').send_keys(Keys.DOWN) # 选择供应商企业
    time.sleep(1)
    drivers.find_element(By.XPATH, '//form/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/input').send_keys(Keys.ENTER)  # 选择供应商企业
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div[2]/div/div/div[1]/input').send_keys(randint(500,1000)) # 随机输入采购单价
    drivers.find_element(By.XPATH,'//form/div[2]/div[1]/div/div[3]/div/div/div[1]/input').send_keys(date[13][1]) # 输入发货地点
    # 供应商结算信息
    drivers.find_element(By.XPATH,'//form/div[3]/div[2]/div/div/div[1]/div[2]/input').click() # 触发付款方式选择列表
    time.sleep(3)
    fkfs=date[14][1]  # 付款方式赋值
    # 选择付款方式
    fkfs_element=drivers.find_element(By.XPATH, '//form/div[3]/div[2]/div/div/div[1]/div[2]/input') # 付款方式选择列表元素
    if fkfs=='预付':
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.ENTER)
    elif fkfs=='货到站台付款':
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.ENTER)
    elif fkfs=='货到买方指定地点付款':
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.DOWN)
        fkfs_element.send_keys(Keys.ENTER)

    drivers.find_element(By.XPATH, '//form/div[3]/div[3]/div/div/div/div[1]/input').click() # 触发交货方式选择
    time.sleep(1)
    jhfs_element=drivers.find_element(By.XPATH, '//form/div[3]/div[3]/div/div/div/div[1]/input')
    jhfs=date[15][1]
    # 选择交货方式
    if jhfs == '汽车-直达':
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.ENTER)
    elif jhfs == '火车-直达':
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.ENTER)
    elif jhfs == '火车转汽车直达':
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.ENTER)
    else:
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.DOWN)
        jhfs_element.send_keys(Keys.ENTER)

    drivers.find_element(By.XPATH,'//form/div[3]/div[4]/div/div/div/input').send_keys(randint(1,10)) # 随机输入付款频次
    # 货品规格
    drivers.find_element(By.XPATH,'//form/div[4]/div[2]/div/div/div/input').send_keys(randint(4500,5400)) # 随机输入热值
    drivers.find_element(By.XPATH, '//div[1]/form/div[4]/div[3]/div/div/div/input').send_keys(randint(1, 10))  # 随机输入含硫量
    drivers.find_element(By.XPATH, '//form/div[4]/div[4]/div/div/div/input').send_keys(randint(1, 10))  # 随机输入含水分
    drivers.find_element(By.XPATH, '//form/div[4]/div[5]/div/div/div/input').send_keys(randint(1, 10))  # 随机输入挥发分

    drivers.find_element(By.XPATH,'//div[4]/div[2]/button[1] ').click() # 点击暂存按钮
    time.sleep(30)
    
def start(url): # 启动浏览器
    global drivers
    drivers=webdriver.Chrome()
    drivers.get(url)
    drivers.maximize_window()
def get_time(): # 获取当前时间yyyy-mm-dd-hhmmss

    localtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) # 以time.strftime()格式化时间
    return localtime

def read_csv(fileurl):  # 打开csv文件读取数据
    with open(fileurl,"r") as file:   # 注意不能加, encoding='UTF-8'，因为报错了，解码搞不出！！！
        data = csv.reader(file)
        # 遍历数据data，一行一行的展示出来
        #     for row in data:
        #         print(row)
        # 一个空列表，把文件中的数据data放入列表中，除了第一行标题
        list = []
        i = 0  # 从0开始for循环计数
        for row in data:
            if i == 0:
                pass  # pass表示什么也不做
            else:
                list.append(row)  # append在列表的尾部添加元素
            i = i + 1
            # print(list)
    return list  # 列表比data少一行

if __name__ == '__main__':
    main()

