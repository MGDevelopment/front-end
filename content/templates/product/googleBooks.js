/**
 * Name:
 *  - googleBooks.js
 *
 * fragment related:
 *  - googleBooks.html
 *
 * dependency:
 * 	- info: http://code.google.com/intl/es-ES/apis/books/docs/viewer/developers_guide.html
 * 	- <script type="text/javascript" src="http://www.google.com/jsapi"></script>
 * ISBN Format:
 *  - (JAVA) String[]isbn_ = articulo.getISBN().split("-"); StringBuffer cadena = new StringBuffer("");for(int i=0;i<isbn_.length;i++){ cadena.append(""+isbn_[i]); }
 *
 */

google.load("books", "0", {
	"language" : "es"
});

function alertNotFound() {
	if (document.getElementById('viewerCanvas') != 'undefined') {
		document.getElementById('viewerCanvas').innerHTML = '';
		document.getElementById('googleBook').innerHTML = '';
	}
}
function alertInitialized() {
	if (document.getElementById('viewerCanvas') != 'undefined') {
		var view = document.getElementById('viewerCanvas');
		var viewChildNodes = view.childNodes;
		var nodes = viewChildNodes[0].childNodes;
		nodes[1].innerHTML = '<div>';
		nodes[1].innerHTML = '<a href=\'http://books.google.com/?hl=es\' target=\'_blank\'> <img style=\'border:none;\'src=\"http://books.google.com/googlebooks/images/poweredby.png\"> </a>'
				+ '</div>';
	}
}
function initialize() {
	var divVisor = document.getElementById('viewerCanvas');
	var viewer = new google.books.DefaultViewer(divVisor, {
		'showLinkChrome' : false
	});
	viewer.load('ISBN:{{ ISBN }}', alertNotFound,
			alertInitialized);
}

if (document.getElementById('viewerCanvas') != null) {
	google.setOnLoadCallback(initialize);
}