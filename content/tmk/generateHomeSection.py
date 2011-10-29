'''
Created on 01/10/2011
Proceso de generacion de la HOME de Secciones de Tematika.

@author: mgoldsman
'''
"""
"""

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from generatorClass import CMPGeneric, FileGenerate
import yaml


stream = open('./cfg/homeBooks.yaml')
cfg = yaml.load(stream)

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
                "idSeccion" : cfg['SECCION_HOME'],
                "seccionBusqueda" : "En Tematika.com",
                "idSeccionPropia" : cfg['SECCION_HOME'],
                "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(cfg['SECCION_HOME'])
            },{
                "idOpt" : "optBus2",
                "txtOpt" : "En Libros",
                "idSeccion" : cfg['SECCION_LIBRO'],
                "seccionBusqueda" : "En Libros",
                "idSeccionPropia" : cfg['SECCION_LIBRO'],
                "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(cfg['SECCION_LIBRO'])
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
env = Environment(loader=FileSystemLoader(cfg['tplDocBase']))
        
homeHTML = ""

# slider
jinjaSlider = CMPGeneric(env, cfg['tmpSlider'])
# slider TMK_RDA
sliderHomeBooksTMK_RDAM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
sliderHomeBooksTMK_RDAY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
sliderHomeBooksTMK_RDAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
sliderHomeBooksTMK_RDAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
# slider MV
sliderHomeBooksMVM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVM})
sliderHomeBooksMVY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVY})
sliderHomeBooksMVT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVT})
# slider MP
sliderHomeBooksMPM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPM})
sliderHomeBooksMPY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPY})
sliderHomeBooksMPT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPT})
# slider MVA
sliderHomeBooksMVAM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
sliderHomeBooksMVAY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
sliderHomeBooksMVAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAT})
# tooltip
jinjaToolTip = CMPGeneric(env, cfg['tmpToolTip'])
# tooltip TMK_RDA
tooltipHomeBooksTMK_RDAM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeBooksTMK_RDAY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeBooksTMK_RDAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeBooksTMK_RDAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
# tooltip MV
tooltipHomeBooksMVM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVM})
tooltipHomeBooksMVY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVY})
tooltipHomeBooksMVT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVT})
# tooltip MP
tooltipHomeBooksMPM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPM})
tooltipHomeBooksMPY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPY})
tooltipHomeBooksMPT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPT})
# tooltip MVA
tooltipHomeBooksMVAM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
tooltipHomeBooksMVAY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
tooltipHomeBooksMVAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAT})

# Genero los JS
# comments
comments = CMPGeneric(env, cfg['tmpComments']).generate({'comments_data' : commentsData, 'site_domain': cfg['siteDomain']})
jsComments = CMPGeneric(env, cfg['jsHomeComments']).generate({'comments_data_last' : comments, 'comments_data_books' : comments, 'comments_data_music' : comments, 'comments_data_movies' : comments})
FileGenerate(cfg['outDir'] + cfg['home-comments-file']).generate(jsComments)    
# showcase
jsShowCase = CMPGeneric(env, cfg['jsHomeShowCase']).generate({'showcase_data_TMK_RDAM' : {'books': sliderHomeBooksTMK_RDAM},
                                                  'showcase_data_TMK_RDAY' : {'books': sliderHomeBooksTMK_RDAY},
                                                  'showcase_data_TMK_RDAT' : {'books': sliderHomeBooksTMK_RDAT},
                                                  'showcase_data_MVM' : {'books': sliderHomeBooksMVM},
                                                  'showcase_data_MVY' : {'books': sliderHomeBooksMVY},
                                                  'showcase_data_MVT' : {'books': sliderHomeBooksMVT},
                                                  'showcase_data_MPM' : {'books': sliderHomeBooksMPM},
                                                  'showcase_data_MPY' : {'books': sliderHomeBooksMPY},
                                                  'showcase_data_MPT' : {'books': sliderHomeBooksMPT},
                                                  'showcase_data_MVAM' : {'books': sliderHomeBooksMVAM},
                                                  'showcase_data_MVAY' : {'books': sliderHomeBooksMVAY},
                                                  'showcase_data_MVAT' : {'books': sliderHomeBooksMVAT},
                                                  })
