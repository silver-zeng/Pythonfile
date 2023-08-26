import os

import requests,re
url='https://image.baidu.com/search/albumsdata?pn=30&rn=30&tn=albumsdetail&word=%E8%9B%8B%E7%B3%95&album_tab=%E4%BA%BA%E7%89%A9&album_id=45&ic=0&curPageNum=1'
header={
    'Cookie':'winWH=%5E6_1646x878; BDIMGISLOGIN=0; BDqhfp=%E9%9D%93%E5%A5%B3%E5%9B%BE%E7%89%87%26%26NaN-1undefined%26%260%26%261; BIDUPSID=D35648476D4B34E73C96CEEE49CCD95B; PSTM=1677477886; BAIDUID=D35648476D4B34E72F3827E2A474125F:FG=1; BAIDUID_BFESS=D35648476D4B34E72F3827E2A474125F:FG=1; ZFY=iMETVza3gFLTKjnylVHalVxFNm2EfS3lIqcu6:Am3jaQ:C; BA_HECTOR=0hahag20048h818h258k212j1i961m51p; BDRCVFR[bPTzwF-RsLY]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; H_PS_PSSID=38516_36549_38687_38881_38797_38903_38832_38582_38820_38824_38637_26350_38567; BDRCVFR[0_FPWPLXdzb]=mk3SLVN4HKm; BDRCVFR[Q5XHKaSBNfR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; PSINO=3; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; indexPageSugList=%5B%22%E7%BE%8E%E5%A5%B3%22%2C%22%E8%90%A5%E4%B8%9A%E6%89%A7%E7%85%A7%22%2C%22%E8%90%A5%E4%B8%9A%E6%89%A7%E7%85%A7PDF%22%2C%22%E5%A3%81%E7%BA%B8%22%2C%224k%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%94%B5%E8%84%91%E5%A3%81%E7%BA%B8%20%E6%A1%8C%E9%9D%A2%22%2C%224k%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%BB%BF%E5%B7%A8%E4%BA%BA%22%2C%22%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%BB%BF%E5%B7%A8%E4%BA%BA%22%2C%22%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%22%2C%224k%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8%20%E6%97%A0%E6%8D%9F%22%5D; cleanHistoryStatus=0; BDRCVFR[Txj84yDU4nc]=mk3SLVN4HKm; userFrom=www.baidu.com; ab_sr=1.0.1_N2JhZWEwNWIyMzRjZTllZjJkMGM0N2ViZmU2MmEzYmJjYjY2ZDg1ODBhOGQwY2I1ZDhjOTNkNmQ0NDRhMGU5MDcwNTM5NmUzMWE5MDUzNWNhY2JiYzQzOTM1MTVkYWM0ZTlkMmNiOGNlZTA5Njc0NmVlODQyOTIwNjM3NTkyMDIyNmMyZjc1ZmY4OWM1ZWFmNjRjMDZhNDQ3NTQ0MWZmMw==',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
res = requests.get(url,headers=header)
img_list=re.findall('"thumbnailUrl":"(.*?)"',res.text) # 获取脏的图片地址的列表
print(img_list,type(img_list))
num=0
for i in img_list:
    img_url=str(i).replace('\\','')  #将脏的图片url处理
    img=requests.get(img_url) # 发送图片请求
    path = "./image/"

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created.")
    with open('image/{}.jpeg'.format(num),'wb') as f:
        f.write(img.content)
        num+=1
print("图片爬取完成")