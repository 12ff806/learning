/**
 * MoveBox JS
 * by Sin
 * 23 June 2017
 */


/**
 * Object DrawPlayground
 * draw playground
 */
var DrawPlayground = function(mountPoint, x=10, y=10){

    this.mountPoint = mountPoint;
    this.x = x;
    this.y = y;

    this.render = function(){
        var container = document.getElementById("container");
        var xul = document.createElement("ul");
        var yul = document.createElement("ul");
        var playground = document.createElement("div");

        this.mountPoint.appendChild(xul);
        this.mountPoint.appendChild(yul);
        this.mountPoint.appendChild(playground);
        
        container.style.width = `${52*this.x+100}px`;
        this.mountPoint.style.width = `${52*this.x}px`;
        playground.className = "playground";
        playground.style.width = `${52*this.x}px`;
        playground.style.height = `${52*this.y}px`;

        for(var i = 0; i < this.x; i++){
            var xli = document.createElement("li");
            xli.innerHTML = i+1;
            xli.className = "xli";
            xli.style.left = `${52*i+52+14}px`;
            xul.appendChild(xli);
        }

        for(var i = 0; i < this.y; i++){
            var yli = document.createElement("li");
            yli.innerHTML = i+1;
            yli.className = "yli";
            yli.style.top = `${52*i+52+14}px`;
            yul.appendChild(yli);
        }

        for(var i = 0; i < this.y; i++){
            for(var j = 0; j < this.x; j++){
                var lb = document.createElement("div");
                lb.className = "little-box";
                lb.style.top = `${52*i}px`;
                lb.style.left = `${52*j}px`;
                playground.appendChild(lb);
            }
        }
    }
}


/**
 * Object MoveBox
 */
var MoveBox = function(playground, x, y){
    this.playground = playground;
    this.currentDirection = "E";
    this.hPosition = 0;
    this.vPosition = 0;

    this.create = function(){
        var box = document.createElement("div");
        this.playground.appendChild(box);
        box.className = "box";
        return box;
    }

    this.render = function(box){
        box.style.top = `${this.vPosition*52+1}px`;
        box.style.left = `${this.hPosition*52+1}px`;
        
        switch(this.currentDirection){
            case "E":
                box.style.backgroundImage = "linear-gradient(to left, blue, blue 25%, red 25%, red)";
                break;
            case "N":
                box.style.backgroundImage = "linear-gradient(to bottom, blue, blue 25%, red 25%, red)";
                break;
            case "W":
                box.style.backgroundImage = "linear-gradient(to right, blue, blue 25%, red 25%, red)";
                break;
            case "S":
                box.style.backgroundImage = "linear-gradient(to top, blue, blue 25%, red 25%, red)";
                break;
            default:
                box.style.backgroundImage = "linear-gradient(to left, blue, blue 25%, red 25%, red)";
                break;
        }
    }

    this.go = function(){
        switch(this.currentDirection){
            case "E":
                if(this.hPosition < (x-1)){
                    this.hPosition = this.hPosition + 1;
                }
                break;
            case "N":
                if(this.vPosition > 0){
                    this.vPosition = this.vPosition - 1;
                }
                break;
            case "W":
                if(this.hPosition > 0){
                    this.hPosition = this.hPosition - 1;
                }
                break;
            case "S":
                if(this.vPosition < (y-1)){
                    this.vPosition = this.vPosition + 1;
                }
                break;
        }
    }

    this.turnTo = function(direction){
        switch(this.currentDirection){
            case "E":
                if(direction === "LEFT"){
                    this.currentDirection = "N"; 
                }
                else if(direction === "RIGHT"){
                    this.currentDirection = "S"; 
                }
                else if(direction === "BACK"){
                    this.currentDirection = "W"; 
                }
                break;
            case "N":
                if(direction === "LEFT"){
                    this.currentDirection = "W"; 
                }
                else if(direction === "RIGHT"){
                    this.currentDirection = "E"; 
                }
                else if(direction === "BACK"){
                    this.currentDirection = "S"; 
                }
                break;
            case "W":
                if(direction === "LEFT"){
                    this.currentDirection = "S"; 
                }
                else if(direction === "RIGHT"){
                    this.currentDirection = "N"; 
                }
                else if(direction === "BACK"){
                    this.currentDirection = "E"; 
                }
                break;
            case "S":
                if(direction === "LEFT"){
                    this.currentDirection = "E"; 
                }
                else if(direction === "RIGHT"){
                    this.currentDirection = "W"; 
                }
                else if(direction === "BACK"){
                    this.currentDirection = "N"; 
                }
                break;
        }
    }
}


/**
 * function init()
 * 初始化playground box
 * 监听按钮点击事件,并响应
 */
function init(){
    var x = 10,
        y = 10;
    
    var mp = document.getElementById("mount-point");
    var drawPlayground = new DrawPlayground(mp, x, y);
    drawPlayground.render();
    
    var playgroundNode = mp.getElementsByTagName("div")[0];
    var moveBox = new MoveBox(playgroundNode, x, y);
    var box = moveBox.create();
    moveBox.render(box);

    var input = document.getElementById("cmd-input");
    var exeBtn = document.getElementById("cmd-execution");
    function exeCommand(){
        var inputValue = input.value.trim();
        if(!inputValue){
            return;
        }
        else{
            var cmd = inputValue.split(/\s+/);
            switch(cmd[0].toUpperCase()){
                case "GO":
                    moveBox.go();
                    moveBox.render(box);
                    break;
                case "TUN":
                case "TURN":
                    moveBox.turnTo(cmd[1].toUpperCase());
                    moveBox.render(box);
                    break;
                default:
                    alert("Invalid Command!");
            }
        }
    }
    
    exeBtn.addEventListener("click", exeCommand, false);
    window.addEventListener("keypress", function(e){
        if(e.keyCode === 13){
            exeCommand();
        }
    }, false);
}


window.onload = function(){
    init();
}
