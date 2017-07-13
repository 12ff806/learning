/**
 * floating layer
 * by Sin
 * 28 June 2017
 */


var Floatinglayer = function(config={}){
    this.scroll = config.scroll || "no";
    this.move = config.move || "yes";
    this.resize = config.resize || "no";
    this.width = config.width || 400;
    this.height = config.height || 300;
    this.title = config.title || "Tips";
    this.content = config.content || "Here is the tips";
    this.button = config.button || "no";

    // create and show the floating layer
    this.show = function(){
        var bodyNode = document.getElementsByTagName("body")[0];
        
        // create mask
        var fullScreen = document.createElement("div");
        fullScreen.id = "full-screen";
        fullScreen.className = "fullscreen";
        bodyNode.appendChild(fullScreen);

        // create floating layer 
        var floatLayer = document.createElement("div");
        floatLayer.id = "float-layer";
        floatLayer.className = "floatlayer";
        floatLayer.style.width = this.width+"px";
        floatLayer.style.height = this.height+"px";
        bodyNode.appendChild(floatLayer);
        
        // title
        var flTitle = document.createElement("div");
        flTitle.className = "fltitle";
        flTitle.innerHTML = this.title;
        floatLayer.appendChild(flTitle);

        // content
        var flContent = document.createElement("div");
        flContent.className = "flcontent";
        flContent.innerHTML = this.content;
        floatLayer.appendChild(flContent);

        if(this.button === "yes"){
            var flBtnWrap = document.createElement("div");
            var flButton1 = document.createElement("button");
            var flButton2 = document.createElement("button");
            flBtnWrap.className = "flbtnwrap";
            flButton1.innerHTML = "确定";
            flButton1.className = "flbutton";
            flButton2.innerHTML = "取消";
            flButton2.className = "flbutton";

            flBtnWrap.appendChild(flButton1);
            flBtnWrap.appendChild(flButton2);
            floatLayer.appendChild(flBtnWrap);

            flButton1.addEventListener("click", this.close, false);
            flButton2.addEventListener("click", this.close, false);
        }

        if(this.scroll === "no"){
            bodyNode.style.overflowY = "hidden";
            
            /*
            window.addEventListener("wheel", function(event){
                event.preventDefault();
            });
            */
        }

        if(this.move === "yes"){
            var offsetTop;
            var offsetLeft;

            function mousedown(event){
                var flTop = floatLayer.offsetTop;
                var flLeft = floatLayer.offsetLeft;
                offsetTop = event.clientY - flTop;
                offsetLeft = event.clientX - flLeft;
                document.body.addEventListener("mousemove", mousemove);
                document.addEventListener("mouseup", mouseup); 
            }
            
            function mousemove(event){
                floatLayer.style.top = (event.clientY - offsetTop) + "px";
                floatLayer.style.left = (event.clientX - offsetLeft) + "px";
            }

            function mouseup(){
                document.body.removeEventListener("mousemove", mousemove);
                document.removeEventListener("mouseup", mouseup); 
            }

            flTitle.addEventListener("mousedown", mousedown);
            
            /*
            console.log(floatLayer.offsetWidth);     // floatLayer的width + padding + border: offsetWidth = clientWidth + 滚动条 + 边框
            console.log(floatLayer.offsetHeight);    // floatLayer的height + padding + border: offsetHeight = clientHeight + 滚动条 + 边框
            console.log(floatLayer.scrollWidth);     // floatLayer中内容的宽度 + padding: 如果内容宽度小于clientWidth, 则等于clientWidth
            console.log(floatLayer.scrollHeight);    // floatLayer中内容的高度 + padding: 如果内容高度小于clientHeight, 则等于clientHeight
            console.log(floatLayer.clientWidth);     // floatLayer的width + padding: 不包括边框 滚动条等
            console.log(floatLayer.clientHeight);    // floatLayer的height + padding: 不包括边框 滚动条等
            */
        }

        if(this.resize === "yes"){
            floatLayer.style.resize = "both";
            floatLayer.style.overflow = "auto";
        }
    }

    // close the floating layer
    this.close = function(){
        var bodyNode = document.getElementsByTagName("body")[0];
        var fullScreen = document.getElementById("full-screen");
        var floatLayer = document.getElementById("float-layer");

        bodyNode.removeChild(floatLayer);
        bodyNode.removeChild(fullScreen);
        bodyNode.style.overflowY = "scroll";
        
        var btnNode = document.getElementById("btn");
        btnNode.disabled = false;
    }
}

