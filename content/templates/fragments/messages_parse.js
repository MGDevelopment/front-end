var dataMessages = {};
function parseMSJ(){
	var messageList = new Array(100);
	    	$.ajax({
	    		type: "GET",
	    		url: "/leyendas/mensajes/msj.xml",
	    		dataType: "xml",
	    		success: function(xml) {
	    			count = 0;
	    			$(xml).find('mensaje').each(function(){
	    				var id = $(this).find('id').text();
	    				var texto = escape($(this).find('texto').text());
	    				messageList[count++] = new Msg(id, texto);
	    			});
	    			dataMessages = messageList;
	    			loadMessages();
	    			fillMessages();
	    		}
	    	});
	return;
}


function loadMessages() {
	APP.addData('messages', dataMessages);
	return;
}
parseMSJ();

function Msg(id, text) {
    this._text = text;
    this._id = id;

	this.getText = function() {
			return this._text;
		};
	this.getId = function() {
			return this._id;
		};

}
