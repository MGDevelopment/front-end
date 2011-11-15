'''
Created on 12/11/2011

@author: mgoldsman
'''

from tmk.component.detail import DetailFragment
from tmk.component.home import HomeFragment
from tmk.component.section import SectionFragment
import shutil
import unittest


class Test(unittest.TestCase):
        
    def testCreateOUT(self): 
        try:
            shutil.rmtree('../../out', True)
        except Exception as e:
            print e
        try:
            shutil.copytree('./content/', '../../out', False, None)
        except Exception as e:
            print e     
        pass
    
    def testDetail(self):    
        detail = DetailFragment()
        
        self.assertNotEqual(detail.generateHTML(), '', 'testDetail - Error on generateHTML')
        pass

    def testSection(self):
        section = SectionFragment()
        
        self.assertNotEqual(section.generateHTML(), '', 'testSection - Error on generateHTML')
        pass
    
    def testHome(self):     
        home = HomeFragment()
        
        self.assertNotEqual(home.generateHTML(), '', 'testHome - Error on generateHTML')
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSection']
    unittest.main()