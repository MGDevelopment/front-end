{%- import 'macros/productRelated.html' as render -%}
/**
 * Name:
* 	- product-related.js
* expected keys:
* 	- d
*/
var dataRelatedProduct = {};

{%- if data -%}
	dataRelatedProduct = '{{ render.renderRelated(data)|replace("\n", "") }}';
{% endif %}

function loadRelatedProduct() {
	APP.addData('relatedProduct', dataRelatedProduct);
	return;
}

loadRelatedProduct();