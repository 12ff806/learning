/**
 * floating layer
 * by Sin
 * 28 June 2017
 */


/**
 * 验证是否设置弹窗大小 如果设置 则显示设置框 否则隐藏
 */
function validateSetwh(){
    var whNode = document.getElementById("wh");
    var setyNode = document.getElementById("sety");
    if(setyNode.checked){
        whNode.className = "show";
    }
    else{
        whNode.className = "hide";
    }
}


/**
 * 获取选择项及输入项的值
 */
function getValue(){
    var value = {};
    var inputNodes = document.getElementsByTagName("input");
    value[inputNodes[0].name] = inputNodes[0].value;
    value[inputNodes[1].name] = inputNodes[1].value;
    for(var i = 2; i < inputNodes.length; i++){
        if(inputNodes[i].checked){
            value[inputNodes[i].name] = inputNodes[i].value;
        }
    }
    if(value["setwh"] === "yes"){
        var wInput = document.getElementById("w-input");
        var hInput = document.getElementById("h-input");
        value["width"] = wInput.value;
        value["height"] = hInput.value;
    }
    return value;
}


function init(){
    var setyNode = document.getElementById("sety");
    var setnNode = document.getElementById("setn");
    setyNode.addEventListener("click", validateSetwh, false);
    setnNode.addEventListener("click", validateSetwh, false);

    var btnNode = document.getElementById("btn");
    btnNode.addEventListener("click", function(){
        btnNode.disabled = true;
        var config = getValue();
        // console.log(config);
        var floatlayer = new Floatinglayer(config);
        floatlayer.show()

        var fullScreen = document.getElementById("full-screen");
        fullScreen.addEventListener("click", function(){
            floatlayer.close();
            // btnNode.disabled = false;
        }, false);
    }, false);
}

window.onload = function(){
    init();
}
