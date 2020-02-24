// Author: Muhammad F. Khan
// FileName: quick_server.js
// Description: Allows user to quickly create a web server in nodejs
// License: MIT

var http = require('http'); // http module - comes by default
const fs = require("fs"); // file-system module

// route configuration
var config = {
	port: 8080,
	routes: [
		{
			path: "/",
			methods: ["GET", "POST"],
			response: "Hello World"
		},
		{
			path: "/about",
			methods: ["GET"],
			response: {
				type: "text",
				body: "<p>u wanna learn about me??</p> <img src='https://media3.giphy.com/media/l44QoAtMOGDhYjjVu/giphy.gif' />"}
		},
		{
			path: "/contact",
			methods: ["GET","POST"],
			response: {
				type: "file",
				path: "./file.json"
			}
		},
	],
	reject: "No No No"
}



http.createServer(function (req, res) {
	res.writeHead(200, { 'Content-Type': 'text/html' }); // sending status code + 
	response = config.reject; // by default return rejection msg

	config.routes.forEach((route) => { // search through all routes
		if (req.url === route.path && route.methods.includes(req.method)){ // if a request type and path are valid
			// returns appropirate response depending on response type
			if (route.response.type == "text"){
				response = route.response.body;
			} else {
				response = fs.readFileSync("./response_file.html");
			}
		}
	})

	// returning response
	res.write(response);
	res.end(); // ending connection
}).listen(config.port);  // Starting Listener on port 8080 - config.port
