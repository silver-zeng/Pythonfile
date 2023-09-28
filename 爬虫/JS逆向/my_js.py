'''
    1、安装依赖 pip3 install PyExecJS
    2、导包 import execjs
    3、从 JS 文件中读取源码
        def js_from_file(file_name):
            """
            读取js文件
            :return:
            """
            with open(file_name, 'r', encoding='UTF-8') as file:
                result = file.read()
            return result
    最后，使用 execjs 类的compile()方法编译加载上面的 JS 字符串，返回一个上下文对象

    import execjs
    from js_code import *
    # 编译加载js字符串
    context1 = execjs.compile(js_from_file('./norm.js'))

    4、最后，调用上下文对象的call() 方法执行 JS 方法
    其中，参数包含：JS 代码被调的方法名、对应方法的传入参数

        # 调用js代码中的add()方法，参数为2和3
        # 方法名：add
        # 参数：2和3
        result1 = context1.call("add", 2, 3)

    5、非对称加密，需要导包，要安装在当前py文件夹目录下   cmd中输入：npm install node-jsencrypt
        若要使用非对称加密，还需要将文件在js文件中引入：  var 变量名=require('node-jsencrypt')
'''
# 执行js的第三方库
import execjs