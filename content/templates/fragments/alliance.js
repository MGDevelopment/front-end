/**
 * alliance.js
 */


function gup( varname ) {
    varname = varname.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+varname+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( window.location.href );
    if( results == null ) return ""; else return results[1];
}

function processAlliance(){
    if (gup("ID_ALIANZA") != "") {
        $.ajax({
            type: "GET",
            url: "/alianzas/alianzas.jsp?idArticulo={{ d.EntityId }}&ID_ALIANZA=" + gup('ID_ALIANZA') + "&ID_SECCION={{ d.Categoria_Seccion}}",
            dataType: "xml",
            success: function() {
            }
        });
    }
    return;
}

processAlliance();