/**
 * exchange.js
 */

function doExchange(from, to, amount) {
	var calculated = '';
	try {
		var exchange = APP.getData('exchange');
		if (exchange) {
			var sellRate = exchange[from + '-' + to];
			calculated = amount * sellRate;
		}
	} catch (e) {
		// TODO: handle exception
	}
	return calculated;
}