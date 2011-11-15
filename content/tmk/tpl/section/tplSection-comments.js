{%- import './macros/comments.html' as render -%}
/**
* section-comments.js
*/
var dataComments = {};

{%- if comments_data -%}
dataComments['section'] = '{{ render.renderComments(comments_data, site_domain)|replace("\n", "") }}';
{% endif %}

function loadComments() {
	TMK.addData('comments', dataComments);
	return;
} 

loadComments();

