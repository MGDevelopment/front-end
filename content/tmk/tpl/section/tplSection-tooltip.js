{%- import './macros/tooltip.html' as render -%}
/**
* section-tooltip.js
*/
var dataToolTip = {};

{%- for key in tooltip_data -%}
	{%- for subKey in tooltip_data[key] -%}
		dataToolTip['{{ subKey }}{{ key }}'] = '{{ render.renderToolTip(tooltip_data[key][subKey], key)|replace("\n", "") }}';
	{%- endfor %}
{%- endfor -%}

function loadToolTip() {
	TMK.addData('tooltip', dataToolTip);
	return;
} 

var callBackDropDownToolTip = function (section) {
	
	return;
}
loadToolTip();

