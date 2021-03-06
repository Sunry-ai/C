import unittest
from SE import *

class MapTestCase(unittest.TestCase):
    def setUp(self):
        self.map = Map('The map')

    def test_not_null(self):
        pass
        
    def test_default_size(self):
        self.assertEqual(self.map.size(), (10,10),
                         'incorrect default size')

    def test_map_resize(self):
        self.map.resize([100,150])
        self.assertEqual(self.map.size(), (100,150),
                         'wrong size after resize')
    
    def test_empty(self):
        for line in self.map.elements:
            for elem in line:
                self.assertIsNone(elem.design,'Not empty')
                
    def test_correct_possitions(self):
        for i in range(len(self.map.elements)):
            for j in range(len(self.map.elements[i])):
                self.assertEqual(self.map.elements[i,j].position,[i,j],'Elements out of order')
                
    def test_safe_resize(self):
        #should check that content of the map isn't erased on resize
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MapTestCase('test_default_size'))
    suite.addTest(MapTestCase('test_map_resize'))
    suite.addTest(MapTestCase('test_empty'))
    suite.addTest(MapTestCase('test_correct_possitions'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
