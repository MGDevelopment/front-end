'''
Created on 01/10/2011
Proceso de generacion de la HOME de Tematika.

@author: mgoldsman
'''
"""
"""
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

# OUT directory
#outDir = '/Users/mgoldsman/workspaces/python_workspace/PythonJinja/src/tmk/out/'
outDir = './out/'
# templates temporales
#tmpTree = "tmpTree.html"
tmpComments = "tmpComments.html"
tmpSlider = "tmpSlider.html"
tmpToolTip = "tmpToolTip.html"
# doc base para recuperar los templates
tplDocBase = "tmk"
# templates de las paginas
tplHome = "tplHome.html"
# templates de los componentes
cmpHead = "cmpHead.html"
cmpFooter = "cmpFooter.html"
cmpMetaTag = "cmpMetaTag.html"
cmpCss = "cmpCss.html"
cmpJavaScriptTop = "cmpJavaScriptTop.html"
cmpJavaScriptBottom = "cmpJavaScriptBottom.html"
cmpTop = 'cmpTop.html'
cmpMessages = 'cmpMessages.html'
cmpExtra = 'cmpExtra.html'
cmpShowCase = 'cmpShowCase.html'
cmpRightMenu = 'cmpRightMenu.html'
#cmpTree = 'cmpTree.html'
cmpComments = 'cmpComments.html'
cmpLastVisited = 'cmpLastVisited.html'
# template de los componentes JS
jsHomeComments = 'js-home-comments.tmp'
jsHomeMessages = 'js-home-messages.tmp'
jsHomeShowCase = 'js-home-showcase.tmp'
jsHomeToolTip = 'js-home-tooltip.tmp'
# valores globales (exportar a otro modulo)
SECCION_HOME = 0;
SECCION_LIBRO = 1;
SECCION_REVISTAS = 2;
SECCION_JUGUETES = 3;
SECCION_MUSICA = 4;
SECCION_PELICULA = 5;
# info que se necesita para la generacion
siteDomain = "www.tematika.com"
messageData = {
    "mensajes" : {
        "lista" : [
                {
                    "id" : "297",
                    "texto" : "<a href=\"http://oblogo.com\" target=\"_blank\"><IMG SRC=\"/imagenes/grupos/cartelera/oblogo.jpg\" border=\"0\" ALT=\"Oblogo\"></a><br/></div>Con tu compra en Tematika.com recibir&aacute;s de regalo un ejemplar de la revista Oblogo, la revista que publica lo mejor de la blog&oacute;sfera."
                },{
                   "id" : "41",
                   "texto" : '<div style="font-weight:bold;"&gt;Promoci&amp;oacute;n en Tematika.com:<br/&gt; </div&gt;Env&amp;iacute;o Gratis en Argentina con tus compras mayores a $150.- No acumulable con otras promociones.'
                   },{
                    "id" : "46",
                    "texto" : '<div style="font-weight:bold;"&gt;<a href="/articulo/detalleArticulo.jsp?idArticulo=493735&amp;ID_ALIANZA=1139&amp;ID_SECCION=1089"&gt;Videomatch &amp; Showmatch</a&gt;<br/&gt;</div&gt;Una resenia fotogr&amp;aacute;fica y biogr&amp;aacute;fica de las dos d&amp;eacute;cadas de vida de este &amp;eacute;xito que arranc&amp;oacute; el 1 de marzo de1990. (env&amp;iacute;o gratis en Argentina hasta el 30 de Junio)'
                } ]
    }
}

searchOpts = {
    "options": [
             {
                "idOpt" : "optBus1",
                "txtOpt" : "Todo el Sitio",
                "idSeccion" : SECCION_HOME,
                "seccionBusqueda" : "En Tematika.com",
                "idSeccionPropia" : SECCION_HOME,
                "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(SECCION_HOME)
            },{
                "idOpt" : "optBus2",
                "txtOpt" : "En Libros",
                "idSeccion" : SECCION_LIBRO,
                "seccionBusqueda" : "En Libros",
                "idSeccionPropia" : SECCION_LIBRO,
                "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(SECCION_LIBRO)
            }
                  ]
    }
