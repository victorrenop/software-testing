class KataBowling:
    def __init__(self):
        self.match_score = 0

    def roll(self, round_score: int) -> int:
        self.match_score += round_score

    def score(self) -> int:
        return self.match_score