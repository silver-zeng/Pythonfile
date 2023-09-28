import base64
import binascii
import random
import string
from Crypto.Cipher import AES



# 16个随机字符串或者也可以写成一个固定值
def random_str(str_len):
    rtn_str = ''
    chr_pool = string.ascii_letters + string.digits # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(str_len):
        rtn_str += random.choice(chr_pool)
    return rtn_str



# AES对称加密
def aes_encrypt(content, key, iv):
                #  密钥          模式          向量
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    # 明文补码
    num = 16 - len(content) % 16
    bytes_content = (content+(num*chr(num))).encode()
    # 加密
    encrypted_content = aes.encrypt(bytes_content)
    # base64编码
    b64_encrypted_content = base64.b64encode(encrypted_content).decode()
    return b64_encrypted_content


# 生成params的值
def get_params(AES_KEY_2):
    content = '{"rid":"R_SO_4_1313584359","threadId":"R_SO_4_1313584359","pageNo":"7","pageSize":"20","cursor":"1694878383196","offset":"0","orderType":"1","csrf_token":""}'
    AES_KEY_1 = '0CoJUm6Qyw8W8jud'
    iv = "0102030405060708"
    # 第一次加密
    one = aes_encrypt(content,AES_KEY_1.encode(),iv.encode())
    # 第二次加密
    two = aes_encrypt(one, AES_KEY_2.encode(), iv.encode())
    print(two)
    return two

# my_key = random_str(16)
# get_params(my_key)


# 生成c
def rsa_encrypt(content,exponent, modulus): # 明文， 指数， 公模
    # 小端字节序 和大端字节序
    content = content[::-1]
    # 先全部转成10进制进行计算
    rsa = int(binascii.hexlify(content.encode()),16) **int(exponent,16) % int(modulus,16)
    # 计算完了之后再转成16进制
    hex_rsa = format(rsa, 'x')
    print(hex_rsa)
    return hex_rsa



# "dcde03cdfa88030d2d01db33d92a6fa7bf71166a55f9239146135b4e9789fd85a7ea723796d8dea3a5e70c4a5ebdc451fb7d843757d389970028633ef73e25a3f20735afb408956b2b7498a0e194680bfa7e115f6941256ec2ebbba6053e156472bda8a058905644c235dad2232580e7b01ff488e872b8b0b97c850ba235280e"

def get_encSecKey():
    a = "jjKMeNHcutkpjnoj"
    b = "010001"
    c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    return rsa_encrypt(a,b,c)