from Chaojiying_Python.chaojiying import Chaojiying_Client
from Chaojiying_Python import userinfo

# 超级鹰识别
def img_identify(img_path):
    chaojiying = Chaojiying_Client(username=userinfo.user, password=userinfo.password, soft_id='931146')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(img_path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    resp = chaojiying.PostPic(im, 9103)
    # {'err_no': 0, 'err_str': 'OK', 'pic_id': '2219320570832210076', 'pic_str': '80,110|146,95|222,109', 'md5': '6896edf2ee6d75a59c81b24ce73967f6'}
    # '80,110|146,95|222,109'
    pic_str = resp.get('pic_str') # '80,110|146,95|222,109'
    pic_list = pic_str.split("|")
    return pic_list


img_identify('yy_register.png')