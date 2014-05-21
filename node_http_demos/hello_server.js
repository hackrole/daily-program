var http = require('http');

var server = http.createServer(function(req, res){
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 202;
    res.end('hello world');
});

server.listen(3000, '127.0.0.1');
