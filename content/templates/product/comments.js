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

{%- if data -%}
dataComments['detail'] = '{{ render.renderComments(data["ArticleId"], data["SubjectId"], data["Comments"])|replace("\n", "") }}';
{% endif %}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

loadComments();