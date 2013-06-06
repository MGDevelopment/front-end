{%- import 'macros/productComments.html' as render -%}
/**
* Name:
*     - product-comments.js
* expected keys:
*    - ArticleId
*    - SubjectId
*     - Comments
*         - Date ?
*/
var dataComments = {};

{%- if d -%}
dataComments['detail'] = '{{ render.renderComments(d.EntityId, d.Categoria_Seccion, d["Comments"], url)|replace("\n", "") }}';
{% endif %}

function loadComments() {
    APP.addData('comments', dataComments);
    return;
}

loadComments();

function showAllComments(divName) {
    if (document.getElementById('plus_minus')) {
        if (document.getElementById('plus_minus').innerHTML == '+') {
            document.getElementById('plus_minus').innerHTML = '-';
        } else {
            document.getElementById('plus_minus').innerHTML = '+';
        }
    }
    $('#'+divName).toggle();
}