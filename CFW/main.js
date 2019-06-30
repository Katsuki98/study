// // aFunc(); // => Run

// function aFunc(a, b, c) {
//     // Code
//     console.log(a);
//     console.log(b);
//     console.log(c);
// }

// // bFunc() // => Error

// const bFunc = function(callback) {
//     // executed something.....
//     callback(10, 15, 20);
// }

// bFunc(aFunc); // =>Run

// const cFunc = () => {

// }

// console.log('Begin');
// setTimeout(function() {
//     console.log('Hello');
// }, 1000);
// console.log('End');

// var a =15;

// function aFunc() {
//     var b =10;

//     function bFunc() {
//         var c = 20;

//         console.log(a); //15
//         console.log(b); //10
//         console.log(c); //20
//     }
//     console.log(a); //15
//     console.log(b); //10
//     console.log(c); //undefined
// }

// aFunc();

// console.log(a); //15
// console.log(b); //undefined

// for(var i = 0; i < 1; i++) {

// }
// console.log(i);

//block scope { }
const countDown = function(count) {
    for(let i = count; i >= 0; i--) {
        // const a = i;
        setTimeout(function() {
            console.log(i);
        }, 1000*(count - i));
    }
}

countDown(10);