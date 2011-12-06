/**
 * related.js
 */
APP.addData('relatedFilter_order', 'OPT1');

function fillRelated(order, callback) {
	var relatedHTML = '';
	var defaultOrder = APP.getData('relatedFilter_order');

	if (order == null) {
		order = defaultOrder;
	} else {
		order = 'OPT' + order;
		APP.addData('relatedFilter_order', order);
	}

	try {
		if (APP.getData('related')[order]) {
			relatedHTML = APP.getData('related')[order];
		}

	} catch (e) {
		relatedHTML = '<!-- Sin datos -->';
	}
	// render
	if (document.getElementById('relatedSection')) {
		document.getElementById('relatedSection').innerHTML = relatedHTML;
	}

	var pageCount = 1;
	if (document.getElementById('relatedPageCount')) {
		pageCount = document.getElementById('relatedPageCount').value;
	}
	if (pageCount > 1) {
		var display = pageCount;
		if (pageCount > 5) {
			display = 5;
		}
		$("#paginator").paginate({
			count 		: pageCount,
			start 		: 1,
			display     : display,
			border					: true,
			border_color			: '#BEF8B8',
			text_color  			: '#68BA64',
			background_color    	: '#E3F2E1',
			border_hover_color		: '#68BA64',
			text_hover_color  		: 'black',
			background_hover_color	: '#CAE6C6',
			images					: false,
			mouse					: 'press',
			onChange     			: function(page){
										$('._current','#paginationdemo').removeClass('_current').hide();
										$('#p'+page).addClass('_current').show();
									  }
		});
	}

	try {
		if (callback && typeof (callback) === "function") {
			// execute the callback, passing parameters as necessary
			callback(order);
		}
	} catch (e) {
		// TODO: handle exception
	}
	return;
}