from assignments.assignment_5.kata_bowling import KataBowling

game = KataBowling()

class TestKataBowling:
    def test_gutter_game(self):
        self.roll_many(20, 0, game)
        assert game.score() == 0

    def test_all_ones(self):
        self.roll_many(20, 1, game)
        assert game.score() == 20

    # def test_spare(self):

    def roll_many(self, rolls: int, pins: int, game: KataBowling):
        for i in range(rolls):
            game.roll(pins)
        