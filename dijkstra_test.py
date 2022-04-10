import unittest
import dijkstra

class TestDijkstra(unittest.TestCase):
    
    answerPath3 = ['v1', 'v9', 'v3', 'v4']
    answerWeight3 = 10
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_run(self):
        self.assertEqual(dijkstra.run(3),(self.answerWeight3, self.answerPath3))
    
if __name__ == "__main__":
    unittest.main()