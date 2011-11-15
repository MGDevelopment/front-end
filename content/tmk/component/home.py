'''
Created on 12/11/2011

@author: mgoldsman
'''
from tmk.dummy.dummyData import DummyHomeData
from tmk.util.generator import CMPGeneric, FileGenerate
from tmk.util.functions import loadConfiguration, loadEnvironment

class HomeFragment:
    def __init__(self, dataSource=DummyHomeData(), config=None, environment=None):
        '''
        Constructor
        '''
        self.ds = dataSource
        self.id = dataSource.getTMKId()
        if (config != None):
            self.cfg = config
        else:
            self.cfg = loadConfiguration(self.id.getCfgFilePath())
        if (environment != None):
            self.env = environment
        else:
            self.env = loadEnvironment(self.cfg['tplDocBase'])
            
    
    def generateJSComments(self):
        jsComments = CMPGeneric(self.env, self.cfg['tplHomeComments']).generate({'comments_data' : self.ds.getCommentsData(), 'site_domain': self.cfg['siteDomain']})
        FileGenerate(self.cfg['outDir'] + self.id.getURL() + self.cfg['home-comments-file']).generate(jsComments)
        return
    
    def generateJSMessages(self):
        jsMessages = CMPGeneric(self.env, self.cfg['tplHomeMessages']).generate({'messages_data' : self.ds.getMessagesData()})
        FileGenerate(self.cfg['outDir'] + self.id.getURL() + self.cfg['home-messages-file']).generate(jsMessages)
        return
    
    def generateJSShowCase(self):
        jsShowCase= CMPGeneric(self.env, self.cfg['tplHomeShowCase']).generate({'showcase_data' : self.ds.getShowCaseData()})
        FileGenerate(self.cfg['outDir'] + self.id.getURL() + self.cfg['home-showcase-file']).generate(jsShowCase)
        return
    
    def generateJSToolTip(self):
        jsToolTip = CMPGeneric(self.env, self.cfg['tplHomeToolTip']).generate({'tooltip_data' : self.ds.getShowCaseData()})
        FileGenerate(self.cfg['outDir'] + self.id.getURL() + self.cfg['home-tooltip-file']).generate(jsToolTip)
        return
    
    def getMenuData(self):
        menuData = {
            "secciones" : [{"idSeccion" : "seccion4"}, {"idSeccion" : "seccion5"}, {"idSeccion" : "seccion3"}, {"idSeccion" : "seccion200"}, {"idSeccion" : "seccion300"}, {"idSeccion" : "seccion400"}]
            }
        return menuData
    
    def getSearchData(self):
        searchOpts = {
            "options": [
                     {
                        "idOpt" : "optBus1",
                        "txtOpt" : "Todo el Sitio",
                        "idSeccion" : self.cfg['SECCION_HOME'],
                        "seccionBusqueda" : "En Tematika.com",
                        "idSeccionPropia" : self.cfg['SECCION_HOME'],
                        "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(self.cfg['SECCION_HOME'])
                    }, {
                        "idOpt" : "optBus2",
                        "txtOpt" : "En Libros",
                        "idSeccion" : self.cfg['SECCION_LIBRO'],
                        "seccionBusqueda" : "En Libros",
                        "idSeccionPropia" : self.cfg['SECCION_LIBRO'],
                        "urlBus" : "/buscador/productos.jsp?idSeccion=" + str(self.cfg['SECCION_LIBRO'])
                    }
                          ]
            }
        return searchOpts  

    
    def generateHTML(self):
        homeHTML = ''
        try:
            # Genero los JS
            self.generateJSMessages()
            self.generateJSComments()
            self.generateJSShowCase()
            self.generateJSToolTip()
            
            # Genero los parametros que va a necesitar la generacion del head
            headParams = {'metaTag' : CMPGeneric(self.env, self.cfg['cmpMetaTag']).generate({'site_domain': self.cfg['siteDomain']}),
                  'css' : CMPGeneric(self.env, self.cfg['cmpCss']).generate()}
    
            # Genero los componentes que va a necesitar la home
            params = {'head' : CMPGeneric(self.env, self.cfg['cmpHead']).generate(headParams),
              'bottom' : CMPGeneric(self.env, self.cfg['cmpFooter']).generate(),
              'js_top' : CMPGeneric(self.env, self.cfg['cmpJavaScriptTop']).generate(),
              'js_bottom' : CMPGeneric(self.env, self.cfg['cmpJavaScriptBottom']).generate({'jssrc' : self.id.getURL()}),
              'top' : CMPGeneric(self.env, self.cfg['cmpTop']).generate({'search_opts': self.getSearchData()}),
              'messages' : CMPGeneric(self.env, self.cfg['cmpMessages']).generate(),
              'extra' : CMPGeneric(self.env, self.cfg['cmpExtra']).generate(),
              'showcase' : CMPGeneric(self.env, self.cfg['cmpShowCase']).generate({'slider' :self.ds.getShowCaseDataDefault(), 'tooltip' : self.ds.getToolTipDataDefault()}),
              'rightmenu' : CMPGeneric(self.env, self.cfg['cmpRightMenu']).generate({'menu_data': self.getMenuData()}),
              'comments' : CMPGeneric(self.env, self.cfg['cmpComments']).generate(),
              'lastvisited' : CMPGeneric(self.env, self.cfg['cmpLastVisited']).generate()
              }
            homeHTML = CMPGeneric(self.env, self.cfg['tplHome']).generate(params)
            FileGenerate(self.cfg['outDir'] + self.id.getURL() + self.cfg['home-file']).generate(homeHTML)
        except Exception as e:
            print e
        
        return homeHTML  
