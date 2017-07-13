window.onload = function(){
    var tabmenuul = document.getElementById("tabmenu");
    var tabmenu =tabmenuul.getElementsByTagName("li");
    var div = document.getElementById("tablist");
    var divlist = div.getElementsByTagName("div");

    for(var i = 0; i < tabmenu.length; i++){
        tabmenu[i].index = i;
        tabmenu[i].onmouseover = function(){
            for(var j = 0; j < tabmenu.length; j++){
                tabmenu[j].className = "";
            }
            this.className = "active";

            for(var k = 0; k < divlist.length; k++){
                divlist[k].className = "hide";
            }
            divlist[this.index].className = "show";
        }
    }
}
