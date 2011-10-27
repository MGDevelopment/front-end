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
		if (TMK.getData('showcase')[section + 'Books']) {
			sliderBooksHTML = TMK.getData('showcase')[section + 'Books'];
			tooltipBooksHTML = TMK.getData('tooltip')[section + 'Books'];
		}
		if (TMK.getData('showcase')[section + 'Music']) {
			sliderMusicHTML = TMK.getData('showcase')[section + 'Music'];
			tooltipMusicHTML = TMK.getData('tooltip')[section + 'Music'];
		}
		if (TMK.getData('showcase')[section + 'Movies']) {
			sliderMoviesHTML = TMK.getData('showcase')[section + 'Movies'];
			tooltipMoviesHTML = TMK.getData('tooltip')[section + 'Movies'];
		}
		if (TMK.getData('showcase')[section + 'Games']) {
			sliderGamesHTML = TMK.getData('showcase')[section + 'Games'];
			tooltipGamesHTML = TMK.getData('tooltip')[section + 'Games'];
		}
	} catch (e) {
		sliderBooksHTML = 'Sin comentarios';
		sliderMusicHTML = 'Sin comentarios';
		sliderMoviesHTML = 'Sin comentarios';
		sliderGamesHTML = 'Sin comentarios';
		tooltipBooksHTML = 'Sin comentarios';
		tooltipMusicHTML = 'Sin comentarios';
		tooltipMoviesHTML = 'Sin comentarios';
		tooltipGamesHTML = 'Sin comentarios';
	}
	// render
	document.getElementById('tooltip_content_books').innerHTML = tooltipBooksHTML;
	document.getElementById('tooltip_content_music').innerHTML = tooltipMusicHTML;
	document.getElementById('tooltip_content_movies').innerHTML = tooltipMoviesHTML;
	document.getElementById('tooltip_content_games').innerHTML = tooltipGamesHTML;
	
	document.getElementById('sliderBooks').innerHTML = sliderBooksHTML;
	$('#sliderHomeBooks').tinycarousel({ axis: 'y', display: 1} );
	document.getElementById('sliderMusic').innerHTML = sliderMusicHTML;
	$('#sliderHomeMusic').tinycarousel({ axis: 'y', display: 1} );
	document.getElementById('sliderMovies').innerHTML = sliderMoviesHTML;
	$('#sliderHomeMovies').tinycarousel({ axis: 'y', display: 1} );
	document.getElementById('sliderGames').innerHTML = sliderGamesHTML;
	$('#sliderHomeGames').tinycarousel({ axis: 'y', display: 1} );
	
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