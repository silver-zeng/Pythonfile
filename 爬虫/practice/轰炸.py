import time
import requests
import re
import keyboard

for u in range(7,40):
    url = f'http://www.ainicr.cn/qh/{u}.html'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Referer': 'http://www.ainicr.cn/'
    }

    res = requests.get(url,headers=head)
    # print(res.text)
    response = res.text
    worlds = re.findall('<p>(.*?)<p>',response)
    time.sleep(3)
    for w in worlds:
        w1 = w[0:]
        keyboard.write(w1)
        keyboard.press_and_release("enter")
        print(w1)
