import execjs,requests
from lxml import etree


def one():
    # 第一次请求， 获取token
    url = 'http://shanzhi.spbeen.com/login/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    csrfmiddlewaretoken = html.xpath('//input[@name="csrfmiddlewaretoken"]/@value')[0]
    return csrfmiddlewaretoken,url

# 第二次请求
my_csrf,my_url = one()
print(my_csrf,my_url)

def two(my_csrf,my_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': f'csrftoken={my_csrf}',
    }

    user = 'zengfanyu'

    with open('hun.js', 'r', encoding='utf-8') as f:
        en_data = execjs.compile(f.read()).call('doLogin', 'qwer1234')
        print(en_data)

    form_data = {
        'username': user,
        'password': en_data,
        'csrfmiddlewaretoken':my_csrf,
    }

    resp = requests.post(my_url, headers=headers, data=form_data)

    print(resp.text)
    return resp.text

ress = two(my_csrf, my_url)
print(ress)

