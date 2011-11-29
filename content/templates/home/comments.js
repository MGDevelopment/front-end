{%- import 'macros/comments.html' as render -%}
/**
* Name:
* 	- home-comments.js
* expected keys:
* 	- all
* 	- books
* 	- music
* 	- movies
*
*/
var dataComments = {};

{%- for key in d -%}
	dataComments['{{ key|lower }}'] = '{{ render.renderComments(d[key])|replace("\n", "") }}';
{%- endfor -%}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

var callBackDropDownComments = function (section) {
	if(section == 'books'){
		$('#optComentarios').html('Solo libros');
	}else if(section == 'music') {
		$('#optComentarios').html('Solo m&uacute;sica');
	}else if(section == 'movies') {
		$('#optComentarios').html('Solo peliculas');
	}else{
		$('#optComentarios').html('&Uacute;ltimos  comentados');
	}
	return;
}

loadComments();

