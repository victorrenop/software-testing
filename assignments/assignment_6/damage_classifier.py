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
        bonus_damage = 0
        if damage >= 1000.0:
            bonus_damage += (min(damage - 1000.00, 999.99))*self.first_multiplier
        if damage >= 3000.0:
            bonus_damage += min(damage - 3000.00, 1999.99)*self.second_multiplier
        if damage >= 5000.0:
            bonus_damage += (damage - 5000.00)*self.third_multiplier
        return float("{:.2f}".format(damage + bonus_damage))

    def _calc_magical_damage(self, damage: float) -> float:
        bonus_damage = 0
        if damage >= 1000.0:
            bonus_damage += min(damage - 1000.0, 999.99)*self.first_multiplier
        if damage >= 5000.0:
            bonus_damage += (damage - 5000.00)*self.third_multiplier
        return float("{:.2f}".format(damage + bonus_damage))