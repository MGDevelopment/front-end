/**
 * lastVisited.js
 *
 */

var _cookieLastVisitedName = "TMKLastVisitedCookie";
var _numberOfItems = 3;

function addLastVisited(article) {
	var articleList = null;

	if (article == null) {
		return;
	}

	// check if cookie exists
	if (APP.readCookie(_cookieLastVisitedName) != null) {
		articleList = JFather.unserialize(APP.readCookie(_cookieLastVisitedName));
		for (var i = 0; i < _numberOfItems; i++) {
			tmpArticle = articleList[i];
			if (tmpArticle != null && tmpArticle.getArticleId() == article.getArticleId()) {
				return;
			}
		}
	} else {
		articleList = new Array(3);
	}

	for (var i = _numberOfItems; i > 1; i--) {
		articleList[i-1] = articleList[i-2];
	}
	articleList[0] = article;

	// create cookie
	APP.createCookie(_cookieLastVisitedName, JFather.serialize(articleList), null);
	return;
}

function renderLastVisited(divTarget) {
	var articleList = null;
	if (APP.readCookie(_cookieLastVisitedName) != null) {
		articleList = JFather.unserialize(APP.readCookie(_cookieLastVisitedName));
	}
	var lastVisitedHTML = getNoItems();
	if (articleList != null) {
		lastVisitedHTML = getItems(articleList);
	}
	if (document.getElementById(divTarget)) {
		document.getElementById(divTarget).innerHTML = lastVisitedHTML;
	}
	return;
}

function getNoItems() {
	return '<table align="center" width="389" border="0" cellpadding="0" cellspacing="0" class="modulosmedio">' +
	  '<tr>' +
	  	'<td class="titulosceldas"><table width="387" border="0" cellpadding="0" cellspacing="0" class="titulosceldas2">' +
	  		'<tr>' +
	      '<td><img src="{{ url.images }}/imagenes/libros/t-ultimosvisitados.gif" alt="&Uacute;ltimos visitados" width="127" height="10" /></td>' +
	      	'</tr>' +
	      	'</table></td>' +
	   '</tr>' +
	'<tr>' +
	'<td><div class="GultvisitadosB" align="center">' +
	    '<div><img src="{{ url.images }}/imagenes/ultvisitados.gif" height="30" style="margin-top:10px;" alt="" /></div>' +
	  '<div class="Ftexto03" style="margin-top:10px">EN ESTE SECTOR SE CARGARAN AUTOM&Aacute;TICAMENTE TODOS LOS PRODUCTOS QUE VISITES EN NUESTRO SITIO. </div>' +
	'</div></td>' +
	'</tr>' +
	'</table>';
}

function getItems(articleList) {
	var HTML = '';
	HTML = '<table align="center" width="390" border="0" cellpadding="0" cellspacing="0" class="modulosmedio">' +
		'<tr>' +
			'<td class="titulosceldas">' +
				'<table width="390" border="0" cellpadding="0" cellspacing="0" class="titulosceldas2">' +
					'<tr>' +
						'<td>' +
							'<img src="{{ url.images }}/imagenes/libros/t-ultimosvisitados.gif" alt="&Uacute;ltimos visitados" width="127" height="10" />' +
						'</td>' +
					'</tr>' +
				'</table>' +
			'</td>' +
		'</tr>';
	for (var i = 0; i < _numberOfItems; i++) {
		var article = articleList[i];
		if (article != null) {
			HTML = HTML + '<tr>' +
				'<td>' +
					'<table align="center" width="386" border="0" cellpadding="0" cellspacing="0" class="Gultimosvitadosprod">' +
						'<tr>' +
							'<td colspan="3">' +
								'<div align="left">' +
									'<a class="FProductos" href="' + article.getURL()  + '">' + article.getTitle() + '</a>' +
		        	 				'<span class="FProductos"> | <a href="' + article.getURLPrincipalAttribute() + '" class="Fautores0">' + article.getPrincipalAttribute() + '</a>' +
		        	 				'</span>' +
							        '<br>' +
							        '<a href="' + article.getURLGroup() + '" class="FCategorias">' + article.getGroup() + '</a>' +
								'</div>' +
							'</td>' +
						'</tr>' +
		   				'<tr>' +
		     				'<td width="299" valign="bottom" class="Gultimosvitadosprodprecio">' +
		     					'<div align="left">' +
 		     						'<span class="Fprecio">PRECIO: ' + article.getPrice() + '</span>' +
		     					'</div>' +
		     				'</td>' +
		     				'<td valign="bottom">' +
		     					'<div align="right">' +
		           					'<table width="2" border="0" cellspacing="0" cellpadding="0" class="divComprar">' +
		             					'<tr>' +
		               						'<td height="19" class="divInfo">' +
			               						'<a class="FProductos" href="' + article.getURL() + '" alt="' + article.getTitle() +'">' +
				               						'<img src="{{ url.images }}/imagenes/inicio/b-info.gif" alt="" title="" border="0" />' +
			               						'</a>' +
		               						'</td>' +
		               						'<td class="divComprarPedir">';

		    if (article.getAvailable()) {
		    	HTML = HTML + '<a href="javascript:carrito_AgregarArticulo(\"' + article.getArticleId() + '\");window.scrollTo(0,0);" rel="nofollow">' +
		               			'<img src="{{ url.images }}/imagenes/inicio/b-comprar.gif" alt="Comprar"  border="0" /></a>';
		    } else {
		    	HTML = HTML + '<a href="javascript:if (confirm(\"Este producto no esta disponible actualmente. Desea hacer un pedido?\"))document.location = "/PedidoEspecial?ID_ARTICULO=' + article.getArticleId() + ';" rel="nofollow">' +
		    					'<img src="{{ url.images }}/imagenes/inicio/b-pedir.gif" alt="Comprar"  border="0"/>' +
		    				'</a>';
		    }
		    HTML = HTML + '</td>' +
		             					'</tr>' +
		           					'</table>' +
		         				'</div>' +
		     				'</td>' +
		   				'</tr>' +
		 			'</table>' +
		 		'</td>' +
			'</tr>';
		}
	}
	HTML = HTML + '</table>';
	return HTML;
}

function Article(url, title, urlPrincipalAttribute, principalAttribute, urlGroup, group, price, available, id) {
    this._url = url;
    this._title = title;
    this._urlPrincipalAttribute = urlPrincipalAttribute;
    this._principalAttribute = principalAttribute;
    this._urlGroup = urlGroup;
    this._group = group;
    this._price = price;
    this._available = available;
    this._id = id;


    this.getURL = function() {
			return this._url;
		};
	this.getTitle = function() {
			return this._title;
		};
	this.getURLPrincipalAttribute = function() {
			return this._urlPrincipalAttribute;
		};
	this.getPrincipalAttribute = function() {
			return this._principalAttribute;
		};
	this.getURLGroup = function() {
			return this._urlGroup;
		};
	this.getGroup = function() {
			return this._group;
		};
	this.getPrice = function() {
			return this._price;
		};
	this.getAvailable = function() {
			return this._available;
		};
	this.getArticleId = function() {
			return this._id;
		};

}
