{%- import 'macros/productRelated.html' as render -%}
/**
 * Name:
* 	- product-related.js
* expected keys:
* 	- d
*/
var dataRelatedProduct = {};

{%- if d -%}
	dataRelatedProduct = '{{ render.renderRelated(d.Related)|replace("\n", "") }}';
{% endif %}

function loadRelatedProduct() {
	APP.addData('relatedProduct', dataRelatedProduct);
	return;
}

loadRelatedProduct();