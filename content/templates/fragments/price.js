/**
 * price.js
 */
function fillPrice(callback) {
	var priceHTML = '';

	try {
		if (APP.getData('price')) {
			priceHTML = APP.getData('price');
		}
	} catch (e) {
		priceHTML = '<!-- Sin datos -->';
	}
	if (document.getElementById('price_detail')) {
		document.getElementById('price_detail').innerHTML = priceHTML;
	}

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