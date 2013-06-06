{%- import 'macros/slider.html' as render -%}
/**
* section-showcase.js
*/
var dataShowCase = {};

{% for key in ('Classics', 'Showcase') %}

    dataShowCase['{{ key }}'] = '{{ render.renderSlider(d[key], key|lower, 6, url)|replace("\n", "") }}';

{%- endfor -%}

APP.addData('showcase', dataShowCase);

// XXX ????
function callBackDropDownShowCase(section) {

    return;
}

APP.addData('showcaseFilter', 'Showcase');
