{%- import 'macros/productPrice.html' as render -%}
/**
 * Name:
*  - product-price.js
*  expected keys
*
*/
var dataPrice = {};

{%- if d -%}
	dataPrice = '{{ render.renderPrice(d)|replace("\n", "") }}';
{% endif %}

function loadPrice() {
	APP.addData('price', dataPrice);
	return;
}

loadPrice();