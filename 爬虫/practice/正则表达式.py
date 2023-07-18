import re   # 导入re包，用正则表达式的前提

'''
findall  在字符串中找到全部符合要求的内容
格式：
re.findall(要找的内容，找的范围)
会将找到的内容放入列表
'''

mail="598725443@qq.com ￥%*&（）"
# f=re.findall("qq",mail)
# print(f)

'''
re.match()只找字符串开头的内容
'''
f=re.match("598",mail)
# print(f)  # <re.Match object; span=(0, 3), match='598'>   span=(0, 3)表示找到的内容的位置，取头不取尾
# print(f.span())  # 表示找到的位置
# print(f.group())  # 表示找到的内容

"""
re.search() 在整个字符串里面找，但是只找到一个匹配的就返回
"""
d=re.search("4",mail)
# print(d)

"""
元字符：
.       匹配任意字符（除了\n）
[]      匹配[]中列举的字符      [1-5a-z] 表示1-5和a-z之间的字符
\d      匹配数字，即0-9
\D      匹配非数字
\s      匹配空格、tab健
\S      匹配非空白
\w      匹配单词符，即a-z，A-Z，0-9，_下划线
\W      匹配非单词符
若多个拼接，如"\d\w"  匹配数字和单词符拼接的内容

代表数量的元字符，要放在后面，如"\d\w*"
*   匹配前一个字符出现0次或者无限次
+   匹配前一个字符出现1或者无限次
？   匹配前一个字符出现0次或者1次
{m}  匹配前一个字符出现m次
{m,}  匹配前一个字符至少出现m次
{m,n}  匹配前一个字符出现m至n次
"""
print(re.findall(".",mail))  #查询所有字符
print(re.findall("[.]",mail))  #查询.
print(re.findall("\d",mail))  #查询其中所有数字
print(re.findall("\D",mail))  #查询非数字
print(re.findall("\s",mail))  #匹配空白
print(re.findall("\S",mail))  #匹配非空白
print(re.findall("\w",mail))  #匹配单词符
print(re.findall("\W",mail))  #匹配非单词符， 空格！@#￥%……&*（）·
print(re.findall("[1-5a-z]",mail))  #表示1-5和a-z之间的字符
print(re.findall("\d\W",mail))

print(re.findall("\w*",mail))  # 字符有或没有都可以,没有则会输出空列表元素占一位
print(re.findall("\w+",mail))  # 字符至少出现一次
print(re.findall("\w?",mail))  # 字符至少出现一次，或者没有
print(re.findall("\d{2}",mail)) # 表示2个连着的数字
print(re.findall("\d{2}\W",mail)) # 表示两个连着的数字且连着非单词符
print(re.findall("\d{3,}",mail))  #表示找到三个以上的连着的数字
print(re.findall("\d{2,3}",mail))  # 找到2到3个连在一起的数字

"""
代表边界的元字符
^  匹配字符串开头
$  匹配字符串结尾
\b  匹配一个单子的边界
\B  匹配非单词边界

"""
print(re.findall("\W{2,3}$",mail)) # 只看结尾符不符合
print(re.findall("^\w{2,3}",mail))  # 只看开头符不符合

"""
贪婪和非贪婪
贪婪：在整个表达式匹配成功的情况下，尽可能多的匹配
非贪婪：在整个表达式匹配成功的情况下，尽可能少的匹配
"""
print(re.findall("\d{2,3}",mail))

#判断是不是qq号
qq=input("请输入qq号：")
res=re.findall("^[1-9]\d{4,9}@qq[.]com$",qq)
print(res)
if res:
    print("%s是一个QQ号"%qq)
else:
    print("%s是一个假的QQ号！！！！"%qq)

