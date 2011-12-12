/**
 * lastVisited.js
 *
 */

var _cookieLastVisitedName1 = "TMKLastVisitedCookie1";
var _cookieLastVisitedName2 = "TMKLastVisitedCookie2";
var _cookieLastVisitedName3 = "TMKLastVisitedCookie3";
var _numberOfItems = 3;
var _separator = "|||";

function getArticle(cookie) {
	var article = null;
	try {
		// check if cookie exists
		if (APP.readCookie(cookie) != null) {
			art1 = unescape(_unserialize(APP.readCookie(cookie)));
			var aux = art1.split(_separator);
			if (aux.length == 9) {
				article = new Article(aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux[6], aux[7], aux[8]);
			}
		}
	} catch(e) {
		// TODO
	}
	return article;
}

function setArticle(cookieName, article) {
	APP.createCookie(cookieName, _serialize(escape(article.serialize())), null);
}

function addLastVisited(article) {
	var articleList = null;

	if (article == null) {
		return;
	}

	var article1 = null;
	var article2 = null;
	var article3 = null;

	article1 = getArticle(_cookieLastVisitedName1);
	if (article1 && article.getArticleId() == article1.getArticleId()) {
		return;
	}

	article2 = getArticle(_cookieLastVisitedName2);
	if (article2 && article.getArticleId() == article2.getArticleId()) {
		return;
	}

	article3 = getArticle(_cookieLastVisitedName3);
	if (article3 && article.getArticleId() == article3.getArticleId()) {
		return;
	}

	article3 = article2;
	article2 = article1;
	article1 = article;

	// create cookie
	setArticle(_cookieLastVisitedName1, article1);
	if (article2) {
		setArticle(_cookieLastVisitedName2, article2);
	}
	if (article3) {
		setArticle(_cookieLastVisitedName3, article3);
	}
	return;
}

function renderLastVisited(divTarget) {
	var article1 = null;
	var article2 = null;
	var article3 = null;

	article1 = getArticle(_cookieLastVisitedName1);

	article2 = getArticle(_cookieLastVisitedName2);

	article3 = getArticle(_cookieLastVisitedName3);

	var articleList = null;
	if (article1 || article2 || article3) {
		articleList = new Array(3);
		articleList[0] = article1;
		articleList[1] = article2;
		articleList[2] = article3;
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
	try {
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
			    	HTML = HTML + '<a href="javascript:APP.cartAdd(\"' + article.getArticleId() + '\");window.scrollTo(0,0);" rel="nofollow">' +
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
	} catch (e) {
		HTML = getNoItems();
	}
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

	this.serialize = function () {
			return this._url + _separator + this._title + _separator + this._urlPrincipalAttribute + _separator + this._principalAttribute + _separator + this._urlGroup + _separator + this._group + _separator + this._price + _separator +  this._available + _separator + this._id;
		};
}