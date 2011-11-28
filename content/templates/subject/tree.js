{%- import 'macros/tree.html' as render -%}
/**
 * Name:
 * 	- tree.js
 *
 */

var dataTree = {};

{%- if data -%}
dataTree['tree'] = '{{ render.renderTree(data)|replace("\n", "") }}';
{%- endif %}

function loadTree() {
	APP.addData('tree', dataTree);
	return;
}

var callBackTree = function () {
	return;
}
loadTree();