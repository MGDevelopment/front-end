    function carrito_AgregarArticulo(idArticulo) {
        $('#modalBack').css("display", "block");
        $('#modalBack').css("visibility", "visible");
        var param = 'idArticulo=' + idArticulo + '&par=' + Math.random();
        $.ajax({
               type: "POST",
               cache:false,
               url: "/AgregarArticulo",
               data: param,
               success: function (msg) {
                    var obj= jQuery.parseJSON(msg);
                    carrito_AlertCarrito(obj.Articulo);
                    carrito_SetCarrito(obj.Carrito);
               }
        });
    }

    function carrito_AlertCarrito(articulo) {
        if (articulo.cls_error) {
            $('#msgCarritoERROR').get(0).innerHTML = articulo.cls_msgError;
            $('#msgCarritoERROR').get(0).style.display='';
            $('#spnPrecioCarrito').get(0).style.display='none';
            //$('#carritoImagen').get(0).src = articulo.cls_urlImagen;
            $('#divCarrito').get(0).className = 'efectoCarritoModError';
        } else {
            $('#msgCarritoOK').get(0).innerHTML = articulo.titulo;
            $('#precioCarrito').get(0).innerHTML = formatCurrency(articulo.cls_precio);
            $('#carritoImagen').get(0).src = articulo.cls_urlImagen;
            $('#spnPrecioCarrito').get(0).style.display='';
            $('#msgCarritoERROR').get(0).style.display='none';
            $('#divCarrito').get(0).className = 'efectoCarritoMod';

            $('#divCarrito').get(0).style.top =getScrollXY()[1]+ window.screen.height/2 -174 + "px";
        }
        $('#divCarrito').get(0).style.display = '';
    }

    function carrito_CloseCarrito() {
        $('#divCarrito').get(0).style.display = 'none';
        $('#modalBack').get(0).style.display = 'none';

    }

    function carrito_Pedir(idArticulo) {
        if (confirm('Este producto no est&aacute; disponible actualmente. Desea hacer un pedido?')) {
            document.location = '/PedidoEspecial?ID_ARTICULO=' + idArticulo;
        }
    }

    function carrito_ActualizarCarrito() {
        $.ajax({
               type: "POST",
               url: "/GetInfoCarrito",
               data: 'par=' + Math.random(),
               cache: false,
               success: function(msg){
                    var obj= jQuery.parseJSON(msg);
                    carrito_SetCarrito(obj.Carrito);
               }
        });
    }

    function carrito_SetCarrito(objCarrito) {
        if (objCarrito!= null && typeof(objCarrito.cantidad) != undefined && objCarrito.cantidad < 1) {
            $('#textoCarrito').get(0).innerHTML = 'No hay<br/> items'
        } else {
            if(objCarrito !=null && typeof(objCarrito.cantidad) != undefined) {
                $('#textoCarrito').get(0).innerHTML =  objCarrito.cantidad + ((objCarrito.cantidad>1)?' items':' item') + '<br/>$ ' + formatCurrency(objCarrito.total);
            }
        }
    }

    //para compatibilidad con el detalle de articulo generado
    function agregarProducto(idArticulo) {
        carrito_AgregarArticulo(idArticulo);
    }

    function formatCurrency(num) {
        num = num.toString().replace(/\$|\,/g,'');
        if (isNaN(num))
          num = 0;
        var signo = (num == (num = Math.abs(num)));
        num = Math.floor(num * 100 + 0.50000000001);
        cents = num % 100;
        num = Math.floor(num / 100).toString();
        if (cents < 10)
          cents = '0' + cents;
        for (var i = 0; i < Math.floor((num.length - (1 + i)) / 3); i++)
            num = num.substring(0, num.length - (4 * i + 3)) + ',' + num.substring(num.length - (4 * i + 3));

        return (((signo) ? '' : '-') + num + '.' + cents);
    }
