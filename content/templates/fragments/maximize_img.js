/**
 * maximize_img.js
 */

function popitup(imgLocation) {

	img = new Image();

	img.src = imgLocation;

	img.onload = doImgpop;

}

function doImgpop(e) {
	try {
		var img = this; // I THINK that's the right way to get the image object. If
						// not, may involve using e.

		var width = img.width + 20;

		var height = img.height + 20;

		var settings = "width="
				+ width
				+ ",height="
				+ height
				+ "resizable=1";

		var popup = window.open(img.src, '', settings);
	} catch(exception) {
		// TODO
	}
}
