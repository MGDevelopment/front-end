{%- import 'macros/tree.html' as render -%}
/**
 * Name:
 * 	- tree.js
 *
 */

var dataTree = {};

{%- if d['Tree'] -%}
dataTree['tree'] = '{{ render.renderTree(d['Tree'])|replace("\n", "") }}';
{%- endif %}

function loadTree() {
	APP.addData('tree', dataTree);
	return;
}

var callBackTree = function () {
	return;
}
loadTree();
