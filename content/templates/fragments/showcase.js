/* showcase.js */
APP.addData('showcaseFilter', 'Recommended');

function fillShowCase(filter, callback) {
    var commentsHTML = '';
    var defaultFilter = APP.getData('showcaseFilter');

    if (filter == null) {
        filter = defaultFilter;
    } else {
        APP.addData('showcaseFilter', filter);
    }

    section = filter;

    try {
    	section = filter + '-Books';
        if (APP.getData('showcase')[section]) {
            sliderBooksHTML = APP.getData('showcase')[section];
            tooltipBooksHTML = APP.getData('tooltip')[section];
        }
        section = filter + '-Music';
        if (APP.getData('showcase')[section]) {
            sliderMusicHTML = APP.getData('showcase')[section];
            tooltipMusicHTML = APP.getData('tooltip')[section];
        }
        section = filter + '-Movies';
        if (APP.getData('showcase')[section]) {
            sliderMoviesHTML = APP.getData('showcase')[section];
            tooltipMoviesHTML = APP.getData('tooltip')[section];
        }
        section = filter + '-Games';
        if (APP.getData('showcase')[section]) {
            sliderGamesHTML = APP.getData('showcase')[section];
            tooltipGamesHTML = APP.getData('tooltip')[section];
        }
        section = filter + '-Section';
        if (APP.getData('showcase')[section]) {
            sliderSectionHTML = APP.getData('showcase')[section];
            tooltipSectionHTML = APP.getData('tooltip')[section];
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
    if (document.getElementById('tooltip_content_section')) {
        document.getElementById('tooltip_content_section').innerHTML = tooltipSectionHTML;
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
    if (document.getElementById('slider')) {
        document.getElementById('slider').innerHTML = sliderSectionHTML;
        $('#sliderSection').tinycarousel({ axis: 'y', display: 1} );
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

$('ul.overview td.product-entry').qtip({
    content: function () {
        return this.find('div.product-popup-content').html();
        },
    position: {
        my: 'left center',
        at: 'right center',
        viewport: $(this)
        },
    style: {
        classes: 'ui-tooltip-rounded ui-tooltip-light'
        },
    hide: {
        delay: 300,
        fixed: true
        }
});
