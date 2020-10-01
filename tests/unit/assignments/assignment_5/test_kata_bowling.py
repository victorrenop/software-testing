from assignments.assignment_5.kata_bowling import KataBowling

class TestKataBowling:
    def test_gutter_game(self):
        game = KataBowling()
        for i in range(20):
            game.roll(0)
        assert game.score() == 0
        