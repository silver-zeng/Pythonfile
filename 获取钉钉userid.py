# 参数
# "access_token": "0cc028c596bf34d38967eaf52adfcc03",
# "dingding_token": "0cc028c596bf34d38967eaf52adfcc03",
# "kingdee": "http://117.40.226.220:7891",
# "appkey": "dingmhz9zth1mqz4k6gp",
# "appsecret": "PGwrVxfDsOBFgfKGGcf-xy3r0XxcBMfsaieovinldVOEAm_iFReLDmbafXBJymVG",
# "robotCode": "dingmhz9zth1mqz4k6gp"


import requests

# 获取钉钉访问的access_token
def get_access_token():
    res = requests.get(
        url="https://oapi.dingtalk.com/gettoken",
        params={
            "appkey": "dingmhz9zth1mqz4k6gp",
            "appsecret": "PGwrVxfDsOBFgfKGGcf-xy3r0XxcBMfsaieovinldVOEAm_iFReLDmbafXBJymVG",
        }
    )
    print('获取访问token的响应日志：' + str(res.json()))
    return res.json()["access_token"]

# 获取部门列表dept_id
def get_dept_id():
    res = requests.get(
        url="https://oapi.dingtalk.com/department/list",
        params={
            "access_token": get_access_token(),
        }
    )
    print('获取部门列表的响应日志：' + str(res.json()))


# 获取部门下所有用户userid，47804716直属营业部，473594099保理基建部
def get_userid():
    res = requests.get(
        url="https://oapi.dingtalk.com/topapi/user/listid",
        params={
            "access_token": get_access_token(),
            "dept_id": "901247231",
        }
    )
    print('获取部门下所有用户userid的响应日志：' + str(res.json()))
    return res.json()["result"]["userid_list"]

# 获取用户详情
def get_user_detail():
    for userid in get_userid():
        res = requests.get(
            url="https://oapi.dingtalk.com/topapi/v2/user/get",
            params={
                "access_token": get_access_token(),
                "userid": userid,
            }
        )
        print('获取用户详情的响应日志：' + str(res.json()))
        # 打印用户的userid和姓名和部门
        # 导出excel
        print(str(userid) + ',' + res.json()["result"]["name"] + ',' + str(res.json()["result"]["dept_id_list"][0]), file=open("风控部.csv", "a"))

get_user_detail()

