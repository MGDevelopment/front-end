'''
Created on 01/10/2011
Proceso de generacion de la HOME de Tematika.

@author: mgoldsman
'''

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from generatorClass import CMPGeneric, FileGenerate
import yaml


stream = open('./cfg/home.yaml')
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

# slider
jinjaSlider = CMPGeneric(env, cfg['tmpSlider'])
# slider TMK_RDA
sliderHomeBooksTMK_RDAM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
sliderHomeMusicTMK_RDAM = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAM})
sliderHomeMoviesTMK_RDAM = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAM})
sliderHomeGamesTMK_RDAM = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAM})
sliderHomeBooksTMK_RDAY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
sliderHomeMusicTMK_RDAY = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAY})
sliderHomeMoviesTMK_RDAY = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAY})
sliderHomeGamesTMK_RDAY = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAY})
sliderHomeBooksTMK_RDAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMusicTMK_RDAT = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMoviesTMK_RDAT = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
sliderHomeGamesTMK_RDAT = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
sliderHomeBooksTMK_RDAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMusicTMK_RDAT = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
sliderHomeMoviesTMK_RDAT = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
sliderHomeGamesTMK_RDAT = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
# slider MV
sliderHomeBooksMVM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVM})
sliderHomeMusicMVM = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVM})
sliderHomeMoviesMVM = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVM})
sliderHomeGamesMVM = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVM})
sliderHomeBooksMVY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVY})
sliderHomeMusicMVY = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVY})
sliderHomeMoviesMVY = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVY})
sliderHomeGamesMVY = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVY})
sliderHomeBooksMVT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVT})
sliderHomeMusicMVT = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVT})
sliderHomeMoviesMVT = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVT})
sliderHomeGamesMVT = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVT})
# slider MP
sliderHomeBooksMPM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPM})
sliderHomeMusicMPM = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMPM})
sliderHomeMoviesMPM = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMPM})
sliderHomeGamesMPM = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMPM})
sliderHomeBooksMPY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPY})
sliderHomeMusicMPY = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMPY})
sliderHomeMoviesMPY = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMPY})
sliderHomeGamesMPY = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMPY})
sliderHomeBooksMPT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMPT})
sliderHomeMusicMPT = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMPT})
sliderHomeMoviesMPT = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMPT})
sliderHomeGamesMPT = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMPT})
# slider MVA
sliderHomeBooksMVAM = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
sliderHomeMusicMVAM = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVAM})
sliderHomeMoviesMVAM = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVAM})
sliderHomeGamesMVAM = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVAM})
sliderHomeBooksMVAY = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
sliderHomeMusicMVAY = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVAY})
sliderHomeMoviesMVAY = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVAY})
sliderHomeGamesMVAY = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVAY})
sliderHomeBooksMVAT = jinjaSlider.generate({'prefix': 'books', 'slider_data': sliderDataMVAT})
sliderHomeMusicMVAT = jinjaSlider.generate({'prefix': 'music', 'slider_data': sliderDataMVAT})
sliderHomeMoviesMVAT = jinjaSlider.generate({'prefix': 'movies', 'slider_data': sliderDataMVAT})
sliderHomeGamesMVAT = jinjaSlider.generate({'prefix': 'games', 'slider_data': sliderDataMVAT})

