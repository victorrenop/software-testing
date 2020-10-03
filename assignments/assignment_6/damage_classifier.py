class RPGDamageClassifier:
    def __init__(self):
        self.first_multiplier = 0.245
        self.second_multiplier = 0.4
        self.third_multiplier = 0.15

    def damage_dealt(self, damage: float, damage_type: str) -> float:
        total_damage_dealt = 0
        if damage_type == 'physical':
            total_damage_dealt = self._calc_physical_damage(damage)
        elif damage_type == 'magical':
            total_damage_dealt = self._calc_magical_damage(damage)
        return total_damage_dealt
    
    def _calc_physical_damage(self, damage: float) -> float:
        total_damage_dealt = damage
        if damage >= 1000.0 and damage <= 3000.0:
            total_damage_dealt += total_damage_dealt*self.first_multiplier
        return float("{:.2f}".format(total_damage_dealt))

    def _calc_magical_damage(self, damage: float) -> float:
        total_damage_dealt = damage
        if damage >= 1000.0 and damage <= 3000.0:
            total_damage_dealt += total_damage_dealt*self.first_multiplier
        return float("{:.2f}".format(total_damage_dealt))