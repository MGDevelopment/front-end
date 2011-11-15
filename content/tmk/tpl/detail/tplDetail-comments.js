{%- import './macros/detailComments.html' as render -%}
/**
* detail-comments.js
*/
var dataComments = {};

{%- if comments_data -%}
	dataComments['detail'] = '{{ render.renderComments(idArticle, idSection, comments_data)|replace("\n", "") }}';
{% endif %}

function loadComments() {
	TMK.addData('comments', dataComments);
	return;
} 

loadComments();