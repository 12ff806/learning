/**
 * JS create object method
 * by sin
 * June 22 2017
 * last update: 08 July 2017
 */





/**
 * 字面量方式
 */
var person = {
    name: ["Bob", "Smith"],
    age: 24,
    gender: "male",
    interests: ["music", "skiing"],
    bio: function(){
        console.log(this.name[0] + " " + this.name[1] + " is " + this.age + " years old. He likes " + this.interests[0] + " and " + this.interests[1] + ".");
    },
    greeting: function(){
        console.log("Hi! I'm " + this.name[0] + ".");
    }
};

console.log(person.name[0]);
console.log(person.age);
console.log(person.gender);
console.log(person.interests[1]);
person.bio();
person.greeting();
person.__proto__ === Object.prototype       // true (验证原型)
person instanceof Object                    // true (验证继承关系)





/**
 * 工厂模式
 */
function createNewPerson(name, job){
    var obj = {};                       // var obj = new Object();
    obj.name = name;
    obj.job = job;
    obj.greeting = function(){
        console.log("Hi! I'm " + this.name);
    };
    return obj;
}

var sin = createNewPerson("Sin", "Coding");
var janus = createNewPerson("Janus", "coding")
console.log(sin.name);
sin.greeting();
sin.__proto__ === Object.prototype      // true (验证原型)
sin instanceof Object                   // true (验证继承关系)
sin.greeting === janus.greeting         // false (两个不同的实例方法)





/**
 * 构造函数
 * 其实就是一个普通的函数
 * 需要使用new调用这个函数来创建对象
 * 使用new后会自动执行如下操作
 *     a). 创建一个新对象
 *     b). Person1.prototype指向新对象的原型对象
 *     c). 这个新对象会绑定到函数调用的this
 *     d). 返回this 即新对象
 * 缺点: 每个方法都要在每个实例上重新创建一次
 */
function Person1(name, job){
    this.name = name;
    this.job = job;
    this.greeting = function(){
        console.log("Hi! I'm " + this.name);
    };
}

var person1 = new Person1("Bob", "coding");
var person2 = new Person1("Sarah", "coding");
console.log(person1.name);
person1.greeting();
console.log(person2.name);
person2.greeting();
person1.greeting === person2.greeting                    // false (两个不同的实例方法)
person1.__proto__ === Person1.prototype                  // true (验证原型)
person1 instanceof Person1                               // true (验证继承关系)
person1.constructor === Person1.prototype.constructor    // true (person1的属性constructor指向Person1)
Person1.prototype.constructor === Person1                // true
Object.getPrototypeOf(person1) === Person1.prototype     // true





/**
 * 原型模式
 * 优点: 所有的实例可共享所包含的属性和方法
 * 缺点: 所有实例的属性都是共享的
 *       对于那些包含值类型的属性勉强没问题
 *       因为实例的属性可以屏蔽原型的属性
 *       但是引用类型的值就会出现问题
 */

/* example one */
function Cat() {
}

Cat.prototype.name = "Tom";
Cat.prototype.color = "black";
Cat.prototype.friends = ["Jack", "Jerry"];
Cat.prototype.yell = function() {
    console.log(this.name + "'s yell is miaow ~");
}

var cat = new Cat();
var cat1 = new Cat();
console.log(cat.friends)                       // ["Jack", "Jerry"]
cat1.friends.push("Lily");
console.log(cat1.friends);                     // ["Jack", "Jerry", "Lily"]
console.log(cat.friends);                      // ["Jack", "Jerry", "Lily"]
console.log(cat.friends === cat1.friends);     // true

/**
 * example two
 * 缺点: 将Dog.prototype的值设置为一个以对象字面量形式创建的对象
 *       相当于重写了默认的Dog.prototype对象
 *       会导致Dog.prototype.constructor属性丢失
 */
function Dog() {
}

Dog.prototype = {
    // constructor: Dog,    // 如果需要这个属性的话,可以像这样手动添加.不过这种方式不够好,因为constructor属性默认是不可枚举的.这样直接设置,它将是可枚举的
    name: "Jerry",
    color: "brown",
    sayName: function() {
        console.log(this.name)
    }
}

// 像上面手动添加constructor属性的方式不够好,因为constructor属性默认是不可枚举的.这样直接设置,它将是可枚举的.所以可以使用Object.defineProperty方法
Object.defineProperty(Dog.prototype, "constructor", {
    enumerable: false,
    value: Dog
})

var dog1 = new Dog();





/**
 * 构造函数 && 原型模式
 */
function Person(first, last, age, gender, interests){
    /** same as below
    this.name = {
        first: first,
        last: last
    };
    */
    this.name = {
        first,
        last
    };
    this.age = age;
    this.gender = gender;
    this.interests = interests;
    this.bio = function(){
        console.log(this.name.first + " " + this.name.last + " is " + this.age + " years old. He likes " + this.interests[0] + " and " + this.interests[1] + ".");
    };
    this.greeting = function(){
        console.log("Hi! I'm " + this.name.first + ".");
    };
}

var person3 = new Person("Bob", "Smith", 42, "male", ["music", "skiing"]);
console.log(person3["age"]);
console.log(person3.interests[1]);
person3.bio();
person3.greeting();

/* 在prototype属性上创建的方法,所有实例都共享同一个方法 */
Person.prototype.farewell = function(){
    console.log(this.name.first + " has left the building. Bye for now!");
};

person3.farewell();





/**
 * Using the Object()
 */
var person4 = new Object();
person4.name = "Chris";
person4["age"] = 24;
person4.greeting = function(){
    console.log("Hi I'm " + this.name + ".");
};

/* or */
var person5 = new Object({
    name: "Chris",
    age: 24,
    greeting: function(){
        console.log("Hi I'm " + this.name + ".");
    }
});





/**
 * Using the create() method
 * which allows you to create a new object instance based on an existing object
 */
var person6 = Object.create(person5);
console.log(person6.name);
console.log(person6.age);
person6.greeting();
console.log(person6.__proto__ === person5)    // true





/**
 * 常用的方式: 构造函数 && 原型模式
 * 所有的属性在构造函数里创建
 * 所有的方法在prototype上创建
 */
function Student(props={}) {
    this.name = props.name || "Anonymous";
    this.grade = props.grade || 1;
}

Student.prototype.hello = function() {
    console.log("Hello, " + this.name + "!");
}

// 避免遗漏new, 所以做个简单的封装
function createStudent(props) {
    return new Student(props || {});
}

xiaoming = createStudent({name:"xiaoming"});
console.log(xiaoming.name);
console.log(xiaoming.grade);
xiaoming.hello()
xiaohong = createStudent({name:"xiaohong"});
xiaohong.__proto__ === Student.prototype        // true
xiaoming.__proto__ === Student.prototype        // true
xiaoming.hello === xiaohong.hello               // true
xiaoming instanceof Student                     // true
xiaohong instanceof Student                     // true
