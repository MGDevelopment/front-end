{%- import 'macros/catalog.html' as render -%}
/**
* 	- catalog/section.js
* expected keys:
* 	- OPT1 = MAS_VENDIDOS
* 	- OPT2 = PRECIO_VENTA_1 + economicos primero
* 	- OPT3 = FECHA_APARICION_1 + antiguos primero
* 	- OPT4 = FECHA_APARICION_2 + recientes primero
* 	- OPT5 = PRECIO_VENTA_2 + costosos primero
* 	- OPT6 = ALFABETICAMENTE_AZ
* 	- OPT7 = ALFABETICAMENTE_ZA
*
* TODO:
* 	- maxItemPage
* 	- order
* 	- articles
*/
var dataCatalog = {};

{%- for item in data -%}
	dataCatalog['{{ item }}'] = '{{ render.renderCatalog(data[item].maxItemPage, data[item].order, data[item].articles)|replace("\n", "") }}';
{%- endfor %}

function loadCatalog() {
	APP.addData('catalog', dataCatalog);
	return;
}

var callBackCatalog = function (order) {
{%- for item in data -%}
	if (order == '{{ item }}') {
		document.getElementById('{{ item }}OFF').style.display = 'block';
		document.getElementById('{{ item }}ON').style.display = 'none';
	} else {
		document.getElementById('{{ item }}OFF').style.display = 'none';
		document.getElementById('{{ item }}ON').style.display = 'block';
	}
{%- endfor %}
	return;
}
loadCatalog();

