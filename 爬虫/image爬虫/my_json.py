
a = {"name":'tongyao','sex':True,'age':None,'addr':"湖南长沙"}

# print(a.get("addr"))# keys()  get  values ()  []  items [(),()]

import json

# 字典转json格式的字符串
json_data = json.dumps(a)
print(json_data,type(json_data))

# json格式的字符串转字典
dict_data = json.loads(json_data)
print(dict_data, type(dict_data))

# 作业 json 也是可以操作文件的  load 和 dump