/**
 * relatedProduct.js
 */
function fillRelatedProduct(callback) {
    var relatedDetailHTML = '';

    try {
        if (APP.getData('relatedProduct')) {
            relatedDetailHTML = APP.getData('relatedProduct');
        }
    } catch (e) {
        relatedDetailHTML = '<!-- Sin datos -->';
    }
    if (document.getElementById('related_detail')) {
        document.getElementById('related_detail').innerHTML = relatedDetailHTML;
    }

    try {
        if (callback && typeof (callback) === "function") {
            // execute the callback, passing parameters as necessary
            callback();
        }
    } catch (e) {
        // TODO: handle exception
    }
    return;
}