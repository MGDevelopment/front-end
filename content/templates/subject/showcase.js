{%- import 'macros/slider.html' as render -%}
/**
* section-showcase.js
*/
var dataShowCase = {};

{%- for key in d['ShowCase'] -%}
	{%- for subKey in d[key] -%}
        {%- set dataKey = key|replace("Recommended-","")|replace("Showcase-","")|lower -%}
		{# dataShowCase['{{ subKey }}{{ key }}'] = '{{ render.renderSlider(showcase_data[key][subKey], key)|replace("\n", "") }}'; #}
        dataShowCase['{{ key }}'] = '{{ render.renderSlider(d[key], dataKey, 6, url)}}';
	{%- endfor %}
{%- endfor -%}

function loadShowCase() {
	APP.addData('showcase', dataShowCase);
	return;
}

var callBackDropDownShowCase = function (section) {

	return;
}

loadShowCase();
