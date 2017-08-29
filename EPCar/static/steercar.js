$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/steercar/");

    chatsock.onopen = function() {
           console.log("Connected!");
           $('#sensor').text("Connected!");
           chatsock.send("Connected!");
    };

    chatsock.onmessage = function(message) {
        console.log("Received Sock message!");
        console.log(message);
    };
    
	$(document).on("vmousedown", ".steer_forward_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_1");
	});
	
	$(document).on("vmouseup", ".steer_forward_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_1");
	});
	
	$(document).on("vmousedown", ".steer_forward_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_2");
	});
	
	$(document).on("vmouseup", ".steer_forward_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_2");
	});
	
	$(document).on("vmousedown", ".steer_forward_3", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_3");
	});
	
	$(document).on("vmouseup", ".steer_forward_3", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_3");
	});
	
	$(document).on("vmousedown", ".steer_forward_left_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_left_1");
	});
	
	$(document).on("vmouseup", ".steer_forward_left_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_left_1");
	});
	
	$(document).on("vmousedown", ".steer_forward_left_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_left_2");
	});
	
	$(document).on("vmouseup", ".steer_forward_left_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_left_2");
	});
	
	$(document).on("vmousedown", ".steer_forward_right_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_right_1");
	});
	
	$(document).on("vmouseup", ".steer_forward_right_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_right_1");
	});
	
	$(document).on("vmousedown", ".steer_forward_right_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_forward_right_2");
	});
	
	$(document).on("vmouseup", ".steer_forward_right_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_forward_right_2");
	});
	
	$(document).on("vmousedown", ".steer_backward_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_1");
	});
	
	$(document).on("vmouseup", ".steer_backward_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_1");
	});
	
	$(document).on("vmousedown", ".steer_backward_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_2");
	});
	
	$(document).on("vmouseup", ".steer_backward_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_2");
	});
	
	$(document).on("vmousedown", ".steer_backward_3", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_3");
	});
	
	$(document).on("vmouseup", ".steer_backward_3", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_3");
	});
	
	$(document).on("vmousedown", ".steer_backward_left_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_left_1");
	});
	
	$(document).on("vmouseup", ".steer_backward_left_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_left_1");
	});
	
	$(document).on("vmousedown", ".steer_backward_left_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_left_2");
	});
	
	$(document).on("vmouseup", ".steer_backward_left_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_left_2");
	});
	
	$(document).on("vmousedown", ".steer_backward_right_1", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_right_1");
	});
	
	$(document).on("vmouseup", ".steer_backward_right_1", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_right_1");
	});
	
	$(document).on("vmousedown", ".steer_backward_right_2", function(){
		console.log("vmousedown");
		chatsock.send("steer_backward_right_2");
	});
	
	$(document).on("vmouseup", ".steer_backward_right_2", function(){
		console.log("vmouseup");
		chatsock.send("stop_steer_backward_right_2");
	});

});
