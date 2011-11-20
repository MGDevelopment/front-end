APP = (function() {

    // Internal (unreachable)
    var _data    = {};    // Stored data
    var _session = false; // Is there a site session cookie?

    // Cookie methods inspired by quirksmode.org
    function createCookie(name, value, days) {

        var cookie = name + "=" + value;
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            cookie += "; expires=" + date.toGMTString();
        }

        document.cookie = cookie + "; path=/";
    }

    function readCookie(name) {

        if (!document.cookie)
            return null; // No cookie

        var nameEQ = name + "=";
        var ca = document.cookie.split(';'); // Split cookies

        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];                    // This cookie
            while (c.charAt(0) == ' ')
                c = c.substring(1, c.length); // Remove leading spaces
            if (c.indexOf(nameEQ) == 0)
                return c.substring(nameEQ.length, c.length); // Found
        }

        return null; // Not found
    }

    function eraseCookie(name) {

        createCookie(name, "", -1); // Cookie overwritten with expired
    }
    
    function getStatus() {

        return readCookie('status'); // Return status cookie (to be parsed)
    }

    //
    // Application methods
    //

    function getStatus() {

        var statusCookie = readCookie('status')
        if (!statusCookie)
            return false;

        var statusVars = statusCookie.split(',');
        var statusMap = {};
        for (var i = 0; i < statusVars.length; i++) {
            var kv = statusVars[i].split(':'); // key:value -> [key, value]
            statusMap[kv[0]] = kv[1];
        }

        return statusMap;
    }
    
    function checkSession() {
        _session = document.cookie.indexOf('JSESSIONID') != -1;
    }

    function cartAdd(idArticulo) {
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
                    cartAlert(obj.Articulo);
                    cartSet(obj.Carrito);
               }
        });
    }

    function cartAlert(articulo) {
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

    function cartClose() {
        $('#divCarrito').get(0).style.display = 'none';
        $('#modalBack').get(0).style.display = 'none';

    }

    function cartSpecialRequest(idArticulo) {
        if (confirm('Este producto no est&aacute; disponible actualmente. Desea hacer un pedido?')) {
            document.location = '/PedidoEspecial?ID_ARTICULO=' + idArticulo;
        }
    }

    function cartUpdate() {
        if (!_session)
            return; /* nothing to do */
        $.ajax({
               type: "POST",
               url: "/GetInfoCarrito",
               data: 'par=' + Math.random(),
               cache: false,
               success: function(msg){
                    var obj= jQuery.parseJSON(msg);
                    cartSet(obj.Carrito);
               }
        });
    }

    function cartSet(objCarrito) {
        if (objCarrito!= null && typeof(objCarrito.cantidad) != undefined && objCarrito.cantidad < 1) {
            $('#textoCarrito').get(0).innerHTML = 'No hay<br/> items'
        } else {
            if(objCarrito !=null && typeof(objCarrito.cantidad) != undefined) {
                $('#textoCarrito').get(0).innerHTML =  objCarrito.cantidad + ((objCarrito.cantidad>1)?' items':' item') + '<br/>$ ' + formatCurrency(objCarrito.total);
            }
        }
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
    
    function init() {

        checkSession();
        cartUpdate();

    }

    return {
        addData: function(name, value) {
            _data[name] = value;
        },
        getData: function(name) {
            return _data[name];
        },
        cartAdd:   cartAdd,
        init:      init
    }
})();
