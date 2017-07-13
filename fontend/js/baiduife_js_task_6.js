/**
 * Baidu ife JavaScript task 06
 * code by sin
 * June 16 2017
 */


/* 定义全局队列 */
var listData = [];


/**
 * getData()
 * 获取输入的值,并加以判断值的合法性
 */
function getData(){
    var input = document.getElementById("input");
    var newValue = input.value;
    input.value = "";
    input.focus();
    if(newValue === ""){
        showTips("你还没有输入任何值");
        return false;
    }
    else{
        var pattern = /[^0-9a-zA-Z\u4e00-\u9fa5]+/gi;
        newValue = newValue.split(pattern).filter(function(arg){
            return arg !== "";
        });
        if(newValue.length === 0){
            showTips("你输入的都是些什么鬼啊..");
            return false;
        }
        return newValue;
    }
}

/**
 * getSearchData()
 * 获取要搜索的数据
 */
function getSearchData(){
    var searchData = document.getElementById("search-input").value;
    if(searchData === ""){
        showTips("你还没有输入要搜索的字符串吖!!");
        return false;
    }
    else{
        return searchData;
    }
}


/**
 * showTips()
 * 显示各种提示信息
 */
function showTips(str){
    var show = document.getElementsByClassName("show-tips")[0];
    if(str === "" || str === null || str === undefined){
        show.innerHTML = "^__^";
    }
    else{
        show.innerHTML = str;
    }
}


/**
 * display()
 * 将处理好的队列展示出来
 */
function display(list){
    var html = "";
    var dis = document.getElementById("display");
    for(var i = 0; i < list.length; i++){
        html += "<li>" + list[i] + "</li>";
    }
    dis.innerHTML = html;
}


/* 执行 */
window.onload = function(){

    // change the colors
    var bodyNode = document.getElementsByTagName("body")[0];
    bodyNode.style.backgroundColor = `rgba(${~~(Math.random()*255)}, ${~~(Math.random()*255)}, ${~~(Math.random()*255)}, 0.5)`;
    var btnNodes = document.getElementsByClassName("btn");
    for(let i = 0; i < btnNodes.length; i++){
        btnNodes[i].style.backgroundColor = `rgba(${~~(Math.random()*255)}, ${~~(Math.random()*255)}, ${~~(Math.random()*255)}, 0.3)`;
    }

    // left in
    var btnLI = document.getElementById("left-in");
    btnLI.addEventListener("click", function(){
        var newData = getData();
        if(newData){
            console.log(newData);
            listData = newData.concat(listData);
            display(listData);
            showTips("~^_^");
        }
    })

    // right in
    var btnRI = document.getElementById("right-in");
    btnRI.addEventListener("click", function(){
        var newData = getData();
        if(newData){
            console.log(newData);
            listData = listData.concat(newData);
            display(listData);
            showTips("^_^~");
        }
    })

    // left out
    var btnLO = document.getElementById("left-out");
    btnLO.addEventListener("click", function(){
        if(listData.length > 0){
            var delItem = listData.shift();
            showTips("delete " + delItem);
            display(listData);
        }
        else{
            showTips("队列都被你删空啦!!");
        }
    })

    // right out
    var btnRO = document.getElementById("right-out");
    btnRO.addEventListener("click", function(){
        if(listData.length > 0){
            var delItem = listData.pop();
            showTips("delete " + delItem);
            display(listData);
        }
        else{
            showTips("队列都被你删空啦!!");
        }
    })
    
    // search
    var btnS = document.getElementById("search-btn");
    btnS.addEventListener("click", function(){
        if(listData.length > 0){
            var sData = getSearchData();
            if(sData){
                var liNodes = document.getElementsByTagName("li");
                for(var i = 0; i < liNodes.length; i++){
                    liNodes[i].style.backgroundColor = "#fe8d9e";
                }

                for(var i = 0; i < listData.length; i++){
                    var temp = listData[i].indexOf(sData);
                    if(temp >= 0){
                        liNodes[i].style.backgroundColor = "#ff0000";
                    }
                }
            }
        }
        else{
            showTips("队列都是空的,你搜啥??");
        }
    })
}
