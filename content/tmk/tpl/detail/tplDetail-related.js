{%- import './macros/detailRelated.html' as render -%}
/**
* detail-related.js
*/
var dataRelatedDetail = {};

{%- if related_data -%}
	dataRelatedDetail = '{{ render.renderRelated(related_data)|replace("\n", "") }}';
{% endif %}

function loadRelatedDetail() {
	TMK.addData('relatedDetail', dataRelatedDetail);
	return;
} 

loadRelatedDetail();