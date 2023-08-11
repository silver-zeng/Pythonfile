import json
import re
import requests     # 发送网络请求
import csv
with open('data2.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_write = csv.DictWriter(f, fieldnames=['股票名称','涨跌幅'])
    csv_write.writeheader()
url='http://webstock.quote.hermes.hexun.com/a/sortlist?block=132&callback=stocklistrequest.sortlistback&commodityid=0&title=15&direction=0&start=0&number=50&input=undefined&time=150400&column=code,name,price,updownrate,LastClose,open,high,low,volume,priceweight,amount,exchangeratio,VibrationRatio,VolumeRatio'
head={
'Cookie': 'ADVC=3b97084ac29986; ADVS=3b97084ac29986; ASL=19413,0000z,af00d630; UM_distinctid=186876159871a8-0ef9b604a81a13-26031951-1fa400-18687615988c39; appToken=pc%2Cother%2Cchrome%2ChxAppSignId2085845532479353.51677308549536%2CPCDUAN; HexunTrack=SID=202302251502291468b228d71285d425dbb2b1d6acfd54348&CITY=0&TOWN=0; Hm_lvt_81ff19c9eb1c05cdfeacb05d2036f066=1677308550; Hm_lpvt_81ff19c9eb1c05cdfeacb05d2036f066=1677308550; hxck_cd_sourceteacher=sR%2FuPcnSSZVIdShwHag3RAnrY9aauRbMjEnRBtq%2FNF1ooDP7obDVPgaQGWxsj76JqbJObjTyc6E6rymEzcaUa3fUcDMqdMsGuffEgU3G%2BVhBefTcTXxHx7nhqqyqiLhNau0r%2BrcvAYk%2Fc2r0fnIB1ShlSMh8Q6%2BTozfIcquQIFk%3D; cn_1263247791_dplus=%7B%22distinct_id%22%3A%20%22186876159871a8-0ef9b604a81a13-26031951-1fa400-18687615988c39%22%2C%22userFirstDate%22%3A%20%2220230225%22%2C%22userID%22%3A%20%220%22%2C%22userName%22%3A%20%22%22%2C%22userType%22%3A%20%22loginuser%22%2C%22userLoginDate%22%3A%20%2220230225%22%2C%22%24_sessionid%22%3A%201%2C%22%24_sessionTime%22%3A%201677308550%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201677308550%2C%22initial_view_time%22%3A%20%221677306101%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DgCsrrmtYGXcLh0LOlmBWm3_jBwZjFw7XIFeva4BtnDa%26wd%3D%26eqid%3Dabdcee67000f20c40000000663f9b282%22%2C%22initial_referrer_domain%22%3A%20%22www.baidu.com%22%2C%22%24recent_outside_referrer%22%3A%20%22www.baidu.com%22%7D; hxck_cd_channel_order_mark1=tKK6EMkJ7JK75WOJ%2FqluxbbMrhZQZtn9if6%2FTggkwv2RHrKyl6CSjVBJW6EtoC6NopfYJ%2BLsfsOFtqO%2ByDPi%2BaxZSljHcxp4ca8bu4Lx8Gu8rreW9NBj6H4kejXQjD8M',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
'Host': 'webstock.quote.hermes.hexun.com',
'Referer': 'http://quote.hexun.com/'
}
res=requests.get(url=url,headers=head)
data=re.findall('"Data":(.*?)}',res.text)[0]
lis=json.loads(data)[0]
for index in lis:
    股票名称=index[1]
    涨跌幅 = index[3]/100
    print(股票名称,涨跌幅)
    with open('data2.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write=csv.writer(f)
        csv_write.writerow([股票名称,涨跌幅])
