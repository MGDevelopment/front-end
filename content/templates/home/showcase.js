{%- import 'macros/slider.html' as render -%}
/**
 * Name:
*  - home-showcase.js
*/
var dataShowCase = {};

{%- for key in d -%}
	{%- set dataKey = key|replace("Recommended-","")|replace("Showcase-","")|lower -%}
	dataShowCase['{{ key }}'] = '{{ render.renderSlider(d[key], dataKey, 2, url)|replace("\n", "")|e }}';
{%- endfor -%}

function loadShowCase() {
	APP.addData('showcase', dataShowCase);
	return;
}

var callBackDropDownShowCase = function (section) {

	return;
}
loadShowCase();