menuData = {
            "secciones" : [{"idSeccion" : "seccion200"}, {"idSeccion" : "seccion300"}, {"idSeccion" : "seccion400"}]
            }

commentsData ={
                
            "articulos" : [{"urlDetalle" : "/libros/esoterismo--6/ocultismo--4/en_general--1/radiestesia--3886.htm", "calificacionXArticulo" : [{"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}], "class" : "tapaLibros", "altImagen" : "Radiestesia - en_general - ocultismo - esoterismo - libros", "titulo" : "Radiestesia", "llevaLineaDivisora" : "true", "enSeccion" : "libros", "urlImagen" : "/tapas/sitio/3886c0.jpg", "comentario" : "Mi querido H&eacute;ctor Morel, ha expresado en esta obra genial, una de las tantas materias en las que des...", "comentador" : "Nick 3886/3999"}, 
                {"urlDetalle" : "/libros/humanidades--2/biografias_y_relatos--8/biografias--1/sobre_la_lectura--381237.htm", "calificacionXArticulo" : [{"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}], "class" : "tapaLibros", "altImagen" : "Sobre_la_Lectura - biografias - biografias_y_relatos - humanidades - libros", "titulo" : "Sobre la Lectura", "llevaLineaDivisora" : "true", "enSeccion" : "libros", "urlImagen" : "/tapas/sitio/381237c0.jpg", "comentario" : "Es Proust, como siempre un estilo narrativo muy elaborado e impecable. El libro trata de la experien...", "comentador" : "Nick 381237/11883"}, 
                {"urlDetalle" : "/libros/infantil_y_juvenil--18/entretenimientos--9/generales--1/magia_ciencia--389085.htm", "calificacionXArticulo" : [{"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStarDes"}], "class" : "tapaLibros", "altImagen" : "Magia_Ciencia - generales - entretenimientos - infantil_y_juvenil - libros", "titulo" : "Magia Ciencia", "llevaLineaDivisora" : "true", "enSeccion" : "libros", "urlImagen" : "/tapas/sitio/389085c0.jpg", "comentario" : "MUY INTERESANTE, YA REALICE ALGUNOS TRUCOS CON MIS ALUMNOS Y LES ENACANTARON. ALTAMENTE RECOMENDABLE", "comentador" : "Nick 389085/15705"}, 
                {"urlDetalle" : "/libros/ficcion_y_literatura--1/novelas--1/historica--11/el_husar--407797.htm", "calificacionXArticulo" : [{"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}, {"estrellaClass" : "calificacionStar"}], "class" : "tapaLibros", "altImagen" : "El_Husar - historica - novelas - ficcion_y_literatura - libros", "titulo" : "El Husar", "llevaLineaDivisora" : "", "enSeccion" : "libros", "urlImagen" : "/tapas/sitio/407797c0.jpg", "comentario" : "Brillante libro que muestra lo rom&aacute;ntico de la ilusi&oacute;n y la cruel realidad de una batalla.", "comentador" : "Nick 407797/18012"}]
                }

sliderDataTMK_RDAM = {"articulos" : [{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"}]              
              }
sliderDataTMK_RDAY = {"articulos" : [{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"}]              
              }
sliderDataTMK_RDAT = {"articulos" : [{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"}]              
              }
sliderDataMVM = {"articulos" : [{"img_src" : "http://static.flickr.com/58/199481143_3c148d9dd3_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"}]              
              }
sliderDataMVY = {"articulos" : [{"img_src" : "http://static.flickr.com/72/199481203_ad4cdcf109_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"}]              
              }
sliderDataMVT = {"articulos" : [{"img_src" : "http://static.flickr.com/58/199481218_264ce20da0_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"}]              
              }
sliderDataMPM = {"articulos" : [{"img_src" : "http://static.flickr.com/69/199481255_fdfe885f87_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"}]              
              }
sliderDataMPY = {"articulos" : [{"img_src" : "http://static.flickr.com/60/199480111_87d4cb3e38_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"}]              
              }
sliderDataMPT = {"articulos" : [{"img_src" : "http://static.flickr.com/70/229228324_08223b70fa_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"}]              
              }
sliderDataMVAM = {"articulos" : [{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/70/229228324_08223b70fa_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"},{"img_src" : "http://static.flickr.com/57/199481087_33ae73a8de_s.jpg"}]              
              }
sliderDataMVAY = {"articulos" : [{"img_src" : "http://static.flickr.com/70/229228324_08223b70fa_s.jpg"},{"img_src" : "http://static.flickr.com/70/229228324_08223b70fa_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"},{"img_src" : "http://static.flickr.com/75/199481072_b4a0d09597_s.jpg"}]              
              }
sliderDataMVAT = {"articulos" : [{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"},{"img_src" : "http://static.flickr.com/77/199481108_4359e6b971_s.jpg"}]              
              }
# seteo del ambiente para recuperar los archivos template y componentes
env = Environment(loader=FileSystemLoader(tplDocBase))

class Home: 
    def __init__(self, temp=tplHome):
        self.template = env.get_template(temp)
        
    def generate(self, params=""):
        return self.template.render(params)

class CMPGeneric:
    def __init__(self, temp):
        self.template = env.get_template(temp)
        
    def generate(self, params=""):
        return self.template.render(params)

class FileGenerate:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def generate(self, content):
        try:            
            # Genero los JS
            f = open(self.fileName, 'w')
            f.write(content)
            f.close()
        except Exception as e:
            print e
        
homeHTML = ""

# slider TMK_RDA
sliderHomeBooksTMK_RDAM = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
sliderHomeMusicTMK_RDAM = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAM})
sliderHomeMoviesTMK_RDAM = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAM})
sliderHomeGamesTMK_RDAM = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAM})
sliderHomeBooksTMK_RDAY = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
sliderHomeMusicTMK_RDAY = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAY})
sliderHomeMoviesTMK_RDAY = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAY})
sliderHomeGamesTMK_RDAY = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAY})
sliderHomeBooksTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMusicTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMoviesTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
sliderHomeGamesTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
sliderHomeBooksTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMusicTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMoviesTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
sliderHomeGamesTMK_RDAT = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
# slider MV
sliderHomeBooksMVM = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVM})
sliderHomeMusicMVM = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVM})
sliderHomeMoviesMVM = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVM})
sliderHomeGamesMVM = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVM})
sliderHomeBooksMVY = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVY})
sliderHomeMusicMVY = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVY})
sliderHomeMoviesMVY = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVY})
sliderHomeGamesMVY = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVY})
sliderHomeBooksMVT = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVT})
sliderHomeMusicMVT = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVT})
sliderHomeMoviesMVT = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVT})
sliderHomeGamesMVT = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVT})
# slider MP
sliderHomeBooksMPM = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMPM})
sliderHomeMusicMPM = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMPM})
sliderHomeMoviesMPM = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMPM})
sliderHomeGamesMPM = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMPM})
sliderHomeBooksMPY = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMPY})
sliderHomeMusicMPY = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMPY})
sliderHomeMoviesMPY = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMPY})
sliderHomeGamesMPY = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMPY})
sliderHomeBooksMPT = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMPT})
sliderHomeMusicMPT = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMPT})
sliderHomeMoviesMPT = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMPT})
sliderHomeGamesMPT = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMPT})
# slider MVA
sliderHomeBooksMVAM = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
sliderHomeMusicMVAM = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVAM})
sliderHomeMoviesMVAM = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVAM})
sliderHomeGamesMVAM = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVAM})
sliderHomeBooksMVAY = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
sliderHomeMusicMVAY = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVAY})
sliderHomeMoviesMVAY = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVAY})
sliderHomeGamesMVAY = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVAY})
sliderHomeBooksMVAT = CMPGeneric(tmpSlider).generate({'prefix': 'books', 'slider_data': sliderDataMVAT})
sliderHomeMusicMVAT = CMPGeneric(tmpSlider).generate({'prefix': 'music', 'slider_data': sliderDataMVAT})
sliderHomeMoviesMVAT = CMPGeneric(tmpSlider).generate({'prefix': 'movies', 'slider_data': sliderDataMVAT})
sliderHomeGamesMVAT = CMPGeneric(tmpSlider).generate({'prefix': 'games', 'slider_data': sliderDataMVAT})
# tooltip TMK_RDA
tooltipHomeBooksTMK_RDAM = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeMusicTMK_RDAM = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeMoviesTMK_RDAM = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeGamesTMK_RDAM = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeBooksTMK_RDAY = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeMusicTMK_RDAY = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeMoviesTMK_RDAY = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeGamesTMK_RDAY = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeBooksTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMusicTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMoviesTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeGamesTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeBooksTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMusicTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMoviesTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeGamesTMK_RDAT = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
# tooltip MV
tooltipHomeBooksMVM = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVM})
tooltipHomeMusicMVM = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVM})
tooltipHomeMoviesMVM = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVM})
tooltipHomeGamesMVM = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVM})
tooltipHomeBooksMVY = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVY})
tooltipHomeMusicMVY = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVY})
tooltipHomeMoviesMVY = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVY})
tooltipHomeGamesMVY = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVY})
tooltipHomeBooksMVT = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVT})
tooltipHomeMusicMVT = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVT})
tooltipHomeMoviesMVT = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVT})
tooltipHomeGamesMVT = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVT})
# tooltip MP
tooltipHomeBooksMPM = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMPM})
tooltipHomeMusicMPM = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMPM})
tooltipHomeMoviesMPM = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMPM})
tooltipHomeGamesMPM = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMPM})
tooltipHomeBooksMPY = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMPY})
tooltipHomeMusicMPY = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMPY})
tooltipHomeMoviesMPY = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMPY})
tooltipHomeGamesMPY = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMPY})
tooltipHomeBooksMPT = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMPT})
tooltipHomeMusicMPT = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMPT})
tooltipHomeMoviesMPT = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMPT})
tooltipHomeGamesMPT = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMPT})
# tooltip MVA
tooltipHomeBooksMVAM = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
tooltipHomeMusicMVAM = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVAM})
tooltipHomeMoviesMVAM = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVAM})
tooltipHomeGamesMVAM = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVAM})
tooltipHomeBooksMVAY = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
tooltipHomeMusicMVAY = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVAY})
tooltipHomeMoviesMVAY = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVAY})
tooltipHomeGamesMVAY = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVAY})
tooltipHomeBooksMVAT = CMPGeneric(tmpToolTip).generate({'prefix': 'books', 'slider_data': sliderDataMVAT})
tooltipHomeMusicMVAT = CMPGeneric(tmpToolTip).generate({'prefix': 'music', 'slider_data': sliderDataMVAT})
tooltipHomeMoviesMVAT = CMPGeneric(tmpToolTip).generate({'prefix': 'movies', 'slider_data': sliderDataMVAT})
tooltipHomeGamesMVAT = CMPGeneric(tmpToolTip).generate({'prefix': 'games', 'slider_data': sliderDataMVAT})

