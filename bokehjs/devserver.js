var express = require('express');
var app = express();
var appRoot = require('app-root-path');

app.route("/")
    .get((req, res) => {
        res.status(200).send({msg: "HELLO"});
    });

app.route("/test")
    .get((req, res) => {
        res.sendFile("base_test.html", { root: appRoot.toString() });
    });
app.use("/build", express.static(__dirname + '/build'));

// start server and listens on a port
app.set('port', process.env.PORT || 3000);
var server = app.listen(app.get('port'), function() {
    console.log('Express server listening on port ' + server.address().port);
});
