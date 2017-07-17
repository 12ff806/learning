/**
 * Baidu ife JavaScript task 04
 * code by sin
 * June 12 2017
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
        alert("你还没有输入任何值");
        return false;
    }
    else if(!isNaN(newValue)){
        return newValue;
    }
    else{
        alert("输入不合法!请重新输入");
        return false;
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
        html += "<li>" + list[i] + "</li>";
    }
    dis.innerHTML = html;

    // 为所有的li元素添加onclick事件
    var liNode = document.getElementsByTagName("li");
    for(var i = 0; i < liNode.length; i++){
        /* 当点击一个li元素删除后,其他li元素的index还是这次赋的值,
         * 并没有更新,所以连续点击li元素进行删除的话会出现BUG
         * 解决方法是在onclock响应函数里调用display()刷新这里的index值
         */
        liNode[i].index = i;
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


/* 执行 */
window.onload = function(){
    // left in
    var btnLI = document.getElementById("left-in");
    btnLI.addEventListener("click", function(){
        var newData = getData();
        if(newData){
            listData.unshift(newData);
            display(listData);
        }
    })

    // right in
    var btnRI = document.getElementById("right-in");
    btnRI.addEventListener("click", function(){
        var newData = getData();
        if(newData){
            listData.push(newData);
            display(listData);
        }
    })

    // left out
    var btnLO = document.getElementById("left-out");
    btnLO.addEventListener("click", function(){
        if(listData.length > 0){
            var delItem = listData.shift();
            alert(delItem);
            display(listData);
        }
        else{
            alert("不用删啦,队列已经是空的啦");
        }
    })

    // right out
    var btnRO = document.getElementById("right-out");
    btnRO.addEventListener("click", function(){
        if(listData.length > 0){
            var delItem = listData.pop();
            alert(delItem);
            display(listData);
        }
        else{
            alert("不用删啦,队列已经是空的啦");
        }
    })
}
