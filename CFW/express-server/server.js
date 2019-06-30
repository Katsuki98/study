const express = require('express');
const app = express(); //server role

//Router
// app.use(express.static(__dirname + "/html & css"));

app.get('/', function(request, response) {
    response.send('Hello world!');
});

app.get('/about', function(req, res) {
    // res.send('<h1>Katsuki</h1>');
    res.sendFile(__dirname + '/html & css/index.html')
})

app.use(express.static('html & css'));
app.use('/public', express.static('html & css'));

// app.get('style.css', function(req, res) {
//     res.sendFile(_dirname + '/html & css/style.css');
// });

app.listen('4869', function(err) {
    if(err) console.log(err)
    else console.log('Server start success!!!');
})