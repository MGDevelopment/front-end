/**
* home-messages.js
*/

var dataMessages = {};

dataMessages = {{ messages_data|replace("\n", "") }};

function loadMessages() {
	TMK.addData('messages', dataMessages);
	return;
} 

loadMessages();