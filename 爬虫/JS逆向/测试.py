"""
username: wqeqweqwez
password: FT+MNC5QPDSnaRf7HPiWHaT7MuQ1F40w0oNzACPOqMfI751R59VPntlY0jU9yQcJI7xZllboWrPZvKr9YgbT46Ws8s1c0swYqnNi1Tzz19HIMQJE/FmNpC9Ko8w4uq+j57fdBEUsUphz7TMi9FK9LhGA9UyQ0sbarvPmwTOvl5A=
csrfmiddlewaretoken: faehpfZQ8eokF9DjscvSCNZNY79ZpdCLwSeZXpRKg5oLKnT6jdAY4jVeGiXMBBQ6

username: qwe12345678
password: Z1jFjSHIEC4B+fc8+y4qKo6X2eSnL5hLA/kN91xs4vI3GZi+7RXXy3/8eJDOlO6T8wKyt+jQcmJ/t0oDlsaX8R79DRV0KEJ4Vonb2mIsuZl/C3NwbzZ2Y8Q9wcSUgXfh6t2eyrF9/RmZbb7Zj3zxFDsg8iBVjp3zVieDK/xqGD4=
csrfmiddlewaretoken: w1yspJBu1scE6PtoHDMpDKxDhKfiLutxNJyaXTto9jc5b3JbyERv5gt4ZV35XSHS

username: fdsafasddfd
password: NCSBbKbVuPAkUeyx53vB8yxUIgabUGMDRwaK/rcXxTjNO1gZP6p4UAtVwCZShCIRz+eO+SKqEoahZTQ27GKBpUCxlaAO6Iu8tkCKuiaRNeFf+Idwxp8CtPx5IMFZ6c67HHvKtllz2ubjZXYurG6TfRitPmHqNTKlL6IZOTBfHtY=
csrfmiddlewaretoken: Sxjon9CCSurkdEa5FRaV9E88ODSb4Ap49fj6Vjuw0lrLiSqSwSf1Ba4zwOGYgYDp


需要解密的有两个参数

password
csrfmiddlewaretoken   就在页面中 可以通过页面解析方法获取

"""
import execjs

js = """
function tests(p, a, c, k, e, d) {
    e = function(c) {
        return (c < a ? "" : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
    }
    ;
    if (!''.replace(/^/, String)) {
        while (c--)
            d[e(c)] = k[c] || e(c);
        k = [function(e) {
            return d[e]
        }
        ];
        e = function() {
            return '\\w+'
        }
        ;
        c = 1;
    }
    ;while (c--)
        if (k[c])
            p = p.replace(/\\b\w+\\b/g, k[c]);
    return p;
}

"""
p = 'a 9(){1 3=$("#6").2();1 0=7 8();1 4=$("#d").2();0.e(4);1 5=0.0(3);$("#6").2(5);$("#c").b()}'
a = 15
c = 15
k = 'encrypt|var|val|password_old|public_key|pass_new|MemberPassword|new|JSEncrypt|doLogin|function|submit|login_button|pk|setPublicKey'.split('|')
e = 0
d = {}

tongyao = execjs.compile(js)

print(tongyao.call('tests',p, a, c, k, e, d))