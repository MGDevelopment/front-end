(function () {

var pProductId = 0,
    pCover     = 1,
    pTitle     = 2,
    pLink      = 3,
    pAuthor    = 4,
    pAuthorUrl = 5,
    pRank      = 6,
    pPrice     = 7,
    pDate      = 8;

APP.addData('catalog', [
{%- if d['Products'] -%}
	{%- for p in d['Products'] -%}
	    {%- if p['Authors'] and p['Authors'][0]|length > 0 -%}
	        {%- set author = p['Authors'][0]['ContributorName'].decode('utf-8')|e -%}
	        {%- set author_url = p['Authors'][0]['ContributorURL'] -%}
	    {%- else -%}
	        {%- set author = '' -%}
	        {%- set author_url = '' -%}
	    {%- endif -%}
	[
	{{ p['EntityId'] }},
	'{{ p['CoverSmall'] }}',
	'{{ p['Title'].decode('utf-8')|e }}',
	'{{ p['LinkBase'] }}',
	'{{ author }}',
	'{{ author_url }}',
	{{ p['Row_Number']|int }},
	{{ p['PriceAmount'] }},
	{{ p['PublishingDateValue'] }}
	]
	{%- if loop.index < loop.length -%}
	,
	{%- endif -%}
	{%- endfor %}
{%- endif -%}
]);

APP.fillCatalog = function (order, page) {

    function strCmp(a,b) {
        if (a < b) {
            return -1;
        } else if (a > b) {
            return 1;
        } else {
            return 0;
        }
    }

    var c = APP.getData('catalog');
    if (order === 'rank') {
        c.sort(function (a, b) { return a[pRank]  - b[pRank]; });
    } else if (order === 'price-low') {
        c.sort(function (a, b) { return a[pPrice] - b[pPrice]; });
    } else if (order === 'price-high') {
        c.sort(function (a, b) { return b[pPrice] - a[pPrice]; });
    } else if (order === 'date-low') {
        c.sort(function (a, b) { return a[pDate]  - b[pDate]; });
    } else if (order === 'date-high') {
        c.sort(function (a, b) { return b[pDate]  - a[pDate]; });
    } else if (order === 'name-low') {
        c.sort(function (a, b) { return strCmp(a[pTitle], b[pTitle]); });
    } else if (order === 'name-high') {
        c.sort(function (a, b) { return strCmp(b[pTitle], a[pTitle]); });
    }
        /* else keeps last sort */

    var pageElems = $('.moduleproductob');
    var perPage   = pageElems.length;
    var lastPage  = Math.ceil(c.length/perPage) - 1;
    var page = page || 0; /* default page zero */
    if (page > lastPage+1)
        page = lastPage+1;
    var pageStart = page * perPage;
    var pageEnd   = pageStart + perPage;
    var elems     = c.slice(pageStart, pageEnd); /* element of this page */

    pageElems.each(function (i, v) {

        if (elems.length <= i) {
        	$(v).hide();
    		return;
            //i = elems.length - 1; /* repeat last */
        }

        var e = elems[i];
        var productLink  = e[pLink] + '.htm';
        $(v).find('.celdafoto a')[0].href   = productLink;
        $(v).find('.celdafoto img')[0].src  = '{{ url.images }}' + e[pCover];
        $(v).find('.celdafoto img')[0].alt  = e[pTitle] + '- tapa';
        $(v).find('.celdacontenido a')[0].innerHTML = e[pTitle];
        $(v).find('.celdacontenido a')[0].href      = productLink;
        $(v).find('.celdacontenido a')[1].innerHTML = e[pAuthor];
        $(v).find('.celdacontenido a')[1].href      = e[pAuthorUrl];
        $(v).find('.celdapreciocomprar .Fprecio')[0].innerHTML = 'Precio $ ' + e[pPrice] + '.-';
        $(v).find('.divInfo a')[0].href    = productLink;
        $(v).find('.divInfo a img')[0].alt = e[pTitle];
        $(v).find('.divInfo a img')[0].title = e[pAuthor] + ' - ' + e[pTitle];
        $(v).find('.divComprarPedir a')[0].href = 'javascript:APP.cartAdd(' + e[pProductId] + ');window.scrollTo(0,0);';

    });

    var prevPage = page - 1;
    if (page == 0) {
        prevPage = 0;
    }
    var nextPage = page + 1;
    if (page == lastPage+1) {
        nextPage = page;
    }

    /* first and last links are prev and next */
    $('.celdapaginas a.FAyuda').each(function (i,v) {
    	if (lastPage == 0) {
    		// hide all links when no pages or only page
    		$(v).hide();
    	} else {
	    	if (i > lastPage+1) {
	    		if (v.id) {
	    			// hide page numbers out of range
	    			$(v).hide();
	    		}
	    	}
    		if (v.id == 'catalogPrev') {
    	    	if (nextPage == 1) {
    	    		$(v).hide();
    	    	} else {
    	    		$(v).show();
    	    	}
        	}
        	if (v.id == 'catalogNext') {
    	    	if (nextPage == lastPage+1) {
    	    		$(v).hide();
    	    	} else {
    	    		$(v).show();
    	    	}
        	}
	        if (i === 0) {
	            v.href = 'javascript:APP.fillCatalog(null,' + prevPage + ');';
	        } else if (i > lastPage+1) {
	            v.href = 'javascript:APP.fillCatalog(null,' + nextPage + ');';
	        } else {
	            if (i === page + 1) {
	                $(v).css({'font-weight' : 'bolder'});
	            } else {
	                $(v).css({'font-weight' : 'normal'});
	            }
	        }
    	}
    });

};

}());
