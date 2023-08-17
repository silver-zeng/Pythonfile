import requests

USER_AGENT ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
COOKIE = 'Admin-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3N0X2xpc3QiOlsiMTYzIl0sInJvbGVfbGlzdCI6WyIxIiwiMTcwIiwiMTcxIiwiMTcyIiwiMTczIiwiMTc2IiwiMTc3IiwiMTc4IiwiMTc5IiwiMTgwIiwiMTgxIiwiMTgyIiwiMTg0IiwiMTg4IiwiMTg5IiwiMTkwIiwiMTkzIiwiMTk0IiwiMTk2IiwiMTk3Il0sInVzZXJfbmFtZSI6ImFkbWluIiwiY2xpZW50X2lkIjoibWlkZGxlLWdlbmVyYWwtZnJvbnQiLCJjbGllbnRfbGlzdCI6WyJtaWRkbGUtZ2VuZXJhbC1mcm9udCIsImNvbW1vbi1jYW11bmRhLWJpeiIsInBpZyIsImNvbW1vbi1zc28tY29tcG9uZW50LW9hdXRoMiIsInNjcy1mbXMtYml6Iiwic2NzLW1jcy1iaXoiXSwiYXZhdGFyX0lkIjoiMTM2MyIsImFjY291bnRfaWQiOiIxIiwidXNlcl90eXBlIjowLCJwaG9uZSI6IjE4ODg4ODg4ODg4Iiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTY5MjI3NDc4MSwib2ZmaWNlX2xpc3QiOlsiMSJdLCJqdGkiOiJkOGE5Y2RkYy03ODdmLTQ1MDctYWMyZS1mMTMyOTY4ZjE0ZmYiLCJlbWFpbCI6InpwQHFxLmNvbSJ9.SGaQnPaEKrZWIXh6nHSmIcXLGMBLS1yn7LdVBrQLCR4; sidebarStatus=1'
Authorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3N0X2xpc3QiOlsiMTYzIl0sInJvbGVfbGlzdCI6WyIxIiwiMTcwIiwiMTcxIiwiMTcyIiwiMTczIiwiMTc2IiwiMTc3IiwiMTc4IiwiMTc5IiwiMTgwIiwiMTgxIiwiMTgyIiwiMTg0IiwiMTg4IiwiMTg5IiwiMTkwIiwiMTkzIiwiMTk0IiwiMTk2IiwiMTk3Il0sInVzZXJfbmFtZSI6ImFkbWluIiwiY2xpZW50X2lkIjoibWlkZGxlLWdlbmVyYWwtZnJvbnQiLCJjbGllbnRfbGlzdCI6WyJtaWRkbGUtZ2VuZXJhbC1mcm9udCIsImNvbW1vbi1jYW11bmRhLWJpeiIsInBpZyIsImNvbW1vbi1zc28tY29tcG9uZW50LW9hdXRoMiIsInNjcy1mbXMtYml6Iiwic2NzLW1jcy1iaXoiXSwiYXZhdGFyX0lkIjoiMTM2MyIsImFjY291bnRfaWQiOiIxIiwidXNlcl90eXBlIjowLCJwaG9uZSI6IjE4ODg4ODg4ODg4Iiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTY5MjI3NDc4MSwib2ZmaWNlX2xpc3QiOlsiMSJdLCJqdGkiOiJkOGE5Y2RkYy03ODdmLTQ1MDctYWMyZS1mMTMyOTY4ZjE0ZmYiLCJlbWFpbCI6InpwQHFxLmNvbSJ9.SGaQnPaEKrZWIXh6nHSmIcXLGMBLS1yn7LdVBrQLCR4'
REQUESTID = 'pigpigpig'
REQUESTsignature = 'pigpigpig'
MH_COOKIE = 'Admin-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3N0X2xpc3QiOlsiMTYzIl0sInJvbGVfbGlzdCI6WyIxIiwiMTcwIiwiMTcxIiwiMTcyIiwiMTczIiwiMTc2IiwiMTc3IiwiMTc4IiwiMTc5IiwiMTgwIiwiMTgxIiwiMTgyIiwiMTg0IiwiMTg4IiwiMTg5IiwiMTkwIiwiMTkzIiwiMTk0IiwiMTk2IiwiMTk3Il0sInVzZXJfbmFtZSI6ImFkbWluIiwiY2xpZW50X2lkIjoibWlkZGxlLWdlbmVyYWwtZnJvbnQiLCJjbGllbnRfbGlzdCI6WyJtaWRkbGUtZ2VuZXJhbC1mcm9udCIsImNvbW1vbi1jYW11bmRhLWJpeiIsInBpZyIsImNvbW1vbi1zc28tY29tcG9uZW50LW9hdXRoMiIsInNjcy1mbXMtYml6Iiwic2NzLW1jcy1iaXoiXSwiYXZhdGFyX0lkIjoiMTM2MyIsImFjY291bnRfaWQiOiIxIiwidXNlcl90eXBlIjowLCJwaG9uZSI6IjE4ODg4ODg4ODg4Iiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTY5MjI3NDc4MSwib2ZmaWNlX2xpc3QiOlsiMSJdLCJqdGkiOiJkOGE5Y2RkYy03ODdmLTQ1MDctYWMyZS1mMTMyOTY4ZjE0ZmYiLCJlbWFpbCI6InpwQHFxLmNvbSJ9.SGaQnPaEKrZWIXh6nHSmIcXLGMBLS1yn7LdVBrQLCR4; portal-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJfSWQiOm51bGwsImFjY291bnRfaWQiOiIyMTIiLCJ1c2VyX3R5cGUiOjEsInBob25lIjoiMTg3MDc5OTQ0MTciLCJ1c2VyX25hbWUiOiJmMmQ2NWY2Ny1hYmJjLTRkZjktYjNmYy03Y2NkODY1OGUzMjIiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNjkyNDczMTc4LCJvZmZpY2VfbGlzdCI6WyI1Il0sImp0aSI6IjhkZjBhM2MwLTljZDItNDJmYi05ZTIxLWJlNWJhOTk5MDcwMSIsImVtYWlsIjoiIiwiY2xpZW50X2lkIjoibWlkZGxlLWdlbmVyYWwtZnJvbnQifQ.LxkFMV1jtopZnflBR0cTGek39o6HunKtUG4wOMHOb9I; sidebarStatus=1'