# Genero los JS
# comments
comments = CMPGeneric(tmpComments).generate({'comments_data' : commentsData, 'site_domain': siteDomain})
jsComments = CMPGeneric(jsHomeComments).generate({'comments_data_last' : comments, 'comments_data_books' : comments, 'comments_data_music' : comments, 'comments_data_movies' : comments})
FileGenerate(outDir + 'home-comments.js').generate(jsComments)    
# messages
jsMessages = CMPGeneric(jsHomeMessages).generate({'messages_data' : messageData})
FileGenerate(outDir + 'home-messages.js').generate(jsMessages)
# showcase
jsShowCase = CMPGeneric(jsHomeShowCase).generate({'showcase_data_TMK_RDAM' : {'books': sliderHomeBooksTMK_RDAM, 'music' : sliderHomeMusicTMK_RDAM, 'movies' : sliderHomeMoviesTMK_RDAM, 'games' : sliderHomeGamesTMK_RDAM},
                                                  'showcase_data_TMK_RDAY' : {'books': sliderHomeBooksTMK_RDAY, 'music' : sliderHomeMusicTMK_RDAY, 'movies' : sliderHomeMoviesTMK_RDAY, 'games' : sliderHomeGamesTMK_RDAY},
                                                  'showcase_data_TMK_RDAT' : {'books': sliderHomeBooksTMK_RDAT, 'music' : sliderHomeMusicTMK_RDAT, 'movies' : sliderHomeMoviesTMK_RDAT, 'games' : sliderHomeGamesTMK_RDAT},
                                                  'showcase_data_MVM' : {'books': sliderHomeBooksMVM, 'music' : sliderHomeMusicMVM, 'movies' : sliderHomeMoviesMVM, 'games' : sliderHomeGamesMVM},
                                                  'showcase_data_MVY' : {'books': sliderHomeBooksMVY, 'music' : sliderHomeMusicMVY, 'movies' : sliderHomeMoviesMVY, 'games' : sliderHomeGamesMVY},
                                                  'showcase_data_MVT' : {'books': sliderHomeBooksMVT, 'music' : sliderHomeMusicMVT, 'movies' : sliderHomeMoviesMVT, 'games' : sliderHomeGamesMVT},
                                                  'showcase_data_MPM' : {'books': sliderHomeBooksMPM, 'music' : sliderHomeMusicMPM, 'movies' : sliderHomeMoviesMPM, 'games' : sliderHomeGamesMPM},
                                                  'showcase_data_MPY' : {'books': sliderHomeBooksMPY, 'music' : sliderHomeMusicMPY, 'movies' : sliderHomeMoviesMPY, 'games' : sliderHomeGamesMPY},
                                                  'showcase_data_MPT' : {'books': sliderHomeBooksMPT, 'music' : sliderHomeMusicMPT, 'movies' : sliderHomeMoviesMPT, 'games' : sliderHomeGamesMPT},
                                                  'showcase_data_MVAM' : {'books': sliderHomeBooksMVAM, 'music' : sliderHomeMusicMVAM, 'movies' : sliderHomeMoviesMVAM, 'games' : sliderHomeGamesMVAM},
                                                  'showcase_data_MVAY' : {'books': sliderHomeBooksMVAY, 'music' : sliderHomeMusicMVAY, 'movies' : sliderHomeMoviesMVAY, 'games' : sliderHomeGamesMVAY},
                                                  'showcase_data_MVAT' : {'books': sliderHomeBooksMVAT, 'music' : sliderHomeMusicMVAT, 'movies' : sliderHomeMoviesMVAT, 'games' : sliderHomeGamesMVAT},
                                                  })
