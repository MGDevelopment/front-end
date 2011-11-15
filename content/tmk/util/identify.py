'''
Created on 14/11/2011

@author: mgoldsman
'''
def getCfgDocBase():
    return './cfg/'

def getSectionUri(idSection):
    sections = {'1': 'books', '3': 'games', '4': 'music', '5': 'movies'}
    return str(sections[idSection])

class TMKId(object):
    '''
    classdocs
    '''
    def __init__(self, idSection=None, idGroup=None, idFamily=None, idSubFamily=None, idArticle=None):
        '''
        Constructor
        '''
        self.idSection = idSection
        self.idGroup = idGroup
        self.idFamily = idFamily
        self.idSubFamily = idSubFamily
        self.idArticle = idArticle
        
    def getCfgFilePath(self):
        if (self.idSection == None):
            return getCfgDocBase() + 'home.yaml'
        if (self.idArticle == None):
            return getCfgDocBase() + 'section' + getSectionUri(self.idSection) + '.yaml'
        else:
            return getCfgDocBase() + 'detail' + getSectionUri(self.idSection) + '.yaml'
    
    def getURL(self):
        url = '/'
        if (self.idSection == None):
            return url
        else:
            url += getSectionUri(self.idSection) + '/'
        if (self.idGroup == None):
            return url
        else:
            url += self.idGroup + '/'
        if (self.idFamily == None):
            return url
        else:
            url += self.idFamily + '/'
        if (self.idSubFamily == None):
            return url
        else:
            url += self.idSubFamily + '/'
        if (self.idArticle == None):
            return url
        else:
            url += self.idArticle + '/'
        return url
    
    def getName(self):
        name = ''
        if (self.idSection == None):
            return 'home'
        else:
            name += getSectionUri(self.idSection)
        if (self.idGroup == None):
            return name
        else:
            name += '_' + self.idGroup
        if (self.idFamily == None):
            return name
        else:
            name += '_' + self.idFamily
        if (self.idSubFamily == None):
            return name
        else:
            name += '_' + self.idSubFamily
        if (self.idArticle == None):
            return name
        else:
            name += '_' + self.idArticle
        return name