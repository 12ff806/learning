/**
 * Baidu ife JavaScript task 05
 * code by sin
 * June 14 2017
 */


/* 定义全局队列 */
var listData = [];


/**
 * getData()
 * 获取输入的值,并加以判断值的合法性
 */
function getData(){
    var input = document.getElementById("num-input");
    var newValue = input.value;
    input.value = "";
    if(newValue === ""){
        showTips("你还没有输入任何值");
        return false;
    }
    else if(!isNaN(newValue) && (newValue >= 10) && (newValue <= 100)){
        showTips("");
        return parseInt(newValue);
    }
    else{
        showTips("输入不合法!请重新输入");
        return false;
    }
}


/**
 * showTips()
 * 显示各种提示信息
 */
function showTips(str){
    var show = document.getElementsByClassName("show-tips")[0];
    if(str === "" || str === null || str === undefined){
        show.innerHTML = "( •̀ .̫ •́ )";
    }
    else{
        show.innerHTML = str;
    }
}


/**
 * display()
 * 将处理好的队列展示出来
 * 并且给每个li元素添加点击事件
 */
function display(list){
    // 展示所有的List值
    var html = "";
    var dis = document.getElementById("display");
    for(var i = 0; i < list.length; i++){
        html += "<li></li>";
    }
    dis.innerHTML = html;

    var liNode = document.getElementsByTagName("li");
    for(var i = 0; i < liNode.length; i++){
        liNode[i].style.height = list[i] * 2 + "px";
        liNode[i].style.left = ((1280-liNode.length*20)/2+3+20*i) + "px";
        
        /* 当点击一个li元素删除后,其他li元素的index还是这次赋的值,
         * 并没有更新,所以连续点击li元素进行删除的话会出现BUG
         * 解决方法是在onclock响应函数里调用display()刷新这里的index值
         */
        liNode[i].index = i;
        // 为所有的li元素添加onclick事件
        liNode[i].onclick = function(){
            //this.parentNode.removeChild(this);
            //console.log(this.index);
            //console.log(list[this.index]);
            // 删除当前被点击的li元素所对应list数组中的值
            list.splice(this.index, 1);
            // 显示删除点击值后的列表,并更新index值
            display(list);
        }
    }
}


/**
 * cleanShadow()
 * 清楚列表阴影
 */
function cleanShadow(obj){
    for(var i = 0; i < obj.length; i++){
        obj[i].style.boxShadow = "none";
    }
}


/* 执行 */
window.onload = function(){
    // left in
    var btnLI = document.getElementById("left-in");
    btnLI.addEventListener("click", function(){
        if(listData.length < 60){
            var newData = getData();
            if(newData){
                listData.unshift(newData);
                display(listData);
            }
        }
        else{
            showTips("已经满60啦,不能再添加啦");
        }
    })

    // right in
    var btnRI = document.getElementById("right-in");
    btnRI.addEventListener("click", function(){
        if(listData.length < 60){
            var newData = getData();
            if(newData){
                listData.push(newData);
                display(listData);
            }
        }
        else{
            showTips("已经满60啦,不能再添加啦");
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
            showTips("不用删啦,队列已经是空的啦");
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
            showTips("不用删啦,队列已经是空的啦");
        }
    })

    /**
     * sort
     * 冒泡排序,用定时器实现的循环
     */
    var btnS = document.getElementById("sort");
    btnS.addEventListener("click", function(){
        if(listData.length >= 2){
            var i = listData.length -1;
            var j = 0;
            var liNode = document.getElementsByTagName("li");

            var timer = setInterval(function(){
                if(i > 0){
                    if(j < i){
                        cleanShadow(liNode);
                        liNode[j].style.boxShadow = "2px 4px 4px #000";
                        liNode[j+1].style.boxShadow = "2px 4px 4px #000";
                        if(listData[j] > listData[j+1]){
                            var temp = liNode[j].style.height;
                            liNode[j].style.height = liNode[j+1].style.height;
                            liNode[j+1].style.height = temp;

                            var num = listData[j];
                            listData[j] = listData[j+1];
                            listData[j+1] = num;
                        }
                        j++;
                    }
                    else{
                        liNode[i].style.backgroundColor = "#6683fe";
                        i--;
                        if(i === 0){
                            cleanShadow(liNode);
                            liNode[0].style.backgroundColor = "#6683fe";
                        }
                        j = 0;
                    }
                }
                else{
                    clearInterval(timer);
                    showTips("排序搞定");
                }
            }, 200)
        }
        else if(listData.length === 1){
            showTips("就一个值,跟谁排序啊??");
        }
        else{
            showTips("队列是空的,你让我排序??");
        }
    })
}
