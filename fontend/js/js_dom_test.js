window.onload = function(){
    var trNodes = document.getElementsByTagName("tr");
    for(var i = 0; i < trNodes.length; i++){
        trNodes[i].onmouseover = function(){
            this.style.backgroundColor = "#F2F2F2";
        }
        trNodes[i].onmouseout = function(){
            this.style.backgroundColor = "#FFFFFF";
        }
    }
}

var num = 2;
function add(){
    num++;
    var tableNode = document.getElementById("table");
    var newtr = document.createElement("tr");
    var newtd1 = document.createElement("td");
    var newtd2 = document.createElement("td");
    var newtd3 = document.createElement("td");

    newtd1.innerHTML = "A" + num;
    newtd2.innerHTML = "第" + num + "个学生";
    newtd3.innerHTML = "<a href='javascript:;' onclick='del(this)'>删除</a>"

    newtr.appendChild(newtd1);
    newtr.appendChild(newtd2);
    newtr.appendChild(newtd3);

    tableNode.appendChild(newtr);

    var trNodes = document.getElementsByTagName("tr");
    for(var i = 0; i < trNodes.length; i++){
        trNodes[i].onmouseover = function(){
            this.style.backgroundColor = "#F2F2F2";
        }
        trNodes[i].onmouseout = function(){
            this.style.backgroundColor = "#FFFFFF";
        }
    }
}

function del(obj){
    num--;
    var tableNode = obj.parentNode.parentNode.parentNode;
    var trNode = obj.parentNode.parentNode;
    tableNode.removeChild(trNode);
}
