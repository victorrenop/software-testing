from assignments.assignment_5.kata_bowling import KataBowling

class TestKataBowling:
    def test_gutter_game(self):
        game = KataBowling()
        self.roll_many(20, 0, game)
        assert game.score() == 0

    def test_all_ones(self):
        game = KataBowling()
        self.roll_many(20, 1, game)
        assert game.score() == 20

    def test_spare(self):
        game = KataBowling()
        game.roll(5)
        game.roll(5)
        game.roll(3)
        assert game.score() == 16

    def roll_many(self, rolls: int, pins: int, game: KataBowling):
        for i in range(rolls):
            game.roll(pins)
        