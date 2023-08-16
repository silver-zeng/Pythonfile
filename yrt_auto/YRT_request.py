import requests

#  项目准入查询列表
def xmcx():
    url = 'https://test.yiscs.cn/api/GeneralFront/web/biz/project/listPage'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie': 'portal-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJfSWQiOm51bGwsImFjY291bnRfaWQiOiIyMTIiLCJ1c2VyX3R5cGUiOjEsInBob25lIjoiMTg3MDc5OTQ0MTciLCJ1c2VyX25hbWUiOiJmMmQ2NWY2Ny1hYmJjLTRkZjktYjNmYy03Y2NkODY1OGUzMjIiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNjkxNzAwNTcxLCJvZmZpY2VfbGlzdCI6WyI1Il0sImp0aSI6ImRmNWFlNmRkLTg2NDUtNGRmNS1hY2JkLWQ1MjMwZTc4NThjZCIsImVtYWlsIjoiIiwiY2xpZW50X2lkIjoibWlkZGxlLWdlbmVyYWwtZnJvbnQifQ.rhwGsiFqZdsAdbQYLsU24FZZntjqCJcCOOE6VnH_dQg; Admin-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3N0X2xpc3QiOlsiMTgyIl0sInJvbGVfbGlzdCI6WyIxNzEiXSwidXNlcl9uYW1lIjoiemZ5c3d6eSIsImNsaWVudF9pZCI6Im1pZGRsZS1nZW5lcmFsLWZyb250IiwiY2xpZW50X2xpc3QiOlsiY29tbW9uLWNhbXVuZGEtYml6IiwibWlkZGxlLWdlbmVyYWwtZnJvbnQiLCJzY3MtZm1zLWJpeiJdLCJhdmF0YXJfSWQiOm51bGwsImFjY291bnRfaWQiOiIyMjAiLCJ1c2VyX3R5cGUiOjAsInBob25lIjoiMTMzNDU2NTY4OTgiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNjkyMDIzOTM1LCJvZmZpY2VfbGlzdCI6WyIxIl0sImp0aSI6IjE4Y2FkYjRkLTgxOTctNDg1MC05MDM0LTkxMzU3NzI4MzQ2MCIsImVtYWlsIjpudWxsfQ.cswBjMP5cCnhDeBl7I2b13qrFaN9mImGj7jLSo_jG-Q; sidebarStatus=1',
        'Requestid': 'pigpigpig',
        'Requestsignature': 'pigpigpig',
        'Referer': 'https://test.yiscs.cn/general/project/projectInfo',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3N0X2xpc3QiOlsiMTgyIl0sInJvbGVfbGlzdCI6WyIxNzEiXSwidXNlcl9uYW1lIjoiemZ5c3d6eSIsImNsaWVudF9pZCI6Im1pZGRsZS1nZW5lcmFsLWZyb250IiwiY2xpZW50X2xpc3QiOlsiY29tbW9uLWNhbXVuZGEtYml6IiwibWlkZGxlLWdlbmVyYWwtZnJvbnQiLCJzY3MtZm1zLWJpeiJdLCJhdmF0YXJfSWQiOm51bGwsImFjY291bnRfaWQiOiIyMjAiLCJ1c2VyX3R5cGUiOjAsInBob25lIjoiMTMzNDU2NTY4OTgiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNjkyMDIzOTM1LCJvZmZpY2VfbGlzdCI6WyIxIl0sImp0aSI6IjE4Y2FkYjRkLTgxOTctNDg1MC05MDM0LTkxMzU3NzI4MzQ2MCIsImVtYWlsIjpudWxsfQ.cswBjMP5cCnhDeBl7I2b13qrFaN9mImGj7jLSo_jG-Q',
        'Content-Type': 'application/json'
    }
    data = {
        "pageNum": 1,
        "pageSize": 20,
        "productId": "",
        "status": ""
    }
    res = requests.post(url, headers=head, json=data)

    print(res.json())
