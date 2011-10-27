var tempo = 10;

function mostrarBuscarPor(filtro, idBuscador, idDropdown) {
    var elementoBusqueda = document.getElementById(idBuscador);
    if (elementoBusqueda != null) {
        elementoBusqueda.innerHTML = document.getElementById(filtro).innerHTML
    }
    var opciones = document.getElementById(idDropdown);
    if (opciones != null) {
        opciones.style.display = 'none'
    }
}
function mostrarBuscarPor(filtro, idBuscador, idDropdown, idSeccion, idSeccionPropia, seccionBusqueda) {
    var elementoBusqueda = document.getElementById(idBuscador);
    if (elementoBusqueda != null) {
        elementoBusqueda.innerHTML = document.getElementById(filtro).innerHTML
    }
    var opciones = document.getElementById(idDropdown);
    if (opciones != null) {
        opciones.style.display = 'none'
    }
    $('#idSeccion').get(0).value = idSeccion;
    $('#idSeccionPropia').get(0).value = idSeccionPropia;
    $('#seccionBusqueda').get(0).value = seccionBusqueda
}
function ocultarOpciones(idDropdown) {
    var opciones = document.getElementById(idDropdown);
    if (opciones != null) {
        opciones.style.display = 'none'
    }
}
function ocultarOpcionesT(idObjeto) {
    tempo = setTimeout("ocultarOpciones('" + idObjeto + "')", 200)
}
function desplegarOpciones(idDropdown) {
    var opciones = document.getElementById(idDropdown);
    if (opciones != null) {
        if (opciones.style.display == 'inline') {
            opciones.style.display = 'none'
        } else {
            opciones.style.display = 'inline'
        }
    }
}