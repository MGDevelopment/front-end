/**
 * tree.js
 */

function fillTree(divName, callback) {
    var treeHTML = '';

    try {
        if (APP.getData('tree')) {
            treeHTML = APP.getData('tree');
        }
    } catch (e) {
        treeHTML = 'Sin arbol';
    }

    if (document.getElementById(divName)) {
    	document.getElementById(divName).innerHTML = treeHTML;
    }

	$("#tree").treeview({
		persist: "cookie",
		cookieId: "TMKtreeview-black"
	});

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