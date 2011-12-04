{%- import 'macros/comments.html' as render -%}
/**
* Name:
* 	- home-price.js
* expected keys:
* 	-
*
*/
var dataExchange = {};

{%- for key in d -%}
	dataExchange['{{ key }}'] = {{ d[key].SellRate }};
{%- endfor -%}

function loadExchange() {
	APP.addData('exchange', dataExchange);
	return;
}

var callBackExchange = function () {
	return;
}

loadExchange();

