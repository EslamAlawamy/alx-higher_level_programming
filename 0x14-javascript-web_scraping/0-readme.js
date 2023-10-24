#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, contents) {
  if (contents === undefined) {
    console.log(error);
  } else {
    console.log(contents);
  }
});
