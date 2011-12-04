{%- import 'macros/slider.html' as render -%}
/**
 * Name:
*  - home-showcase.js
*/
var dataShowCase = {};

{%- for key in d -%}
	{%- set dataKey = key|replace("Recommended-","")|replace("Showcase-","")|lower -%}
	dataShowCase['{{ key }}'] = '{{ render.renderSlider(d[key], dataKey, 2, url)|replace("\n", "") }}';
{%- endfor -%}

function loadShowCase() {
	APP.addData('showcase', dataShowCase);
	return;
}

var callBackDropDownShowCase = function (section) {

	return;
}
loadShowCase();

/* XXX is this OK? def home page specific so moved it here */
APP.addData('showcaseFilter', 'Recommended');
