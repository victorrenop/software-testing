class KataBowling:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, round_score: int) -> int:
        self.rolls.append(round_score)

    def score(self) -> int:
        score = 0
        for roll in self.rolls:
            score += roll
        return score