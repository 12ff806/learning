/**
 * Baidu ife JavaScript form task 03
 * by sin
 * June 19 2017
 */


/**
 * 全局定义,需要在DOM完全加载完才有效
 */
var radio_show = ["school-wrap", "company-wrap"];
var radioOptions = document.getElementsByName("radio");
var schoolWrap = document.getElementById("school-wrap");
var companyWrap = document.getElementById("company-wrap");
var rstudent = document.getElementById("student");
var rnstudent = document.getElementById("non-student");
var scity = document.getElementById("city");
var schoolselects = document.getElementsByTagName("select");


/**
 * which_checked()
 * 判断哪个radio被选中
 */
function which_checked(radioObjs){
    for(var i = 0; i < radioObjs.length; i++){
        if(radioObjs[i].checked){
            return i;
        }
    }
}


/**
 * radioHandler()
 * radio点击事件响应函数
 */
function radioHandler(){
    schoolWrap.className = "hide";
    companyWrap.className = "hide";
   
    var i = which_checked(radioOptions);
    document.getElementById(radio_show[i]).className = "show"; 
}


/**
 * schoolHandler()
 * city点击事件响应函数
 */
function schoolHandler(){
    var selected = scity.selectedIndex;

    for(var i = 1; i < schoolselects.length; i++){
            schoolselects[i].className = "hide";
    }
    schoolselects[selected+1].className = "";
}


/**
 * DOM加载完成后执行
 */
window.onload = function(){
    radioHandler();
    rstudent.addEventListener("click", radioHandler, false);
    rnstudent.addEventListener("click", radioHandler, false);
    scity.addEventListener("click", schoolHandler, false);
}
