var teodio = 'Te quiero';
var output = '';
var len = 20;

for (let i = 0; i < (len/2) + 1; i++) {
  output += '*';
  for (let j = 0; j < len; j++) {
    output += ((i > 0 && i < len/2) && (j >= 0 && j < len)) ? 
              ((j === (len / 4)) && (i === (len / 4))) ? 
              teodio : (((j > len / 4) && (j < (len / 2) + 4)) && (i === (len / 4))) ? '' : ' ' : '*';
  }
  output += '*\n';
}

console.log(output);