# 门户项目准入，港口煤炭
def project_save():
    url = 'https://test.yiscs.cn/api/GeneralFront/web/portal/project/save'
    head = {
        'User-Agent': USER_AGENT,
        'Cookie': MH_COOKIE,
        'Requestid': REQUESTID,
        'Requestsignature': REQUESTsignature,
        'Authorization': Authorization,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    body = {
            "projectActualControllerFormList": [
                {
                    "actualControllerName": "接口测试",
                    "actualControllerPhone": "13456567878"
                }
            ],
            "projectSubjectMatter": [],
            "projectBasicForm": {
                "productId": "7",  # 6 是电厂，7港口，8大基建
                "name": "zfy接口_煤炭港口再搞一下",
                "violationLiability": "乱七八招删掉阿是发",
                "attachment": "12476,12477,12478"
            },
            "projectExtendForm": {},
            "projectOwnerForm": {
                "ownerId": "15",
                "ownerName": "",
                "lockPrice": False,
                "estimatedCooperation": [
                    "2023-08-01",
                    "2024-01-01"
                ],
                "estimatedSupplyTotalQty": "10000000",
                "estimatedMonthlyTradeTotalQty": "10000",
                "estimatedTradeTurnoverFrequency": "30",
                "firstReturnFundRatio": 80,
                "priceRule": "没有搞啥阿萨法收款方哈市好可怜",
                "estimatedCooperationStartDate": "2023-08-01",
                "estimatedCooperationEndDate": "2024-01-01"
            },
            "ownerReceivingList": [
                {
                    "ownerId": "15",
                    "receiverAddress": "南昌"
                }
            ],
            "projectOwnerSettlementForm": {
                "settlementDetailList": []
            },
            "projectSupplierList": [
                {
                    "supplierId": "38",
                    "deliveryLocation": "",
                    "estimatedPurchasePrice": "899",
                    "supplierStationList": [
                        {
                            "stationAddress": "山西",
                            "stationOwnership": 1,
                            "remarks": "测试"
                        }
                    ],
                    "projectSubjectMatterFormList": [
                        {
                            "estimatedPurchasePrice": "899",
                            "deliveryLocation": ""
                        }
                    ]
                }
            ],
            "projectSupplierSettlementForm": {
                "settlementDetailList": []
            },
            "projectCoalSpecForm": {
                "calorificValue": "5000-5500",
                "sulfurContent": "<10",
                "waterContent": "<3",
                "volatileContent": ">22"
            },
            "projectCustomerList": [
                {
                    "defFlag": 1,
                    "cooperatorFlag": 1,
                    "customerId": "22",
                    "bankAccountId": "89",
                    "officeName": "工商银行",
                    "bankAccountNumber": "130012455555888800121",
                    "bankAccountName": "江西北方宏泰供应链管理有限公司",
                    "customerName": "江西北方宏泰供应链管理有限公司"
                },
                {
                    "defFlag": 0,
                    "cooperatorFlag": 0,
                    "customerId": "114",
                    "bankAccountId": "85",
                    "officeName": "中国邮政储蓄银行股份有限公司芦溪县人民东路支行",
                    "bankAccountNumber": "936005010020946797",
                    "bankAccountName": "萍乡远通煤业有限公司",
                    "customerName": "萍乡远通煤业有限公司"
                }
            ],
            "code": "7"
        }
    res = requests.post(url, headers=head, json=body)
    print(res.json())
#  项目准入查询列表
def xmcx():
    url = 'https://test.yiscs.cn/api/GeneralFront/web/biz/project/listPage'
    head = {
        'User-Agent': USER_AGENT,
        'Cookie': COOKIE,
        'Requestid': REQUESTID,
        'Requestsignature': REQUESTsignature,
        'Referer': 'https://test.yiscs.cn/general/project/projectInfo',
        'Authorization': Authorization,
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

# 收付款登记新增
def collectPayRegistration():
    url = 'https://test.yiscs.cn/api/GeneralFront/web/biz/collectPayRegistration/collectPayRegistration'
    head = {
        'User-Agent': USER_AGENT,
        'Cookie': COOKIE,
        'Requestid': REQUESTID,
        'Requestsignature': REQUESTsignature,
        'Referer': 'https://test.yiscs.cn/general/project/receiptPaymentRegisterDetail',
        'Authorization': Authorization,
        'Content-Type': 'application/json'
    }
    date = {
        "collectPayType": 2,    # 1是收款单，2 是付款单
        "collectPayBankAccountList":
        [
            {
                "attachment": "12467",
                "remarks": '',
                "createDate": '',
                "updateBy": '',
                "createBy": '',
                "createByName": '',
                "updateByName": '',
                "updateDate": '',
                "collectPayRegistrationId": '',
                "bankReceiptNumber": "2976315",
                "tradeDate": "2023-08-16",
                "amount": 5112,
                "collectBankAccount": "江西汇易贸易有限公司",
                "collectBankNumber": "2055427263000159",
                "collectBankName": "渤海银行股份有限公司",
                "collectRemarks": '',
                "payerBankAccount": "江西汇易贸易有限公司",
                "payerBankNumber": "8115701012700145005",
                "payerBankName": "中信银行总行管理部（不受理储蓄业务）",
                "transferPurpose": '',
                "file": ''
            }
        ],
        "tradeDate": "2023-08-16",
        "amount": 5112
    }

    res = requests.post(url, headers=head, json=date)
    print(res.json())



