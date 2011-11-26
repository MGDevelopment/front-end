{%- import 'macros/comments.html' as render -%}
/**
* Name:
* 	- subject-comments.js
* expected key:
* 	- Comments
*/
var dataComments = {};

{%- if data -%}
dataComments['section'] = '{{ render.renderComments(data["Comments"], true)|replace("\n", "") }}';
{%- endif %}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

loadComments();

