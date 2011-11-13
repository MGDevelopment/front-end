/* messages.js */

function fillMessages(callback) {
    getVisualizaMensaje();
    return;
}

var listaMensaje = null;
var visualizaMensaje = false;
var indiceMensajeActual = 0;


function getMensaje() {
    var obj = APP.getData('messages');
    if (obj != undefined) {
        if (obj.mensajes.lista.length > 0) {
            listaMensaje = obj.mensajes.lista;
            getMensajeActual()
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
    if (visualizaMensaje) {
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
    visualizaMensaje = visualiza;
}
function setMensajeLeido() {
    $('#msgAnterior').get(0).href = 'javascript:nada()';
    $('#msgAnterior').get(0).className = 'linkDisabled';
    $('#msgSiguiente').get(0).href = 'javascript:nada()';
    $('#msgSiguiente').get(0).className = 'linkDisabled';
    $('#msgLeido').get(0).className = 'linkDisabled';
    $('#msgLeido').get(0).href = 'javascript:nada()';
    var id = listaMensaje[indiceMensajeActual].id;
    if (indiceMensajeActual == (listaMensaje.length - 1)) {
        indiceMensajeActual--;
        setMensajeActual(indiceMensajeActual)
    }
}
function setMensajeActual(indice) {
    if (indice != -1) {
        var id = listaMensaje[indice].id;
    }
}
function getMensajeActual() {
    setMensajeUsuario(indiceMensajeActual);
}
