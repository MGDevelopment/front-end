{%- import 'macros/comments.html' as render -%}
/**
* Name:
* 	- subject-comments.js
* expected key:
* 	- Comments
*/
var dataComments = {};

{%- if data -%}
dataComments['section'] = '{{ render.renderComments(data["Comments"])|replace("\n", "") }}';
{% endif %}

function loadComments() {
	TMK.addData('comments', dataComments);
	return;
}

loadComments();

