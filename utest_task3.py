# Unit test Velikanov Ivan 181-331

import unittest
import task_3_velikanov

class TestTask_3_Velikanov(unittest.TestCase):

    V = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]

    E = [["V1", "V6"], ["V1", "V8"], ["V2", "V6"], ["V2", "V7"], ["V3", "V4"], ["V3", "V5"], ["V3", "V6"], ["V3", "V8"], ["V4", "V5"], ["V4", "V6"], ["V4", "V8"], ["V7", "V8"]]


    def setUp(self) -> None:
        return super().setUp()

    def test_e_indices(self):
        self.assertEqual(task_3_velikanov.e_indices(self.E, self.V[0]), [0, 1])
        self.assertEqual(task_3_velikanov.e_indices(self.E, self.V[1]), [2, 3])
        self.assertEqual(task_3_velikanov.e_indices(self.E, self.V[2]), [4, 5, 6, 7])
        
    def test_count_ones(self):
        self.assertEqual(task_3_velikanov.count_ones([0, 0, 0, 0, 0, 1, 0, 1]), 0)
        self.assertEqual(task_3_velikanov.count_ones([1, 0, 1, 1, 0, 0, 1, 1]), 1)

    def test_check_ayler(self):
        self.assertEqual(task_3_velikanov.check_ayler(
            [
                [0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1, 0, 1],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 1, 0],
            ], self.V
        ), (True, []))
        
    def test_adjacency_matrix(self):
        self.assertEqual(task_3_velikanov.adjacency_matrix(self.V, self.E), [[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 1, 0]])
    
    def test_additional_ones(self):
        self.assertEqual(task_3_velikanov.additional_ones([
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 1, 0],
        ]
    ,[]), [[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 1, 0]])

    def test_get_path_points(self):
        self.assertEqual(task_3_velikanov.get_path_points(
            [
                [0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1, 0, 1],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 0, 1, 0],
            ], 0
        ), [5, 7])

    def test_ayler_cycle(self):
        self.assertEqual(task_3_velikanov.ayler_cycle(
                    [
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 1, 0],
        ], self.V
        ), ['V1', 'V6', 'V2', 'V7', 'V8', 'V3', 'V4', 'V5'])


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()