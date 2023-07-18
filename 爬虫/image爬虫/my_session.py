import requests  #  70%

session = requests.session()

res = session.get('http://httpbin.org/cookies/set/tongyao/123456789')
print(res.text)

res1 = session.get('http://httpbin.org/cookies')
print(res1.text)

# selenium # mitmproxy