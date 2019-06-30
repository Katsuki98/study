'use strict'

function generate(testLengthArray){
  let result = [];
  for(let i = 0; i < testLengthArray.length; i++) {
    let inputLength = testLengthArray[i];
    let item = {
      input: [],
      target: null,
      output: null,
    }

    for(let j = 0; j < inputLength; j++) {
      let randomNum = Math.floor(Math.random()*20000 - 9999);
      item.input.push(randomNum); 
    }

    item.input.sort(function(a, b) {return a-b});
    item.target = Math.floor(Math.random()*20000 - 9999);
    item.output = item.input.indexOf(item.target);

    result.push(item);
  }

  testLengthArray.forEach(function(item, index, arr) {

  })
  
  return result;
}

module.exports = generate
