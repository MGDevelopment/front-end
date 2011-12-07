/**
 * tree.js
 */
{%- if d.Categoria_Seccion > 0 and d.Categoria_Grupo < 0 and d.Categoria_Familia < 0 and d.Categoria_Subfamilia < 0 -%}
	APP.eraseCookie('TMKtreeview-black');
{%- endif -%}

function fillTree(divName, callback) {
    var treeHTML = '';

    try {
        if (APP.getData('tree')) {
            treeHTML = APP.getData('tree')['tree'];
        }
    } catch (e) {
        treeHTML = '<!-- Sin arbol -->';
    }

    if (document.getElementById(divName)) {
    	document.getElementById(divName).innerHTML = treeHTML;
    }

	$("#tree").treeview({
		'cookieId': "TMKtreeview-black",
		collapsed: true,
		unique: true,
		//persist: "cookie"
	});

	{%- if d.Categoria_Grupo > 0 -%}
		$("li[id='arbol-{{ d.Categoria_Seccion }}-{{ d.Categoria_Grupo }}']").children('.hitarea').trigger('click');
		{%- if d.Categoria_Familia > 0 -%}
			$("li[id='arbol-{{ d.Categoria_Seccion }}-{{ d.Categoria_Grupo }}-{{ d.Categoria_Familia }}']").children('.hitarea').trigger('click');
		{%- endif -%}
	{%- endif -%}

    try {
        if (callback && typeof (callback) === "function") {
            // execute the callback, passing parameters as necessary
            callback();
        }
    } catch (e) {
        // TODO: handle exception
    }
    return;
}