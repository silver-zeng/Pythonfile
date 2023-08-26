import  requests


url = "https://www.wxbqb.com/res/2023/07-27/17/39d971dddded1ff14ee38379c17fc558.gif"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Cookie': '__51uvsct__JlZuw2rrHuhkRhsF=1; __51vcke__JlZuw2rrHuhkRhsF=e6e51144-accb-5e3b-b74d-258f9bf2a254; __51vuft__JlZuw2rrHuhkRhsF=1692972374794; Hm_lvt_de87f3d7f62c428f4c820a38e3b87a9e=1692972375; __gads=ID=44ec5abf7d5441b5-224843ce1de30014:T=1692972376:RT=1692977187:S=ALNI_MaroWDbRSc-4I41rUXumn0lFy2U5Q; __gpi=UID=00000c33331ec2cd:T=1692972376:RT=1692977187:S=ALNI_MYOK86sxkG0lUziWKLwoFWIdQck4Q'
}
res = requests.get(url=url,headers=head)
with open("1.gif","wb") as f:
    print(res)
    f.write(res.content)
