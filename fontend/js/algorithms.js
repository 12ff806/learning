/**
 * JavaScript
 * Basic Algorithm Scripting
 * Follow FCC
 * By Sins
 */

// Reverse a string - 反转字符串
function reverseString(str) {
    var strToArray = str.split("");
    var reverseArray = strToArray.reverse();
    var reverseStr = reverseArray.join("");
    return reverseStr;
}

reverseString("hello");

// Factorialize a number - 求阶乘
function factorialize(num) {
    var value = 1;
    for (var i = num; i >= 1; i--) {
        value = value * i;
    }
    return value;
}

factorialize(5);

// Title Case a Sentence - 将字符串的每个单词首字母大写，其余部分小写
function titleCase(str) {
    var strToArr1 = str.split(" ");
    var array = [];
    for (var i = 0; i < strToArr1.length; i++) {
        var strToArr2 = strToArr1[i].split("");
        strToArr2[0] = strToArr2[0].toUpperCase();
        for (var j = 1; j < strToArr2.length; j++) {
            strToArr2[j] = strToArr2[j].toLowerCase();
        }
        array[i] = strToArr2.join("");
    }
    return array.join(" ");
}

titleCase("I'm a little tea pot");      // I'm A Little Tea Pot
titleCase("sHoRt AnD sToUt");           // Short And Stout

// Check for Palindromes - 判断字符串是否回文
function palindrome(str) {
    var pattern = /\s|\,|\.|\_|\-|\(|\)|\:|\/|\\/gi;
    str = str.toLowerCase();
    str = str.replace(pattern, "");
    var strToArray = str.split("");
    var reverseArr = strToArray.reverse();
    var reverseStr = reverseArr.join("");

    if (str === reverseStr) {
        return true;
    }
    else {
        return false;
    }
}

palindrome("eye");    // true
palindrome("A man, a plan, a canal. Panama");    // true
palindrome("0_0 (: /-\ :) 0-0");    // true

// Find the Longest Word in a String - 返回句中最长单词的长度
function findLongestWord(str) {
    var num = 0;
    var strToArray = str.split(" ");
    for (var i = 0; i < strToArray.length; i++) {
        if (num < strToArray[i].length) {
            num = strToArray[i].length;
        }
    }
    return num;
}

findLongestWord("The quick brown fox jumped over the lazy dog");    // 6

// Return Largest Numbers in Arrays - 找出每个子元素数组中的最大值，串联起来形成一个新的数组
function largestOfFour(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        var num = arr[i][0];
        for (var j = 1; j < arr[i].length; j++) {
            if (num < arr[i][j]) {
                num = arr[i][j];
            }
        }
        newArr[i] = num;
    }
    return newArr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);    // [5, 27, 39, 1001]

// Confirm the Ending - 检查一个字符串（str）是否以指定字符串（target)结尾
function confirmEnding(str, target) {
    var strToArr = str.split("");
    strToArr = strToArr.reverse();
    var targetToArr = target.split("");
    targetToArr = targetToArr.reverse();
    var num = 1;
    for (var i = 0; i < targetToArr.length; i++) {
        if (strToArr[i] !== targetToArr[i]) {
            num = 0;
        }
    }
    if (num === 1) {
        return true;
    }
    else {
        return false;
    }
}

confirmEnding("Bastian, apple", "an, apple");

// Repeat a string - 重复一个字符串（str）num次
function repeat(str, num) {
    if (num <= 0) {
        return "";
    }

    var strToArr = str.split("");
    var newArr = [];
    for (var i = num; i > 0; i--) {
        for (var j = 0; j < strToArr.length; j++) {
            newArr.push(strToArr[j]);
        }
    }
    var newStr = newArr.join("");
    return newStr;
}

repeat("abc", 4);

// Truncate a string - 如果字符串比指定参数num长，则把多余部分用...表示。
function truncate(str, num) {
    if (str.length <= num) {
        return str;
    }
    else if (num <= 3) {
        return (str.slice(0, num) + "...");
    }
    else if (num > 3) {
        return (str.slice(0, num-3) + "...");
    }
}

