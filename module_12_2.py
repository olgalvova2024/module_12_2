import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj1 = runner_and_tournament.Runner('Усэйн', 10)
        self.obj2 = runner_and_tournament.Runner('Андрей', 9)
        self.obj3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for key, value in cls.all_results.items():
            for i, j in value.items():
                result[i] = str(j)
            print(f'{i}: {result}')

    def test_Tournament1(self):
        test = runner_and_tournament.Tournament(90, self.obj1, self.obj3)
        results1 = test.start()
        TournamentTest.all_results[1] = results1
        self.assertTrue(results1.get(len(results1)) == 'Ник')

    def test_Tournament2(self):
        test = runner_and_tournament.Tournament(90, self.obj2, self.obj3)
        results2 = test.start()
        TournamentTest.all_results[2] = results2
        self.assertTrue(results2.get(len(results2)) == 'Ник')

    def test_Tournament3(self):
        test = runner_and_tournament.Tournament(90, self.obj1, self.obj2, self.obj3)
        results3 = test.start()
        TournamentTest.all_results[3] = results3
        self.assertTrue(results3.get(len(results3)) == 'Ник')


if __name__ == '__main__':
    unittest.main()

