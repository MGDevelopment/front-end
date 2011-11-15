'''
Created on 29/10/2011

@author: mgoldsman
'''
from tmk.util.functions import ensure_dir
 
class CMPGeneric:
    def __init__(self, env, temp):
        self.template = env.get_template(temp)
        
    def generate(self, params=""):
        return self.template.render(params)

class FileGenerate:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def generate(self, content):
        try:   
            ensure_dir(self.fileName)         
            f = open(self.fileName, 'w')
            f.write(content)
            f.close()
        except Exception as e:
            print e
