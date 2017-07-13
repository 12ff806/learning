/**
 * Baidu ife JavaScript form task 02
 * by sin
 * June 18 2017
 */


var flag = false;


/**
 * $
 * 简单封装document.getElementById()方法
 */
var $ = function(id){
    return document.getElementById(id);
}


/**
 * addEventHandler(element, event, listener)
 * 封装事件监听,兼容IE8等浏览器
 */
function addEventHandler(element, event, listener){
    if(element.addEventListener){
        element.addEventListener(event, listener, false);
    }
    // IE8 and before..
    else if(element.attachEvent){
        element.attachEvent("on" + event, listener);
    }
    // old method
    else{
        element["on" + event] = listener;
    }
}


/**
 * validate_required()
 * 表单验证:验证必填项目
 */
function validate_required(field){
    var value = field.value;
    if(value === "" || value === null){
        return false;
    }
    else{
        return true;
    }
}


/**
 * validate_length()
 * 表单验证:获取字符串长度
 */
function validate_length(field){
    var value = field.value;
    var sum = 0;
    for(let i = 0; i < value.length; i++){
        if((value.charCodeAt(i) > 0) && (value.charCodeAt(i) < 128)){
            sum++;
        }
        else{
            sum += 2;
        }
    }
    console.log(sum);
    return sum;
}


/**
 * validate_password()
 * 表单验证:验证两次密码是否一致
 */
function validate_password(field1, field2){
    var passwd1 = field1.value;
    var passwd2 = field2.value;
    return (passwd1 === passwd2);
}


/**
 * validate_email()
 * 表单验证:验证邮箱名称
 */
function validate_email(field){
    var value = field.value;
    var regex = /^[\w]+@[\w]+(\.[a-zA-Z]{2,3})+$/;
    return regex.test(value);
}


/**
 * validate_mobile()
 * 表单验证: 验证手机号码
 */
function validate_mobile(field){
    value = field.value;
    var regex = /^1(3|4|5|7|8)[\d]{9}$/;
    return regex.test(value);
}


/**
 * focus_name()
 * name聚焦事件的响应函数
 */
function focus_name(){
    $("name-tips").innerHTML = "请输入名称,长度为4~16位";
    $("name-tips").style.color = "#999";
    $("user-name").style.border = "solid 1px #999";
}


/**
 * blur_name()
 * name失焦事件的响应函数
 */
function blur_name(){
    if(validate_required($("user-name"))){
        var len = validate_length($("user-name"));
        if(len < 4 || len > 16){
            $("name-tips").innerHTML = "名称长度不合适";
            $("name-tips").style.color = "#aa0000";
            $("user-name").style.border = "solid 2px #aa0000";
            flag = false;
        }
        else{
            $("name-tips").innerHTML = "名称输入正确";
            $("name-tips").style.color = "#00aa55";
            $("user-name").style.border = "solid 2px #00aa55";
            flag = true;
        }
    }
    else{
        $("name-tips").innerHTML = "名称不能为空";
        $("name-tips").style.color = "#aa0000";
        $("user-name").style.border = "solid 2px #aa0000";
        flag = false;
    }
}


/**
 * focus_password()
 * passwd聚焦事件的响应函数
 */
function focus_password(){
    $("passwd-tips").innerHTML = "请输入密码,长度为6~30位";
    $("passwd-tips").style.color = "#999";
    $("user-passwd").style.border = "solid 1px #999";
}


/**
 * blur_password()
 * passwd失焦事件的响应函数
 */
function blur_password(){
    if(validate_required($("user-passwd"))){
        var len = validate_length($("user-passwd"));
        if(len < 6 || len > 30){
            $("passwd-tips").innerHTML = "密码长度不能小于6位,大于30位";
            $("passwd-tips").style.color = "#aa0000";
            $("user-passwd").style.border = "solid 2px #aa0000";
            flag = false;
        }
        else{
            $("passwd-tips").innerHTML = "密码可用";
            $("passwd-tips").style.color = "#00aa55";
            $("user-passwd").style.border = "solid 2px #00aa55";
            flag = true;
        }
    }
    else{
        $("passwd-tips").innerHTML = "密码不能为空";
        $("passwd-tips").style.color = "#aa0000";
        $("user-passwd").style.border = "solid 2px #aa0000";
        flag = false;
    }
}


/**
 * focus_password_again()
 * passwd again 聚焦事件的响应函数
 */
