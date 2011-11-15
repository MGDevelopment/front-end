/**
 * showcase.js
 */
TMK.addData('showcaseFilter_order', 'TMK_RDA');
TMK.addData('showcaseFilter_filter', 'T');

function fillShowCase(order, filter, callback) {
	var commentsHTML = '';
	var defaultOrder = TMK.getData('showcaseFilter_order');
	var defaultFilter = TMK.getData('showcaseFilter_filter');
	
	if (order == null) {
		order = defaultOrder;
	} else {
		TMK.addData('showcaseFilter_order', order);
	}
	
	if (filter == null) {
		filter = defaultFilter;
	} else {
		TMK.addData('showcaseFilter_filter', filter);
	}
	
	section = order + filter;
	
	try {
		if (TMK.getData('showcase')[section + 'books']) {
			sliderBooksHTML = TMK.getData('showcase')[section + 'books'];
			tooltipBooksHTML = TMK.getData('tooltip')[section + 'books'];
		}
		if (TMK.getData('showcase')[section + 'music']) {
			sliderMusicHTML = TMK.getData('showcase')[section + 'music'];
			tooltipMusicHTML = TMK.getData('tooltip')[section + 'music'];
		}
		if (TMK.getData('showcase')[section + 'movies']) {
			sliderMoviesHTML = TMK.getData('showcase')[section + 'movies'];
			tooltipMoviesHTML = TMK.getData('tooltip')[section + 'movies'];
		}
		if (TMK.getData('showcase')[section + 'games']) {
			sliderGamesHTML = TMK.getData('showcase')[section + 'games'];
			tooltipGamesHTML = TMK.getData('tooltip')[section + 'games'];
		}
		if (TMK.getData('showcase')[section + 'books']) {
			sliderSectionHTML = TMK.getData('showcase')[section + 'books'];
			tooltipSectionHTML = TMK.getData('tooltip')[section + 'books'];
		}
	} catch (e) {
		sliderBooksHTML = 'Sin comentarios';
		sliderMusicHTML = 'Sin comentarios';
		sliderMoviesHTML = 'Sin comentarios';
		sliderGamesHTML = 'Sin comentarios';
		sliderSectionHTML = 'Sin comentarios';
		tooltipBooksHTML = 'Sin comentarios';
		tooltipMusicHTML = 'Sin comentarios';
		tooltipMoviesHTML = 'Sin comentarios';
		tooltipGamesHTML = 'Sin comentarios';
		tooltipSectionHTML = 'Sin comentarios';
	}
	// render
	if (document.getElementById('tooltip_content_books')) {
		document.getElementById('tooltip_content_books').innerHTML = tooltipBooksHTML;
	}
	if (document.getElementById('tooltip_content_music')) {
		document.getElementById('tooltip_content_music').innerHTML = tooltipMusicHTML;
	}
	if (document.getElementById('tooltip_content_movies')) {
		document.getElementById('tooltip_content_movies').innerHTML = tooltipMoviesHTML;
	}
	if (document.getElementById('tooltip_content_games')) {
		document.getElementById('tooltip_content_games').innerHTML = tooltipGamesHTML;
	}
	if (document.getElementById('tooltip_content_section_books')) {
		document.getElementById('tooltip_content_section_books').innerHTML = tooltipSectionHTML;
	}
	
	if (document.getElementById('sliderBooks')) {
		document.getElementById('sliderBooks').innerHTML = sliderBooksHTML;
		$('#sliderHomeBooks').tinycarousel({ axis: 'y', display: 1} );
	}
	if (document.getElementById('sliderMusic')) {
		document.getElementById('sliderMusic').innerHTML = sliderMusicHTML;
		$('#sliderHomeMusic').tinycarousel({ axis: 'y', display: 1} );
	}
	if (document.getElementById('sliderMovies')) {
		document.getElementById('sliderMovies').innerHTML = sliderMoviesHTML;
		$('#sliderHomeMovies').tinycarousel({ axis: 'y', display: 1} );
	}
	if (document.getElementById('sliderGames')) {
		document.getElementById('sliderGames').innerHTML = sliderGamesHTML;
		$('#sliderHomeGames').tinycarousel({ axis: 'y', display: 1} );
	}
	if (document.getElementById('sliderbooks')) {
		document.getElementById('sliderbooks').innerHTML = sliderSectionHTML;
		$('#sliderSectionbooks').tinycarousel({ axis: 'y', display: 1} );
	}
	$(".inline").colorbox({opacity: 0, inline:true, width:"400px"});
	
	try {
		if (callback && typeof (callback) === "function") {
			// execute the callback, passing parameters as necessary
			callback(section);
		}
	} catch (e) {
		// TODO: handle exception
	}
	return;
}