from assignments.assignment_5.kata_bowling import KataBowling

game = KataBowling()

class TestKataBowling:
    def test_gutter_game(self):
        for i in range(20):
            game.roll(0)
        assert game.score() == 0

    def test_all_ones(self):
        for i in range(20):
            game.roll(1)
        assert game.score() == 20
        