FileGenerate(outDir + 'home-showcase.js').generate(jsShowCase)
# tooltip
jsToolTip = CMPGeneric(jsHomeToolTip).generate({'tooltip_data_TMK_RDAM' : {'books': tooltipHomeBooksTMK_RDAM, 'music' : tooltipHomeMusicTMK_RDAM, 'movies' : tooltipHomeMoviesTMK_RDAM, 'games' : tooltipHomeGamesTMK_RDAM},
                                                  'tooltip_data_TMK_RDAY' : {'books': tooltipHomeBooksTMK_RDAY, 'music' : tooltipHomeMusicTMK_RDAY, 'movies' : tooltipHomeMoviesTMK_RDAY, 'games' : tooltipHomeGamesTMK_RDAY},
                                                  'tooltip_data_TMK_RDAT' : {'books': tooltipHomeBooksTMK_RDAT, 'music' : tooltipHomeMusicTMK_RDAT, 'movies' : tooltipHomeMoviesTMK_RDAT, 'games' : tooltipHomeGamesTMK_RDAT},
                                                  'tooltip_data_MVM' : {'books': tooltipHomeBooksMVM, 'music' : tooltipHomeMusicMVM, 'movies' : tooltipHomeMoviesMVM, 'games' : tooltipHomeGamesMVM},
                                                  'tooltip_data_MVY' : {'books': tooltipHomeBooksMVY, 'music' : tooltipHomeMusicMVY, 'movies' : tooltipHomeMoviesMVY, 'games' : tooltipHomeGamesMVY},
                                                  'tooltip_data_MVT' : {'books': tooltipHomeBooksMVT, 'music' : tooltipHomeMusicMVT, 'movies' : tooltipHomeMoviesMVT, 'games' : tooltipHomeGamesMVT},
                                                  'tooltip_data_MPM' : {'books': tooltipHomeBooksMPM, 'music' : tooltipHomeMusicMPM, 'movies' : tooltipHomeMoviesMPM, 'games' : tooltipHomeGamesMPM},
                                                  'tooltip_data_MPY' : {'books': tooltipHomeBooksMPY, 'music' : tooltipHomeMusicMPY, 'movies' : tooltipHomeMoviesMPY, 'games' : tooltipHomeGamesMPY},
                                                  'tooltip_data_MPT' : {'books': tooltipHomeBooksMPT, 'music' : tooltipHomeMusicMPT, 'movies' : tooltipHomeMoviesMPT, 'games' : tooltipHomeGamesMPT},
                                                  'tooltip_data_MVAM' : {'books': tooltipHomeBooksMVAM, 'music' : tooltipHomeMusicMVAM, 'movies' : tooltipHomeMoviesMVAM, 'games' : tooltipHomeGamesMVAM},
                                                  'tooltip_data_MVAY' : {'books': tooltipHomeBooksMVAY, 'music' : tooltipHomeMusicMVAY, 'movies' : tooltipHomeMoviesMVAY, 'games' : tooltipHomeGamesMVAY},
                                                  'tooltip_data_MVAT' : {'books': tooltipHomeBooksMVAT, 'music' : tooltipHomeMusicMVAT, 'movies' : tooltipHomeMoviesMVAT, 'games' : tooltipHomeGamesMVAT},
                                                  })