truncate("A-tisket a-tasket A green and yellow basket", 11);    // "A-tisket..."
truncate("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length);    // "A-tisket a-tasket A green and yellow basket"

// Chunky Monkey - 把一个数组arr按照指定的数组大小size分割成若干个数组块
function chunk(arr, size) {
    var resultArr = [];
    for (var i = 0; i < arr.length; i+=size) {
        var tempArr = arr.slice(i, i+size);
        resultArr.push(tempArr);
    }
    return resultArr;
}

chunk(["a", "b", "c", "d"], 2);    // [["a", "b"], ["c", "d"]]
chunk([0, 1, 2, 3, 4, 5, 6], 3);    // [[0, 1, 2], [3, 4, 5], [6]]

// slasher Flick - 返回一个数组被截断n个元素后还剩余的元素，截断从索引0开始
// 方案1
function slasher(arr, howMany) {
    for (var i = 0; i < howMany; i++) {
        arr.shift();
    }
    return arr;
}
// 方案2
function slasher(arr, howMany) {
    arr.splice(0, howMany);
    return arr;
}

slasher([1, 2, 3], 2);    // [3]

// Mutations - 如果数组第一个字符串元素包含了第二个字符串元素的所有字符，函数返回true
function mutation(arr) {
    arr[0] = arr[0].toLowerCase();
    arr[1] = arr[1].toLowerCase();
    var searchArr = arr[1].split("");
    for (var i = 0; i < searchArr.length; i++) {
        var num = arr[0].indexOf(searchArr[i]);
        if (num === -1) {
            return false;
        }
    }
    return true;
}

mutation(["hello", "hey"]);    // false
mutation(["Mary", "Army"]);    // true

// Falsy Bouncer - 删除数组中的假值：false, null, 0, "", undefined, NaN
function bouncer(arr) {
    var filtered = arr.filter(function isFakeValue(element) {
        return element;
    });
    return filtered;
}

bouncer([7, "ate", "", false, 9]);    // [7, "ate", 9]
bouncer([false, null, 0, NaN, undefined, ""]);    // []
bouncer([1, null, NaN, 2, undefined]);    // [1, 2]

// Seek and Destroy - 第一个参数是待摧毁的数组，其余的参数是待摧毁的值
function destroyer(arr) {
    var args = [];
    for (var i = 1; i < arguments.length; i++) {
        args.push(arguments[i]);
    }
    var temp = arr.filter(function isNotEqual(item) {
        return args.indexOf(item) < 0;
    })
    return temp;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3)       // [1, 1]
destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3)    // [1, 5, 1]
destroyer([3, 5, 1, 2, 2], 2, 3, 5)       // [1]
destroyer([2, 3, 2, 3], 2, 3)             // []
destroyer(["tree", "hamburger", 53], "tree", 53)  // ["hamburger"]

// Where do I belong - 找到指定的值在数组中的位置
function where(arr, num) {
    arr.push(num);
    arr.sort(function(a, b){return a>b;})
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === num) {
            return i;
        }
    }
}

where([10, 20, 30, 40, 50], 35)    // 3
where([10, 20, 30, 40, 50], 30)    // 2
where([40, 60], 50)                // 1
where([3, 10, 5], 3)               // 0
where([5, 3, 20, 3], 5)            // 2
where([2, 20, 10], 19)             // 2
where([2, 5, 10], 15)              // 3

// Caesars Cipher - ROT13密码会移位13个位置，'A-N','B-O'.实现输入加密字符串，输出解密字符串。
function rot13(str) {
    var arr = str.split("");
    var temp = [];
    for (var i = 0; i < arr.length; i++) {
        temp[i] = arr[i].charCodeAt(0);
        if (arr[i].charCodeAt(0) >= 78 && arr[i].charCodeAt(0) <= 90) {
            temp[i] = arr[i].charCodeAt(0) - 13;
        }
        if (arr[i].charCodeAt(0) >= 65 && arr[i].charCodeAt(0) < 78) {
            temp[i] = arr[i].charCodeAt(0) - 13 + 26;
        }
    }
    var newArr = [];
    for (var j =0; j < temp.length; j++) {
        newArr[j] = String.fromCharCode(temp[j]);
    }
    return newArr.join("");
}

rot13("SERR PBQR PNZC");    // FREE CODE CAMP
rot13("SERR CVMMN!");       // FREE PIZZA!
