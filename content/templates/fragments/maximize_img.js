/**
 * maximize_img.js
 */

var newwindow = ''
function popitup(url) {
	try {
		if (newwindow.location && !newwindow.closed) {
		    newwindow.location.href = url;
		    newwindow.focus(); }
		else {
			var newImg = new Image();
			newImg.src = url;
			var height = newImg.height;
			var width = newImg.width;
		    newwindow=window.open(url,'htmlname','width=' + width +',height=' + height +',resizable=1');
		}
	} catch (e) {
		// TODO
	}
}

function tidy() {
	if (newwindow.location && !newwindow.closed) {
	   newwindow.close();
	}
}
