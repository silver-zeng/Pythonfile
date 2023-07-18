import requests,re


url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B2%E5%BB%AD%B1%DA%D6%BD&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDQsMSw2LDUsMiw3LDgsOQ%3D%3D'
# 构建请求头信息au

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'Cookie': 'BDqhfp=%E6%8F%92%E7%94%BB%E5%A3%81%E7%BA%B8%26%26NaN-1undefined%26%26612%26%262; BIDUPSID=F70BC69731ED1CE0911F71A1EBB1F795; PSTM=1685607184; BAIDUID=F70BC69731ED1CE06CF706BFECA7A04D:FG=1; newlogin=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-158%3A; BDUSS=khCOUlSZ01kanZmSHA1RW1neEp1eW1abFJ2d3VoTkZHZWpuNkxEVHB0VlE1TFJrSVFBQUFBJCQAAAAAAAAAAAEAAACiGDB9yq7B99K2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFBXjWRQV41kS; BDUSS_BFESS=khCOUlSZ01kanZmSHA1RW1neEp1eW1abFJ2d3VoTkZHZWpuNkxEVHB0VlE1TFJrSVFBQUFBJCQAAAAAAAAAAAEAAACiGDB9yq7B99K2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFBXjWRQV41kS; indexPageSugList=%5B%22%E4%BD%A0%E4%BB%A5%E4%B8%BA%E6%9C%89%E9%92%B1%E4%BA%BA%E5%B0%B1%E4%BC%9A%E5%83%8F%E4%BD%A0%E6%83%B3%E8%B1%A1%E4%B8%AD%22%2C%22%E6%9C%89%E9%92%B1%E4%BA%BA%E5%B9%B6%E6%B2%A1%E6%9C%89%E4%BD%A0%E6%83%B3%E8%B1%A1%E7%9A%84%E5%BF%AB%E4%B9%90%22%2C%22%E6%9C%89%E9%92%B1%E4%BA%BA%E7%9A%84%E5%BF%AB%E4%B9%90%22%2C%22%E7%BE%8E%E5%A5%B3%22%2C%22github%22%2C%22echarts%E5%9B%BE%E6%A0%87%22%2C%22pyecharts%E5%9B%BE%E6%A0%87%22%2C%22pyyecharts%E5%9B%BE%E6%A0%87%22%2C%22plotly%E5%9B%BE%E6%A0%87%22%5D; ZFY=fxwkuNve:BJ0KbGc7rqz7jcfRkcnq0nRK0RZK8YDo:BVU:C; BAIDUID_BFESS=F70BC69731ED1CE06CF706BFECA7A04D:FG=1; BA_HECTOR=800ga58g2l85ah8g0g8g2gae1i937hq1p; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_MWI1NDE3NTBjMzgzMDI2MTkwYWIwNzEwYTMzZDYyNzFkMmNjMTk4NmZmYjA0NjQwZjIyZjY4YzczMzAwMmExYzc5OGY5MTI2ZWNmZTk4Yjc1NDYxNWRiZjFjZmYyZjdiNjBmNWUwNGFmZGQyNjA4YWExZTVhMTRhZDA0YmMyNzg0NjIzMjRhODdlMTk4MjUxMDFkMzZjMjg5NTFlM2FiOQ==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; H_PS_PSSID=38516_36543_38687_38878_38903_38832_38816_38838_38638_26350_38571; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0',
}
# 使用requests的get去请求url,使用headers做伪装
res = requests.get(url, headers=headers)
# 如果res能够出来我们想要的数据---证明伪装成功
# print(res.text)# 字符串

img_url_list = re.findall('"thumbURL":"(.+?)"', res.text)
#
# print(img_url_list)

# num = 0
# for i in img_url_list:
#     img_data = requests.get(i)
#     with open(str(num)+'.jpg', 'wb') as f:
#         f.write(img_data.content)
#         num +=1


for i in range(1,3):  # 1,2
    url1 = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10946579064338413468&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E6%8F%92%E7%94%BB%E5%A3%81%E7%BA%B8&cg=wallpaper&queryWord=%E6%8F%92%E7%94%BB%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn={}&rn=30'.format(i*30)
    data = requests.get(url1, headers=headers)
    img_list = re.findall('"thumbURL":"(.+?)"', data.text)
    img_url_list.extend(img_list)


print(img_url_list)
