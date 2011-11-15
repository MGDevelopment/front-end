/**
 * modExtra.js
 */
function fillModExtra(callback) {
	var modExtraHTML = '';
	
	try {
		if (TMK.getData('modExtra')) {
			modExtraHTML = TMK.getData('modExtra');
		}
	} catch (e) {
		modExtraHTML = 'Sin datos';
	}
	document.getElementById('modExtra_detail').innerHTML = modExtraHTML;
	
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