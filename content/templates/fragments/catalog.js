/**
 * catalog.js
 */
APP.addData('catalogFilter_order', 'OPT1');

function fillCatalog(order, callback) {
    var catalogHTML = '';
    var defaultOrder = APP.getData('catalogFilter_order');

    if (order == null) {
        order = defaultOrder;
    } else {
        order = 'OPT' + order;
        APP.addData('catalogFilter_order', order);
    }

    try {
        if (APP.getData('catalog')[order]) {
            catalogHTML = APP.getData('catalog')[order];
        }

    } catch (e) {
        catalogHTML = '<!-- Sin datos -->';
    }
    // render
    if (document.getElementById('catalogSection')) {
        document.getElementById('catalogSection').innerHTML = catalogHTML;
    }

    var pageCount = 1;
    if (document.getElementById('catalogPageCount')) {
        pageCount = document.getElementById('catalogPageCount').value;
    }
    if (pageCount > 1) {
        var display = pageCount;
        if (pageCount > 5) {
            display = 5;
        }
        $("#paginator").paginate({
            count         : pageCount,
            start         : 1,
            display     : display,
            border                    : true,
            border_color            : '#BEF8B8',
            text_color              : '#68BA64',
            background_color        : '#E3F2E1',
            border_hover_color        : '#68BA64',
            text_hover_color          : 'black',
            background_hover_color    : '#CAE6C6',
            images                    : false,
            mouse                    : 'press',
            onChange                 : function(page){
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
