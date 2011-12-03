{%- import 'macros/comments.html' as render -%}
/**
* Name:
* 	- subject-comments.js
* expected key:
* 	- Comments
*/
var dataComments = {};

{%- if d -%}
dataComments['section'] = '{{ render.renderComments(d["Comments"], true)|replace("\n", "") }}';
{%- endif %}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

loadComments();

