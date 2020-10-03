class RPGDamageClassifier:
    def __init__(self):
        self.first_multiplier = 0.245
        self.second_multiplier = 0.4
        self.third_multiplier = 0.15

    def damage_dealt(self, damage: float, damage_type: str) -> float:
        return 0.0