'''
Created on 26/08/2013

@author: Santi
'''
import unittest
from Program import *


class Test(unittest.TestCase):
    
    def setUp(self):
        self.miPrograma=program()
        self.miPrograma.addIns("Santi");
        self.miPrograma.addIns("Phyton");
        self.miPrograma.addIns("TPI");

    def testWhenCount_thenSuccess(self):
        numIns=self.miPrograma.countIns();
        self.assertEqual(numIns,3);


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()