{%- import './macros/comments.html' as render -%}

/**
* home-comments.js
*/
var dataComments = {};

{%- for key in comments_data -%}
	dataComments['{{ key }}'] = '{{ render.renderComments(comments_data[key], site_domain)|replace("\n", "") }}';
{%- endfor -%}

function loadComments() {
	TMK.addData('comments', dataComments);
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

