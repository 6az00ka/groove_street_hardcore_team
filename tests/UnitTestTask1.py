# from asyncio import Task, tasks
import unittest
import numpy as np
import copy
from task1 import fill_array_smejnost_test
from task1 import fill_array_smejnost
class tst(unittest.TestCase):
    array_smj=np.zeros(36, int).reshape(6,6)
    array_smj_check=np.array([[0,1,1,0,1,1],[1,0,1,1,0,1],[1,1,0,1,1,0],[0,1,1,0,1,1],[1,0,1,1,0,1],[1,1,0,1,1,0]])
    
    array_smj_orient=np.zeros(36, int).reshape(6,6)
    array_smj_orient_check=np.array([[0,1,1,0,1,1],[0,0,1,1,0,1],[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],[0,0,0,0,0,0]])
    
    oriented_smj_array=copy.deepcopy(array_smj_orient_check)

    array_inc=np.zeros(72,int).reshape(6,12)
    array_inc_check=np.array([[1,1,1,1,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,1,0,1,1,0],[0,0,1,0,0,0,0,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,1,1]])
    

    def setUp(self) -> None:
        return super().setUp()
 
    def test_array_smejnost_change(self):
        self.assertListEqual(fill_array_smejnost(self.oriented_smj_array,6).tolist(),self.array_smj_check.tolist())
        print('Array smejnost done')
        #DONE!!!!!!!

    def test_array_smejnost_oriented_change(self):
        self.assertListEqual(fill_array_smejnost_test(self.array_smj).tolist(),self.array_smj_orient_check.tolist())
        print('Oriented array smejnost done')
        #DONE!!!!!!!
    

    

        
if __name__ == "__main__":
  unittest.main()