
// 引入非对称加密工具包
var JSEncrypt=require('node-jsencrypt');

function doLogin(my_password){
    // 获取用户密码
    var password_old=my_password;
    // 加密实例化
    var encrypt=new JSEncrypt();

    var public_key='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaP+rYm6rqTMP565UmMU6YXq46KtAN3zwDSO8LNa15p0lJfsaY8jXY7iLsZqQZrGYr2Aayp6hYZy+Q+AMB/VUiSpD9ojPyOQ7r9jsf9jZbTOL4kj6iLZn37fEhp4eLvRgy5EJCyQoFyLCsgLechBTlYl2eA95C3j4ZUFhiV6WFHQIDAQAB';
    // 设置加密
    encrypt.setPublicKey(public_key);
    // 对密码进行加密
    var pass_new=encrypt.encrypt(password_old);

    return pass_new;
}



// var JSEncrypt=require('node-jsencrypt')
//
// function doLogin(my_ppassword){
//     // 获取用户密码
//     var password_old=my_ppassword;
//     // 加密实例化
//     var encrypt=new JSEncrypt();
//
//     var public_key='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaP+rYm6rqTMP565UmMU6YXq46KtAN3zwDSO8LNa15p0lJfsaY8jXY7iLsZqQZrGYr2Aayp6hYZy+Q+AMB/VUiSpD9ojPyOQ7r9jsf9jZbTOL4kj6iLZn37fEhp4eLvRgy5EJCyQoFyLCsgLechBTlYl2eA95C3j4ZUFhiV6WFHQIDAQAB';
//     // 设置加密
//     encrypt.setPublicKey(public_key);
//     // 对密码进行加密
//     var pass_new=encrypt.encrypt(password_old);
//
//     return pass_new;
// }
// my_ppassword='qwer1234'
// doLogin(my_ppassword)