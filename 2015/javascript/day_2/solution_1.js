var fs = require('fs');
var filename = 'day_2/input.txt';

fs.readFile(filename, 'utf8', function (err, data) {

    console.log('The elves should order ' + data + ' square feet of wrapping paper.');
});
