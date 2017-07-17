/**
 * table sort
 * by Sin
 * 01 July 2017
 */


var Table = function(mountPoint, tableData){
    this.mountPoint = mountPoint;
    this.tableHeader = tableData.header;
    this.tableContent = tableData.content;

    var thisTable = this;

    var tableNode = document.createElement("table");
    this.mountPoint.appendChild(tableNode);
    
    this.showHeader = function(){
        var tHeaderNode = document.createElement("thead");
        var trNode = document.createElement("tr");

        for(var i = 0; i < this.tableHeader.length; i++){
            var thNode = document.createElement("th");
            thNode.innerHTML = this.tableHeader[i].label;

            if(this.tableHeader[i].sortable){
                var upDivNode = document.createElement("div");
                var downDivNode = document.createElement("div");
                upDivNode.className = "upsort";
                downDivNode.className = "downsort";
                thNode.appendChild(upDivNode);
                thNode.appendChild(downDivNode);

                upDivNode.index = i;
                downDivNode.index = i;

                upDivNode.addEventListener("click", function(){
                    var j = thisTable.tableHeader[this.index].name;
                    thisTable.tableContent.sort(function(a, b){
                        return a[j] - b[j];
                    })
                    thisTable.showContent();
                }, false);

                downDivNode.addEventListener("click", function(){
                    var j = thisTable.tableHeader[this.index].name;
                    thisTable.tableContent.sort(function(a, b){
                        return b[j] - a[j];
                    })
                    thisTable.showContent();
                }, false);
            }
            trNode.appendChild(thNode);
        }

        tHeaderNode.appendChild(trNode);
        tableNode.appendChild(tHeaderNode);
    }

    this.showContent = function(){
        var tBodyNode = document.getElementsByTagName("tbody")[0];
        if(tBodyNode){
            tableNode.removeChild(tBodyNode);
        }

        var tBodyNode = document.createElement("tbody");
        for(var i = 0; i < this.tableContent.length; i++){
            var trNode = document.createElement("tr");
            for(var key in this.tableContent[i]){
                var tdNode = document.createElement("td");
                tdNode.innerHTML = this.tableContent[i][key];
                trNode.appendChild(tdNode);
            }
            tBodyNode.appendChild(trNode);
        }
        tableNode.appendChild(tBodyNode);
    }
}


function init(){
    var tableData = {
        header: [
            {
                name: "name",
                label: "姓名",
                sortable: false
            },
            {
                name: "chinese",
                label: "语文",
                sortable: true
            },
            {
                name: "math",
                label: "数学",
                sortable: true
            },
            {
                name: "english",
                label: "英语",
                sortable: true
            },
            {
                name: "total",
                label: "总分",
                sortable: true
            }
        ],
        content: [
            {
                name: "小白",
                chinese: 90,
                math: 100,
                english: 70,
                total: 260
            },
            {
                name: "小红",
                chinese: 100,
                math: 70,
                english: 80,
                total: 250
            },
            {
                name: "小绿",
                chinese: 80,
                math: 90,
                english: 90,
                total: 260
            },
            {
                name: "小黄",
                chinese: 70,
                math: 80,
                english: 100,
                total: 250
            },
            {
                name: "小紫",
                chinese: 83,
                math: 92,
                english: 80,
                total: 255
            }
        ]
    };

    var tableWrap = document.getElementById("table-wrap");
    var table = new Table(tableWrap, tableData);
    table.showHeader();
    table.showContent();
}


window.onload = function(){
    init();
}