function focus_password_again(){
    $("passwd-again-tips").innerHTML = "再次输入相同密码";
    $("passwd-again-tips").style.color = "#999";
    $("user-passwd-again").style.border = "solid 1px #999";
}


/**
 * blur_password_again()
 * passwd again 失焦事件的响应函数
 */
function blur_password_again(){
    if(validate_required($("user-passwd-again"))){
        if(validate_password($("user-passwd"), $("user-passwd-again"))){
            $("passwd-again-tips").innerHTML = "两次输入的密码一致";
            $("passwd-again-tips").style.color = "#00aa55";
            $("user-passwd-again").style.border = "solid 2px #00aa55";
            flag = true;
        }
        else{
            $("passwd-again-tips").innerHTML = "两次输入的密码不一致";
            $("passwd-again-tips").style.color = "#aa0000";
            $("user-passwd-again").style.border = "solid 2px #aa0000";
            flag = false;
        }
    }
    else{
        $("passwd-again-tips").innerHTML = "请再次确认";
        $("passwd-again-tips").style.color = "#aa0000";
        $("user-passwd-again").style.border = "solid 2px #aa0000";
        flag = false;
    }
}


/**
 * focus_email()
 * email聚焦事件的响应函数
 */
function focus_email(){
    $("email-tips").innerHTML = "请输入邮箱";
    $("email-tips").style.color = "#999";
    $("user-email").style.border = "solid 1px #999";
}


/**
 * blur_email()
 * email失焦事件的响应函数
 */
function blur_email(){
    if(validate_required($("user-email"))){
        if(validate_email($("user-email"))){
            $("email-tips").innerHTML = "邮箱输入正确";
            $("email-tips").style.color = "#00aa55";
            $("user-email").style.border = "solid 2px #00aa55";
            flag = true;
        }
        else{
            $("email-tips").innerHTML = "邮箱格式不正确";
            $("email-tips").style.color = "#aa0000";
            $("user-email").style.border = "solid 2px #aa0000";
            flag = false;
        }
    }
    else{
        $("email-tips").innerHTML = "邮箱不能为空";
        $("email-tips").style.color = "#aa0000";
        $("user-email").style.border = "solid 2px #aa0000";
        flag = false;
    }
}


/**
 * focus_mobile()
 * mobile聚焦事件的响应函数
 */
function focus_mobile(){
    $("mobile-tips").innerHTML = "请输入手机号";
    $("mobile-tips").style.color = "#999";
    $("user-mobile").style.border = "solid 1px #999";
}


/**
 * blur_mobile()
 * mobile失焦事件的响应函数
 */
function blur_mobile(){
    if(validate_required($("user-mobile"))){
        if(validate_mobile($("user-mobile"))){
            $("mobile-tips").innerHTML = "手机号码正确";
            $("mobile-tips").style.color = "#00aa55";
            $("user-mobile").style.border = "solid 2px #00aa55";
            flag = true;
        }
        else{
            $("mobile-tips").innerHTML = "手机号码不正确";
            $("mobile-tips").style.color = "#aa0000";
            $("user-mobile").style.border = "solid 2px #aa0000";
            flag = false;
        }
    }
    else{
        $("mobile-tips").innerHTML = "手机号不能为空";
        $("mobile-tips").style.color = "#aa0000";
        $("user-mobile").style.border = "solid 2px #aa0000";
        flag = false;
    }
}


/**
 * btnHandle()
 * 按钮点击事件响应函数
 */
function btnHandle(){
    if(flag){
        alert("done");
    }
    else{
        blur_name();
        blur_password();
        blur_password_again();
        blur_email();
        blur_mobile();
        alert("error");
    }
}


window.onload = function(){
    addEventHandler($("btn-submit"), "click", btnHandle);
    addEventHandler($("user-name"), "focus", focus_name);
    addEventHandler($("user-name"), "blur", blur_name);
    addEventHandler($("user-passwd"), "focus", focus_password);
    addEventHandler($("user-passwd"), "blur", blur_password);
    addEventHandler($("user-passwd-again"), "focus", focus_password_again);
    addEventHandler($("user-passwd-again"), "blur", blur_password_again);
    addEventHandler($("user-email"), "focus", focus_email);
    addEventHandler($("user-email"), "blur", blur_email);
    addEventHandler($("user-mobile"), "focus", focus_mobile);
    addEventHandler($("user-mobile"), "blur", blur_mobile);
}
