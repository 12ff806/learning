/**
 * BAIDU IFE JAVASCRIPT TASK 03
 * code by sin
 * June 11 2017
 */


/**
 * getData方法
 * 读取id为source的列表，获取其中城市名字及城市对应的空气质量
 * 返回一个数组,格式如: data = [["北京", 90], ...] 
 */
function getData(){
    var data = [];
    var sourceNode = document.getElementById("source");
    var sourceData = sourceNode.childNodes;
    for(var i = 1; i < sourceData.length; i=i+2){
        var tempArr = sourceData[i].innerHTML.split("：", 1);
        var tempNum = sourceData[i].getElementsByTagName("b")[0];
        tempArr[1] = parseInt(tempNum.innerHTML);
        data.push(tempArr);
    }
    return data;
}


/**
 * sortAqiData方法
 * 按空气质量对data进行从小到大的排序,返回一个排序后的数组
 */
function sortAqiData(data){
    while(true){
        var temp = 0;
        for(var i = 0; i < (data.length - 1); i++){
            var num = data[i];
            if(num[1] > data[i+1][1]){
                data[i] = data[i+1];
                data[i+1] = num;
                temp = 1;
            }
        }
        if(temp === 0){
            return data;
        }
    }
}


/**
 * render方法
 * 将排好序的城市及空气质量指数，输出显示到id为resort的列表中
 * 格式见ul中的注释的部分
 */
function render(data){
    var resortNode = document.getElementById("resort");
    var num = ["一", "二", "三", "四", "五", "六", "七"];
    for(var i = 0; i < data.length; i++){
        var liNode = document.createElement("li");
        liNode.innerHTML = "第" + num[i] + "名: " + data[i][0] + ": " + data[i][1];
        resortNode.appendChild(liNode);
    }
}


function btnHandle(){
    var aqiData = getData();
    aqiData = sortAqiData(aqiData);
    render(aqiData);
}


/**
 * 给sort-btn绑定一个点击事件，点击时触发btnHandle函数
 */
function init(){
    var btn = document.getElementById("sort-btn");
    btn.addEventListener("click", function(){
        btnHandle();
        btn.disabled = "true";
    });
}


window.onload = function(){
    init();
}