# tooltip
jinjaToolTip = CMPGeneric(env, cfg['tmpToolTip'])
# tooltip TMK_RDA
tooltipHomeBooksTMK_RDAM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeMusicTMK_RDAM = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeMoviesTMK_RDAM = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeGamesTMK_RDAM = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAM})
tooltipHomeBooksTMK_RDAY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeMusicTMK_RDAY = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeMoviesTMK_RDAY = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeGamesTMK_RDAY = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAY})
tooltipHomeBooksTMK_RDAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMusicTMK_RDAT = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMoviesTMK_RDAT = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeGamesTMK_RDAT = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeBooksTMK_RDAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMusicTMK_RDAT = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeMoviesTMK_RDAT = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataTMK_RDAT})
tooltipHomeGamesTMK_RDAT = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataTMK_RDAT})
# tooltip MV
tooltipHomeBooksMVM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVM})
tooltipHomeMusicMVM = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVM})
tooltipHomeMoviesMVM = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVM})
tooltipHomeGamesMVM = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVM})
tooltipHomeBooksMVY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVY})
tooltipHomeMusicMVY = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVY})
tooltipHomeMoviesMVY = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVY})
tooltipHomeGamesMVY = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVY})
tooltipHomeBooksMVT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVT})
tooltipHomeMusicMVT = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVT})
tooltipHomeMoviesMVT = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVT})
tooltipHomeGamesMVT = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVT})
# tooltip MP
tooltipHomeBooksMPM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPM})
tooltipHomeMusicMPM = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMPM})
tooltipHomeMoviesMPM = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMPM})
tooltipHomeGamesMPM = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMPM})
tooltipHomeBooksMPY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPY})
tooltipHomeMusicMPY = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMPY})
tooltipHomeMoviesMPY = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMPY})
tooltipHomeGamesMPY = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMPY})
tooltipHomeBooksMPT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMPT})
tooltipHomeMusicMPT = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMPT})
tooltipHomeMoviesMPT = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMPT})
tooltipHomeGamesMPT = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMPT})
# tooltip MVA
tooltipHomeBooksMVAM = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAM})
tooltipHomeMusicMVAM = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVAM})
tooltipHomeMoviesMVAM = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVAM})
tooltipHomeGamesMVAM = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVAM})
tooltipHomeBooksMVAY = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAY})
tooltipHomeMusicMVAY = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVAY})
tooltipHomeMoviesMVAY = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVAY})
tooltipHomeGamesMVAY = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVAY})
tooltipHomeBooksMVAT = jinjaToolTip.generate({'prefix': 'books', 'slider_data': sliderDataMVAT})
tooltipHomeMusicMVAT = jinjaToolTip.generate({'prefix': 'music', 'slider_data': sliderDataMVAT})
tooltipHomeMoviesMVAT = jinjaToolTip.generate({'prefix': 'movies', 'slider_data': sliderDataMVAT})
tooltipHomeGamesMVAT = jinjaToolTip.generate({'prefix': 'games', 'slider_data': sliderDataMVAT})

# Genero los JS
# comments
comments = CMPGeneric(env, cfg['tmpComments']).generate({'comments_data' : commentsData, 'site_domain': cfg['siteDomain']})
jsComments = CMPGeneric(env, cfg['jsHomeComments']).generate({'comments_data_last' : comments, 'comments_data_books' : comments, 'comments_data_music' : comments, 'comments_data_movies' : comments})
FileGenerate(cfg['outDir'] + cfg['home-comments-file']).generate(jsComments)    
# messages
jsMessages = CMPGeneric(env, cfg['jsHomeMessages']).generate({'messages_data' : messageData})
FileGenerate(cfg['outDir'] + cfg['home-messages-file']).generate(jsMessages)
# showcase
jsShowCase = CMPGeneric(env, cfg['jsHomeShowCase']).generate({'showcase_data_TMK_RDAM' : {'books': sliderHomeBooksTMK_RDAM, 'music' : sliderHomeMusicTMK_RDAM, 'movies' : sliderHomeMoviesTMK_RDAM, 'games' : sliderHomeGamesTMK_RDAM},
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
FileGenerate(cfg['outDir'] + cfg['home-showcase-file']).generate(jsShowCase)
# tooltip
jsToolTip = CMPGeneric(env, cfg['jsHomeToolTip']).generate({'tooltip_data_TMK_RDAM' : {'books': tooltipHomeBooksTMK_RDAM, 'music' : tooltipHomeMusicTMK_RDAM, 'movies' : tooltipHomeMoviesTMK_RDAM, 'games' : tooltipHomeGamesTMK_RDAM},
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
FileGenerate(cfg['outDir'] + cfg['home-tooltip-file']).generate(jsToolTip)  
# Genero la Home
homeHTML = ""
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
              'showcase' : CMPGeneric(env, cfg['cmpShowCase']).generate({'slider_home_books' : sliderHomeBooksTMK_RDAM, 'slider_home_music': sliderHomeMusicTMK_RDAM, 'slider_home_movies' : sliderHomeMoviesTMK_RDAM, 'slider_home_games' : sliderHomeGamesTMK_RDAM,
                                                             'tooltip_home_books' : tooltipHomeBooksTMK_RDAM, 'tooltip_home_music': tooltipHomeMusicTMK_RDAM, 'tooltip_home_movies' : tooltipHomeMoviesTMK_RDAM, 'tooltip_home_games' : tooltipHomeGamesTMK_RDAM}),
              'rightmenu' : CMPGeneric(env, cfg['cmpRightMenu']).generate({'menu_data': menuData}),
              'comments' : CMPGeneric(env, cfg['cmpComments']).generate(),
              'lastvisited' : CMPGeneric(env, cfg['cmpLastVisited']).generate()
              }
    #'tree' : CMPGeneric(cmpTree).generate({'tree': tree}),
    # Generacion del HTML de la home
    homeHTML = CMPGeneric(env, cfg['tplHome']).generate(params)
except Exception as e:
    print e
# Imprime el codigo HTML producido
print homeHTML
# Genera el archivo de salida
FileGenerate(cfg['outDir'] + cfg['home-file']).generate(homeHTML)