FileGenerate(cfg['outDir'] + cfg['home-showcase-file']).generate(jsShowCase)
# tooltip
jsToolTip = CMPGeneric(env, cfg['jsHomeToolTip']).generate({'tooltip_data_TMK_RDAM' : {'books': tooltipHomeBooksTMK_RDAM},
                                                  'tooltip_data_TMK_RDAY' : {'books': tooltipHomeBooksTMK_RDAY},
                                                  'tooltip_data_TMK_RDAT' : {'books': tooltipHomeBooksTMK_RDAT},
                                                  'tooltip_data_MVM' : {'books': tooltipHomeBooksMVM},
                                                  'tooltip_data_MVY' : {'books': tooltipHomeBooksMVY},
                                                  'tooltip_data_MVT' : {'books': tooltipHomeBooksMVT},
                                                  'tooltip_data_MPM' : {'books': tooltipHomeBooksMPM},
                                                  'tooltip_data_MPY' : {'books': tooltipHomeBooksMPY},
                                                  'tooltip_data_MPT' : {'books': tooltipHomeBooksMPT},
                                                  'tooltip_data_MVAM' : {'books': tooltipHomeBooksMVAM},
                                                  'tooltip_data_MVAY' : {'books': tooltipHomeBooksMVAY},
                                                  'tooltip_data_MVAT' : {'books': tooltipHomeBooksMVAT},
                                                  })
FileGenerate(cfg['outDir'] + cfg['home-tooltip-file']).generate(jsToolTip)   
try:
    # Genero el temporal para los mensajes, arbol y comentarios
    #tree = CMPGeneric(tmpTree).generate()
    
    # Genero los parametros que va a necesitar la generacion del head
    headParams = {'metaTag' : CMPGeneric(env, cfg['cmpMetaTag']).generate({'site_domain': cfg['siteDomain']}),
                  'css' : CMPGeneric(env, cfg['cmpCss']).generate()}
    
    # Genero los componentes que va a necesitar la home
    params = {'head' : CMPGeneric(env, cfg['cmpHead']).generate(headParams),
              'bottom' : CMPGeneric(env, cfg['cmpFooter']).generate(),
              'js_top' : CMPGeneric(env, cfg['cmpJavaScriptTop']).generate(),
              'js_bottom' : CMPGeneric(env, cfg['cmpJavaScriptBottom']).generate(),
              'top' : CMPGeneric(env, cfg['cmpTop']).generate({'search_opts': searchOpts}),
              'messages' : CMPGeneric(env, cfg['cmpMessages']).generate(),
              'extra' : CMPGeneric(env, cfg['cmpExtra']).generate(),
              'showcase' : CMPGeneric(env, cfg['cmpShowCase']).generate({'slider_home_books' : sliderHomeBooksTMK_RDAM,
                                                             'tooltip_home_books' : tooltipHomeBooksTMK_RDAM}),
              'rightmenu' : CMPGeneric(env, cfg['cmpRightMenu']).generate({'menu_data': menuData}),
              'comments' : CMPGeneric(env, cfg['cmpComments']).generate(),
              'lastvisited' : CMPGeneric(env, cfg['cmpLastVisited']).generate()
              }
    #'tree' : CMPGeneric(cmpTree).generate({'tree': tree}),
    # Generacion del HTML de la home
    homeHTML = CMPGeneric(env, cfg['tplHomeSection']).generate(params)
except Exception as e:
    print e

print homeHTML
FileGenerate(cfg['outDir'] + cfg['home-section-file']).generate(homeHTML)