{%- import './macros/slider.html' as render -%}
/**
* section-showcase.js
*/
var dataShowCase = {};

{%- for key in showcase_data -%}
	{%- for subKey in showcase_data[key] -%}
		dataShowCase['{{ subKey }}{{ key }}'] = '{{ render.renderSlider(showcase_data[key][subKey], key)|replace("\n", "") }}';
	{%- endfor %}
{%- endfor -%}

function loadShowCase() {
	TMK.addData('showcase', dataShowCase);
	return;
} 

var callBackDropDownShowCase = function (section) {
	
	return;
}
loadShowCase();

