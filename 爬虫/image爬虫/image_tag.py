import requests
import re
from bs4 import BeautifulSoup
def main():
    url='https://image.baidu.com/search/albumsdetail?tn=albumsdetail&word=%E8%9B%8B%E7%B3%95&fr=albumslist&album_tab=%E4%BA%BA%E7%89%A9&album_id=45&rn=30'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie':'BIDUPSID=D35648476D4B34E73C96CEEE49CCD95B; PSTM=1677477886; BAIDUID=D35648476D4B34E72F3827E2A474125F:FG=1; indexPageSugList=%5B%22%E8%90%A5%E4%B8%9A%E6%89%A7%E7%85%A7%22%2C%22%E8%90%A5%E4%B8%9A%E6%89%A7%E7%85%A7PDF%22%2C%22%E5%A3%81%E7%BA%B8%22%2C%224k%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%94%B5%E8%84%91%E5%A3%81%E7%BA%B8%20%E6%A1%8C%E9%9D%A2%22%2C%224k%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%BB%BF%E5%B7%A8%E4%BA%BA%22%2C%22%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%E7%BB%BF%E5%B7%A8%E4%BA%BA%22%2C%22%E5%A3%81%E7%BA%B8%E9%AB%98%E6%B8%85%22%2C%224k%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8%20%E6%97%A0%E6%8D%9F%22%2C%224k%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8%E5%8A%A8%E6%BC%AB%22%5D; BAIDUID_BFESS=D35648476D4B34E72F3827E2A474125F:FG=1; ZFY=iMETVza3gFLTKjnylVHalVxFNm2EfS3lIqcu6:Am3jaQ:C; BA_HECTOR=0hahag20048h818h258k212j1i961m51p; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[bPTzwF-RsLY]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; H_PS_PSSID=38516_36549_38687_38881_38797_38903_38832_38582_38820_38824_38637_26350_38567; ab_sr=1.0.1_MTZlNjkzNDU4MzNkNDhlNjJkZDhhMzhmNDQwZDFiYzRlMTI3MjUyNjBhOGUzYjU5NDEyMDM0OGY3NWFiNTIxZTg3N2Y0MWRjOTNkMDU4OTI2NTAwOGZiN2IxOWNhNWMzYjc0NWU2YTkwZjhlNjg2YzFhYmViN2Q3NDVmNTVjNDFmNjU4ZGNkMTBiYTI0NDc2OTEzZTI3ODQxNjFmYmMyZQ==; BDRCVFR[0_FPWPLXdzb]=mk3SLVN4HKm; BDRCVFR[Q5XHKaSBNfR]=mk3SLVN4HKm; userFrom=null',
    }
    res=requests.get(url,headers=header)
    soup=BeautifulSoup(res.text,'html.parser')  # 缩进格式
    image_tags = soup.find_all('img') # 获取页面所有img标签
    # image_url = re.findall('<img class="albumsdetail-item-img" src="(.*?)"',res.text)
    num=1
    for image in image_tags:
        image_url=image['src']  # 获取src属性
        print(image_url)
        with open("download/{}.jpeg".format(num), 'wb') as f:
            f.write(image.content)
            num += 1
    # num=1
    # for i in image_url:
    #     image=requests.get(i)
    #     with open("download/{}.jpeg".format(num),'wb') as f:
    #         f.write(image.content)
    #         num += 1

if __name__ == '__main__':
    main()
