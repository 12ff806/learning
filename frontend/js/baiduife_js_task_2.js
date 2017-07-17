/*
 * code by sin
 * June 10 2017
 */

var aqiData = [
    ["北京", 90],
    ["上海", 50],
    ["福州", 10],
    ["广州", 50],
    ["成都", 90],
    ["西安", 100]
];

// 定义分析函数, 用来筛选出aqi>60的城市
function analysisAqi(data){
    var arr = [];
    for(var i = 0; i < data.length; i++){
        if(data[i][1] > 60){
            arr.push(data[i]);
        }
    }
    return arr;
}

// 定义排序函数, 对这里的二维数组进行排序
function sortArr(arr){
    while(true){
        var temp = 0;
        for(var i = 0; i < arr.length-1; i++){
            var num = arr[i];
            if(num[1] < arr[i+1][1]){
                arr[i] = arr[i+1];
                arr[i+1] = num;
                temp = 1;
            }
        }
        if(temp === 0){
            return arr;
        }
    }
}

window.onload = function(){
    var aqiList = document.getElementById("aqi-list");
   
    var num = ["一", "二", "三", "四", "五", "六"];
    var aqiarr = sortArr(analysisAqi(aqiData));
    for(var i = 0; i < aqiarr.length; i++){
        var liNode = document.createElement("li");
        liNode.innerHTML = "第" + num[i] + "名: " + aqiarr[i][0] + ", " + aqiarr[i][1];
        aqiList.appendChild(liNode);
    }
}
