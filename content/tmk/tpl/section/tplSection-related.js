{%- import './macros/related.html' as render -%}
/**
* section-related.js
* OPT1 = MAS_VENDIDOS
* OPT2 = PRECIO_VENTA_1 + economicos primero
* OPT3 = FECHA_APARICION_1 + antiguos primero
* OPT4 = FECHA_APARICION_2 + recientes primero
* OPT5 = PRECIO_VENTA_2 + costosos primero
* OPT6 = ALFABETICAMENTE_AZ
* OPT7 = ALFABETICAMENTE_ZA
*/
var dataRelated = {};

{%- for item in related_data -%}
	dataRelated['{{ item }}'] = '{{ render.renderRelated(related_data[item].maxItemPage, related_data[item].order, related_data[item].articulos)|replace("\n", "") }}';
{%- endfor %}

function loadRelated() {
	TMK.addData('related', dataRelated);
	return;
} 

var callBackRelated = function (order) {
{%- for item in related_data -%}
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
loadRelated();

