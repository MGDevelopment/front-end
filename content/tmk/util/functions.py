'''
Created on 09/11/2011

@author: mgoldsman
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
import os
import yaml
        
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        try:
            os.makedirs(d)
        except Exception as e:
            print e
    return f

def loadConfiguration(cfgFilePath):
    return yaml.load(open(cfgFilePath))

def loadEnvironment(docBase):
    return Environment(loader=FileSystemLoader(docBase))

