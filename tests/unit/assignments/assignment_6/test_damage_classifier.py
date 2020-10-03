from assignments.assignment_6.damage_classifier import RPGDamageClassifier
import pytest

damage_classifier = RPGDamageClassifier()

class TestRPGDamageClassifier:
    def test_first_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(999.99, 'physical') == 999.99
    
    def test_first_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(1000.0, 'physical') == 1245.00

    def test_first_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(999.99, 'magical') == 999.99
    
    def test_first_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(1000.0, 'magical') == 1245.00
