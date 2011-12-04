{%- import 'macros/comments.html' as render -%}
{%- set section_name = d['Title']|lower -%}
/**
* Name:
* 	- subject-comments.js
* expected key:
* 	- Comments
*/
var dataComments = {};

{%- if d -%}
dataComments['{{ section_name }}'] = '{{ render.renderComments(d["Comments"], url, true)|replace("\n", "") }}';
{%- endif %}

function loadComments() {
	APP.addData('comments', dataComments);
	return;
}

loadComments();

