/**
 * DanMu
 * by Sin
 * 05 July 2017
 */


/**
 * 获取输入的弹幕内容并校验
 */
function get_content() {
    var contentNode = document.querySelector("#content");
    var content = contentNode.value;

    if(content.length <= 0 || (/^\s+$/).test(content)) {
        alert("输入不合法,请重新输入!");
        return false;
    }
    else {
        return content;
    }
}


/**
 * 把获取到的弹幕内容显示到屏幕上
 */
function show() {
    var content = get_content();
    if(content) {
        var movieBoxNode = document.querySelector("#movie-box"); 
        var spanNode = document.createElement("span");
        
        spanNode.innerHTML = content;
        spanNode.style.top = ~~(Math.random() * (movieBoxNode.offsetHeight - spanNode.offsetHeight)) + "px";
        spanNode.style.left = movieBoxNode.offsetWidth + "px";
        spanNode.style.color = "#" + (~~(Math.random() * (1<<24))).toString(16);
        spanNode.style.fontSize = ~~(Math.random() * 8 + 16) + "px";
        movieBoxNode.appendChild(spanNode);

        var speed = ["linear", "ease-out"][~~(Math.random() * 2)];
        var left = spanNode.offsetLeft;

        var timer = setInterval(function() {
            if(left < -(spanNode.offsetWidth)) {
                clearInterval(timer);
                spanNode.parentNode.removeChild(spanNode);
                return;
            }
            switch(speed) {
                case "linear":
                    left = left - 8;
                    spanNode.style.left = left + "px";
                    break;
                case "ease-out":
                    if(left > 200) {
                        left += (0 - left)* .02;
                    }
                    else if(left <= 200) {
                        left = left - 4;
                    }
                    spanNode.style.left = left + "px";
                    break;
                default:
                    break;
            }
        }, 60);
    }
}


/**
 * 监听提交按钮点击事件
 */
function init() {
    var btnNode = document.querySelector("#btn");
    var contentNode = document.querySelector("#content");

    btnNode.addEventListener("click", show, false);
    contentNode.addEventListener("keydown", function(event) {
        if(event.keyCode === 13){
            show();
        }
    }, false);
}


window.onload = function() {
    init();
}
