/**
 * Baidu ife JavaScript form task 01
 * by sin
 * June 17 2017
 */


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
 * 表单验证:验证字符串长度
 */
function validata_length(field){
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
 * showTips()
 * 显示提示信息
 */
function showTips(field, status, str){
    var p = ["p-1", "p-2", "p-3"];
    var i = field.id.split("")[6];
    var tip = document.getElementById(p[i-1]);
    tip.innerHTML = str;

    if(status === "error"){
        field.style.border = "solid 2px #dd0000";
        tip.style.color = "#dd0000";
    }
    else if(status === "right"){
        field.style.border = "solid 2px #00aa55";
        tip.style.color = "#00aa55";
    }
    else{
        field.style.border = "solid 1px #999";
        tip.style.color = "#999";
    }
}


window.onload = function(){
    var button1 = document.getElementById("button-1");
    var button2 = document.getElementById("button-2");
    var button3 = document.getElementById("button-3");
    var name1 = document.getElementById("input-1");
    var name2 = document.getElementById("input-2");
    var name3 = document.getElementById("input-3");
    
    button1.addEventListener("click", function(){
        if(validate_required(name1)){
            var sum = validata_length(name1);
            if(sum < 4 || sum > 16){
                showTips(name1, "error", "长度不合适");
            }
            else{
                showTips(name1, "right", "输入正确");
            }
        }
        else{
            showTips(name1, "error", "不能为空");
        }
    })

    button2.addEventListener("click", function(){
        if(validate_required(name2)){
            var sum = validata_length(name2);
            if(sum < 4 || sum > 16){
                showTips(name2, "error", "长度不合适");
            }
            else{
                showTips(name2, "right", "输入正确");
            }
        }
        else{
            showTips(name2, "error", "不能为空");
        }
    })

    button3.addEventListener("click", function(){
        if(validate_required(name3)){
            var sum = validata_length(name3);
            if(sum < 4 || sum > 16){
                showTips(name3, "error", "长度不合适");
            }
            else{
                showTips(name3, "right", "输入正确");
            }
        }
        else{
            showTips(name3, "error", "不能为空");
        }
    })
}
