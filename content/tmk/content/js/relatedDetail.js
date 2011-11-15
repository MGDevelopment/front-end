/**
 * relatedDetail.js
 */
function fillRelatedDetail(callback) {
	var relatedDetailHTML = '';
	
	try {
		if (TMK.getData('relatedDetail')) {
			relatedDetailHTML = TMK.getData('relatedDetail');
		}
	} catch (e) {
		relatedDetailHTML = 'Sin datos';
	}
	document.getElementById('related_detail').innerHTML = relatedDetailHTML;
	
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