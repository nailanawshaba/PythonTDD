import unittest
from BowlingGame import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def testAllGuttersReturns0(self):
        self.roll_times(0, 20)
        self.assertEquals(0, self.game.score())

    def testAll1sReturns20(self):
        self.roll_times(1, 20)
        self.assertEquals(20, self.game.score())

    def testItHandlesSpares(self):
        self.roll_spare()
        self.game.roll(5)

        self.roll_times(0, 17)
        self.assertEquals(20, self.game.score())

    def testItHandlesStrikes(self):
        self.roll_strike()
        self.game.roll(5)
        self.game.roll(3)

        self.roll_times(0, 17)
        self.assertEquals(26, self.game.score())

    def testPerfectGameIs300(self):
        self.roll_times(10, 12)
        self.assertEquals(300, self.game.score())

    def testDutch200Is200(self):
        for frame in range(10):
            self.roll_strike()
            self.roll_spare()
        self.assertEquals(200, self.game.score())

    def testGutterUntilLastFrameTurkeyIs30(self):
        self.roll_times(0, 18)
        self.roll_strike()
        self.roll_strike()
        self.roll_strike()
        self.assertEquals(30, self.game.score())

    def roll_spare(self):
        self.game.roll(1)
        self.game.roll(9)

    def roll_strike(self):
        self.game.roll(10)

    def roll_times(self, pins_toppled, times):
        for _ in range(times):
            self.game.roll(pins_toppled)


if __name__ == '__main__':
    unittest.main()
