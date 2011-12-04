{%- import 'macros/productComments.html' as render -%}
/**
* Name:
* 	- product-comments.js
* expected keys:
*	- ArticleId
*	- SubjectId
* 	- Comments
* 		- Date ?
*/
var dataComments = {};

{%- if d -%}
dataComments['detail'] = '{{ render.renderComments(d.EntityId, url, d.Categoria_Seccion, d["Comments"])|replace("\n", "") }}';
{% endif %}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

loadComments();