FileGenerate(outDir + 'home-tooltip.js').generate(jsToolTip)   
try:
    # Genero el temporal para los mensajes, arbol y comentarios
    #tree = CMPGeneric(tmpTree).generate()
    
    # Genero los parametros que va a necesitar la generacion del head
    headParams = {'metaTag' : CMPGeneric(cmpMetaTag).generate({'site_domain': siteDomain}),
                  'css' : CMPGeneric(cmpCss).generate()}
    
    # Genero los componentes que va a necesitar la home
    params = {'head' : CMPGeneric(cmpHead).generate(headParams),
              'bottom' : CMPGeneric(cmpFooter).generate(),
              'js_top' : CMPGeneric(cmpJavaScriptTop).generate(),
              'js_bottom' : CMPGeneric(cmpJavaScriptBottom).generate(),
              'top' : CMPGeneric(cmpTop).generate({'search_opts': searchOpts}),
              'messages' : CMPGeneric(cmpMessages).generate(),
              'extra' : CMPGeneric(cmpExtra).generate(),
              'showcase' : CMPGeneric(cmpShowCase).generate({'slider_home_books' : sliderHomeBooksTMK_RDAM, 'slider_home_music': sliderHomeMusicTMK_RDAM, 'slider_home_movies' : sliderHomeMoviesTMK_RDAM, 'slider_home_games' : sliderHomeGamesTMK_RDAM,
                                                             'tooltip_home_books' : tooltipHomeBooksTMK_RDAM, 'tooltip_home_music': tooltipHomeMusicTMK_RDAM, 'tooltip_home_movies' : tooltipHomeMoviesTMK_RDAM, 'tooltip_home_games' : tooltipHomeGamesTMK_RDAM}),
              'rightmenu' : CMPGeneric(cmpRightMenu).generate({'menu_data': menuData}),
              'comments' : CMPGeneric(cmpComments).generate(),
              'lastvisited' : CMPGeneric(cmpLastVisited).generate()
              }
    #'tree' : CMPGeneric(cmpTree).generate({'tree': tree}),
    # Generacion del HTML de la home
    homeHTML = Home().generate(params)
except Exception as e:
    print e

print homeHTML
FileGenerate(outDir + 'Home.html').generate(homeHTML)