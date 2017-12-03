var fs = require('fs');
var filename = 'day_1/input.txt';

fs.readFile(filename, 'utf8', function (err, data) {

  var i = 0;
  var floor = 0;
  while ( i < data.length ) {
    floor += (data.charAt(i) === '(' ? 1 : -1);
    if (floor < 0) {
      console.log('At the '+i+'th floor.');
      return;
    }
    i++;
  }

});
