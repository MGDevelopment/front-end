/**
 * messages.js
 */
var _cookieMessagesName = "TMKMessagesCookie";
var _cookieViewMessagesName = "TMKViewMessagesCookie";
var _expiration = 1000;

function fillMessages(callback) {
	// check if cookie exists
	if ($.cookie(_cookieMessagesName) == null) {
		setMessagesReaded('');
	}
	getVisualizaMensaje();
	return;
}

function setMessagesReaded(messages) {
	// create cookie
	$.cookie(_cookieMessagesName, JFather.serialize(messages), { expires: _expiration, path: '/'});
}
function getMessagesReaded() {
	var messagesReaded = '';
	if ($.cookie(_cookieMessagesName) != null) {
		messagesReaded = JFather.unserialize($.cookie(_cookieMessagesName));
	}
	return messagesReaded;
}
function getMessages() {
	var messages = TMK.getData('messages');
	var messagesReaded = getMessagesReaded();
	if (messages != null) {
		for (var i = messages.mensajes.lista.length-1; i >= 0; i--) {
			var msg = messages.mensajes.lista[i];
			if (messagesReaded.indexOf(getToken(msg.id)) >= 0) {
				messages.mensajes.lista.splice(i, 1);
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
	return "msg.Id=" + id + ";";
}

function getViewMessages() {
	var view = true;
	if ($.cookie(_cookieViewMessagesName) != null) {
		view = JFather.unserialize($.cookie(_cookieViewMessagesName));
	}
	return view;
}

function setViewMessages(view) {
	$.cookie(_cookieViewMessagesName, JFather.serialize(view), { expires: null, path: '/'});
}


/** legacy code **/
var listaMensaje = null;
var indiceMensajeActual = 0;

function getMensaje() {
	var obj = getMessages();
	if (obj != undefined) {
		if (obj.mensajes.lista.length > 0) {
			listaMensaje = obj.mensajes.lista;
			getMensajeActual();
		} else {
			$('#msjMin').get(0).style.display = 'none';
			$('#msjMax').get(0).style.display = 'none'
		}
	} else {
	}

}
function getVisualizaMensaje() {
	// fix mgoldsman 20110831
	document.getElementById('msjMax').innerHTML = '<div class="panelMsjTit">Tenes&nbsp;<span id="totalMsg"></span> mensajes por leer &gt;</div>'
			+ '<div class="panelMsjTxt">'
			+ '<a href="javascript:mostrarDiv(\'msjMin\'); javascript:mostrarDiv(\'msjMax\');javascript:setVisualizaMensaje(false)" class="panelMsjCerrar">cerrar</a>'
			+ '<span id="pagMsg"></span> <span id="textoMsgActual"></span> <div><a href="javascript:nada()" class="pnlMsgComandos" id="msgAnterior">&lt;Anterior</a> | <a href="javascript:nada()" class="pnlMsgComandos" id="msgSiguiente">Siguiente&gt;</a> | <a href="javascript:nada()" class="pnlMsgComandos" id="msgLeido">No volver a mostrar este mensaje</a></div>'
			+ '</div>';
	document.getElementById('msjMin').innerHTML = '<div class="panelMsjTxt"><a href="javascript:mostrarDiv(\'msjMin\'); javascript:mostrarDiv(\'msjMax\');javascript:setVisualizaMensaje(true)" class="panelMsjAbrir">abrir panel y ver mensajes</a>   </div>';
	getMensaje();
}
function setMensajeUsuario(indice) {
	$('#totalMsg').get(0).innerHTML = listaMensaje.length;
	$('#pagMsg').get(0).innerHTML = 'Mensaje ' + (indice + 1) + '/'
			+ listaMensaje.length + ':';
	$('#textoMsgActual').get(0).innerHTML = listaMensaje[indice].texto;
	if (getViewMessages()) {
		$('#msjMax').get(0).style.display = 'block';
		$('#msjMin').get(0).style.display = 'none'
	} else {
		$('#msjMax').get(0).style.display = 'none';
		$('#msjMin').get(0).style.display = 'block'
	}
	if (indice == 0) {
		$('#msgAnterior').get(0).href = 'javascript:nada()';
		$('#msgAnterior').get(0).className = 'linkDisabled'
	} else {
		$('#msgAnterior').get(0).href = 'javascript:msgIrAnterior()';
		$('#msgAnterior').get(0).className = 'pnlMsgComandos'
	}
	if (indice == (listaMensaje.length - 1)) {
		$('#msgSiguiente').get(0).href = 'javascript:nada()';
		$('#msgSiguiente').get(0).className = 'linkDisabled'
	} else {
		$('#msgSiguiente').get(0).href = 'javascript:msgIrSiguiente()';
		$('#msgSiguiente').get(0).className = 'pnlMsgComandos'
	}
	$('#msgLeido').get(0).className = 'pnlMsgComandos';
	$('#msgLeido').get(0).href = 'javascript:setMensajeLeido()'
}
function msgIrAnterior() {
	indiceMensajeActual--;
	setMensajeUsuario(indiceMensajeActual);
	setMensajeActual(indiceMensajeActual)
}
function msgIrSiguiente() {
	indiceMensajeActual++;
	setMensajeUsuario(indiceMensajeActual);
	setMensajeActual(indiceMensajeActual)
}
function setVisualizaMensaje(visualiza) {
	//visualizaMensaje = visualiza;
	setViewMessages(visualiza);
}
function setMensajeLeido() {
	$('#msgAnterior').get(0).href = 'javascript:nada()';
	$('#msgAnterior').get(0).className = 'linkDisabled';
	$('#msgSiguiente').get(0).href = 'javascript:nada()';
	$('#msgSiguiente').get(0).className = 'linkDisabled';
	$('#msgLeido').get(0).className = 'linkDisabled';
	$('#msgLeido').get(0).href = 'javascript:nada()';
	var id = listaMensaje[indiceMensajeActual].id;
	removeMessage(id);
	if (indiceMensajeActual == (listaMensaje.length - 1)) {
		indiceMensajeActual--;
		setMensajeActual(indiceMensajeActual)
	}
	getMensaje();
}
function setMensajeActual(indice) {
	if (indice != -1) {
		var id = listaMensaje[indice].id;
	}
}
function getMensajeActual() {
	setMensajeUsuario(indiceMensajeActual);
}