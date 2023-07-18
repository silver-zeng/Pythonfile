//获取图片
var pic = $('.banner .pic li');
//获取小圆点
var tab = $('.banner .tab li');
//获取箭头
var btn = $('.banner .btn li');
//长度
var len=pic.length;
var first =0;
//定时器
var timer;

//初始化
tab.eq(0).addClass('on');
pic.hide().eq(0).show();

//小圆圈区域
tab.click(function () {
    var x= $(this).index();
    if(x != first){
        change(x)
    }
})

//箭头
btn.click(function () {
    var x = first;
    // console.log($(this).index())
    if($(this).index()){
        x++;
        if(x>=len) x=0;
    }else {
        x--;
        if(x<0) x=len-1
    }
    change(x)  // 只接受0，1，2，3
})

//变化函数
function change(n) {
    // 把老的样式去掉，给当前点击的元素增加样式
    tab.eq(first).removeClass('on');//去除on的属性
    pic.eq(first).fadeOut(1000); // 隐藏上一张的图片
    first = n;
    tab.eq(first).addClass('on')// 显示当前点击的小圆点
    pic.eq(first).fadeIn(1000); //显示当前圆点所对应的图片
}

function auto() {
    timer = setInterval(function () {
        var x= first;
        x++;
        // 取余 0%4  1%4  2%4  3%4
        x %= len;
        change(x);
    },2000);
}
auto();
//清除定时器
$('.banner').hover(function () {
    clearInterval(timer);
},auto);

