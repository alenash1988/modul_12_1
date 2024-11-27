import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        name = runner.Runner('Кристина')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name_1 = runner.Runner('Кира')
        for i in range(10):
            name_1.run()
        self.assertEqual(name_1.distance, 100)

    def test_challenge(self):
        name_2 = runner.Runner('Татьяна')
        name_3 = runner.Runner('Лиза')
        for i in range(10):
            name_2.walk()
            name_3.run()
        self.assertNotEqual(name_2.distance, name_3.distance)


if __name__ == "__main__":
    unittest.main()




