/**
* home-messages.js
*/

var dataMessages = {};

dataMessages = {'mensajes': {'lista': [{'id': '297', 'texto': '<a href="http://oblogo.com" target="_blank"><IMG SRC="/imagenes/grupos/cartelera/oblogo.jpg" border="0" ALT="Oblogo"></a><br/></div>Con tu compra en Tematika.com recibir&aacute;s de regalo un ejemplar de la revista Oblogo, la revista que publica lo mejor de la blog&oacute;sfera.'}, {'id': '41', 'texto': '<div style="font-weight:bold;"&gt;Promoci&amp;oacute;n en Tematika.com:<br/&gt; </div&gt;Env&amp;iacute;o Gratis en Argentina con tus compras mayores a $150.- No acumulable con otras promociones.'}, {'id': '46', 'texto': '<div style="font-weight:bold;"&gt;<a href="/articulo/detalleArticulo.jsp?idArticulo=493735&amp;ID_ALIANZA=1139&amp;ID_SECCION=1089"&gt;Videomatch &amp; Showmatch</a&gt;<br/&gt;</div&gt;Una resenia fotogr&amp;aacute;fica y biogr&amp;aacute;fica de las dos d&amp;eacute;cadas de vida de este &amp;eacute;xito que arranc&amp;oacute; el 1 de marzo de1990. (env&amp;iacute;o gratis en Argentina hasta el 30 de Junio)'}]}};

function loadMessages() {
	TMK.addData('messages', dataMessages);
	return;
} 

loadMessages();