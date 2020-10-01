class KataBowling:
    def __init__(self):
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, round_score: int):
        self.rolls[self.current_roll] = round_score
        self.current_roll += 1

    def score(self) -> int:
        score = 0
        frame_index = 0
        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_spare(self, idx):
        if self.rolls[idx] + self.rolls[idx + 1] == 10:
            return True
        return False

    def _is_strike(self, idx):
        if self.rolls[idx] == 10:
            return True
        return False