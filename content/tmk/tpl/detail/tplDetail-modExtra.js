{%- import './macros/detailModExtra.html' as render -%}
/**
* detail-modExtra.js
*/
var dataModExtra = {};

{%- if modExtra_data -%}
	dataModExtra = '{{ render.renderModExtra(idArticle, Section, modExtra_data)|replace("\n", "") }}';
{% endif %}

function loadModExtra() {
	TMK.addData('modExtra', dataModExtra);
	return;
} 

loadModExtra();