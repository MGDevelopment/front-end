/**
 * Name:
 *  - googleBooks.js
 *
 * fragment related:
 *  - googleBooks.html
 *
 * dependency:
 *     - info: http://code.google.com/intl/es-ES/apis/books/docs/viewer/developers_guide.html
 *
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
    {%- if d.Identifiers -%}
        viewer.load('ISBN:{{ d.Identifiers[0].IDValue }}', alertNotFound,
            alertInitialized);
    {%- else -%}
        // no ISBN
    {%- endif -%}
}

if (document.getElementById('viewerCanvas') != null) {
    google.setOnLoadCallback(initialize);
}