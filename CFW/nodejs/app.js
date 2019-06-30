// console.log('Hello world');
// const fs = require('fs');
// const obj = {
//     a: 10,
//     b: 25
// }

// const objToJSON = JSON.stringify(obj);
// console.log('begin');
// fs.writeFile('test.txt', objToJSON, function(err) {
//     if(err) console.log('Error!!!', err);
//     else console.log('Write file success!');
// })

// fs.readFile('test.txt', { encoding: 'utf-8' }, function(err, data) {
//     if(err) console.log('Error!!!', err);
//     else {
//         jsonToObj = JSON.parse(data);
//         console.log(jsonToObj.a);
//     }
// });
// console.log('end');

// try {
//     console.log('begin sync');
//     fs.writeFileSync('testSync.txt', objToJSON);

//     const data = fs.readFileSync('testSync.txt', { encoding: 'utf8' })
//     console.log(data);
//     console.log('end sync');
// } catch (error) {
//     console.log(error);
// }

const fileCtrl = require('./fileController');

// const readFileCustom = fileCtrl.readFileCustom;
const { readFileCustom, writeFileCustom } = fileCtrl;
console.log(fileCtrl.readFileCustom('test.txt'));
