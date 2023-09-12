#!/usr/bin/node
const array = require('./100-data').list;
const newarray = array.map((n, i) => (n * i));
console.log(array);
console.log(newarray);
