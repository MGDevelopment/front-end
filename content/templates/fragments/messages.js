/**
 * messages.js
 */
var _cookieMessagesName = "TMKMessagesCookie";
var _cookieViewMessagesName = "TMKViewMessagesCookie";
var _expiration = 1000;

function fillMessages(callback) {
	// check if cookie exists
	if (APP.readCookie(_cookieMessagesName) == null) {
		setMessagesReaded(getToken(0));
	}
	getVisualizaMensaje();
	return;
}

function setMessagesReaded(messages) {
	// create cookie
	APP.createCookie(_cookieMessagesName, _serialize(escape(messages)), _expiration);
}
function getMessagesReaded() {
	var messagesReaded = '';
	if (APP.readCookie(_cookieMessagesName) != null) {
		messagesReaded = unescape(_unserialize(APP.readCookie(_cookieMessagesName)));
	}
	return messagesReaded;
}
function getMessages() {
	var messages = APP.getData('messages');
	var messagesReaded = getMessagesReaded();
	if (messages != null) {
        var i;
		for (i = messages.length - 1; i >= 0; i--) {
			var msg = messages[i];
			if (msg == undefined || messagesReaded.indexOf(getToken(msg.getId())) >= 0) {
				messages.splice(i, 1);
			}
		}
	}
	return messages;
}

function removeMessage(msgId) {
	var messagesReaded = getMessagesReaded();
	messagesReaded = messagesReaded + getToken(msgId);
	setMessagesReaded(messagesReaded);
}

function getToken(id) {
	return 'msg.Id=' + id + '@';
}

function getViewMessages() {
	var view = true;
	if (APP.readCookie(_cookieViewMessagesName) != null) {
		view = _unserialize(APP.readCookie(_cookieViewMessagesName));
	}
	return view;
}

function setViewMessages(view) {
	APP.createCookie(_cookieViewMessagesName, _serialize(view), null);
}


/** legacy code **/
var listaMensaje = null;
var indiceMensajeActual = 0;

function getMensaje() {
	var obj = getMessages();
	if (obj != undefined) {
		if (obj.length > 0) {
			listaMensaje = obj;
			getMensajeActual();
		} else {
			$('#msjMin').get(0).style.display = 'none';
			$('#msjMax').get(0).style.display = 'none';
		}
	} else {
	}

}
function getVisualizaMensaje() {

	document.getElementById('msjMax').innerHTML = $('<div>').html([
            '&lt;div class="panelMsjTit"&gt;Ten&amp;eacute;s&amp;nbsp;&lt;',
            'span id="totalMsg"&gt;&lt;/span&gt;&amp;nbsp;mensajes &amp;gt;',
            '&lt;/div&gt;&lt;div class="panelMsjTxt"&gt;&lt;a href="',
            'javascript:mostrarDiv(\'msjMin\'); javascript:',
            'mostrarDiv(\'msjMax\');javascript:setVisualizaMensaje(false)" ',
            'class="panelMsjCerrar"&gt;cerrar&lt;/a&gt;&lt;span id="pagMsg"',
            '&gt;&lt;/span&gt; &lt;span id="textoMsgActual"&gt;&lt;/span&gt; ',
            '&lt;div&gt;&lt;a href="javascript:void(0);" class="pnlMsgComandos',
            '" id="msgAnterior"&gt;&amp;lt;Anterior&lt;/a&gt; | &lt;a href="',
            'javascript:void(0);" class="pnlMsgComandos" id="msgSiguiente"',
            '&gt;Siguiente&amp;gt;&lt;/a&gt; | &lt;a href="javascript:void(0);',
            '" class="pnlMsgComandos" id="msgLeido"&gt;No volver a mostrar ',
            'este mensaje&lt;/a&gt;&lt;/div&gt;&lt;/div&gt;'].join('')).text();

	document.getElementById('msjMin').innerHTML = $('<div>').html([
            '&lt;div class="panelMsjTxt"&gt;&lt;a href="javascript:',
            'mostrarDiv(\'msjMin\'); javascript:mostrarDiv(\'msjMax\');',
            'javascript:setVisualizaMensaje(true)" class="panelMsjAbrir"&gt;',
            'abrir panel y ver mensajes&lt;/a&gt;   &lt;/div&gt;'
            ].join('')).text();

	getMensaje();
}
function setMensajeUsuario(indice) {
	$('#totalMsg').get(0).innerHTML = listaMensaje.length;
	$('#pagMsg').get(0).innerHTML = 'Mensaje ' + (indice + 1) + '/' + listaMensaje.length + ':';
	$('#textoMsgActual').get(0).innerHTML = unescape(listaMensaje[indice].getText());
	if (getViewMessages()) {
		$('#msjMax').get(0).style.display = 'block';
		$('#msjMin').get(0).style.display = 'none';
	} else {
		$('#msjMax').get(0).style.display = 'none';
		$('#msjMin').get(0).style.display = 'block';
	}
	if (indice == 0) {
		$('#msgAnterior').get(0).href = 'javascript:void(0);';
		$('#msgAnterior').get(0).className = 'linkDisabled';
	} else {
		$('#msgAnterior').get(0).href = 'javascript:msgIrAnterior()';
		$('#msgAnterior').get(0).className = 'pnlMsgComandos';
	}
	if (indice == (listaMensaje.length - 1)) {
		$('#msgSiguiente').get(0).href = 'javascript:void(0);';
		$('#msgSiguiente').get(0).className = 'linkDisabled';
	} else {
		$('#msgSiguiente').get(0).href = 'javascript:msgIrSiguiente()';
		$('#msgSiguiente').get(0).className = 'pnlMsgComandos';
	}
	$('#msgLeido').get(0).className = 'pnlMsgComandos';
	$('#msgLeido').get(0).href = 'javascript:setMensajeLeido()';
}
function msgIrAnterior() {
	indiceMensajeActual--;
	setMensajeUsuario(indiceMensajeActual);
	setMensajeActual(indiceMensajeActual);
}
function msgIrSiguiente() {
	indiceMensajeActual++;
	setMensajeUsuario(indiceMensajeActual);
	setMensajeActual(indiceMensajeActual);
}
function setVisualizaMensaje(visualiza) {
	//visualizaMensaje = visualiza;
	setViewMessages(visualiza);
}
function setMensajeLeido() {
	$('#msgAnterior').get(0).href = 'javascript:void(0);';
	$('#msgAnterior').get(0).className = 'linkDisabled';
	$('#msgSiguiente').get(0).href = 'javascript:void(0);';
	$('#msgSiguiente').get(0).className = 'linkDisabled';
	$('#msgLeido').get(0).className = 'linkDisabled';
	$('#msgLeido').get(0).href = 'javascript:void(0);';
	var id = listaMensaje[indiceMensajeActual].getId();
	removeMessage(id);
	if (indiceMensajeActual == (listaMensaje.length - 1)) {
		indiceMensajeActual--;
		setMensajeActual(indiceMensajeActual);
	}
	getMensaje();
}
function setMensajeActual(indice) {
	if (indice != -1) {
		var id = listaMensaje[indice].getId();
	}
}
function getMensajeActual() {
	setMensajeUsuario(indiceMensajeActual);
}
