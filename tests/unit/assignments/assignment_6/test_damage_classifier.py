from assignments.assignment_6.damage_classifier import RPGDamageClassifier
import pytest

damage_classifier = RPGDamageClassifier()

class TestRPGDamageClassifier:
    def test_first_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(1000.00, 'physical') == 1000.00
    
    def test_first_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(2999.99, 'physical') == 1244.99

    def test_first_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(1000.00, 'magical') == 1000.00
    
    def test_first_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(2000.0, 'magical') == 1244.99

    def test_second_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, 'physical') == 4644.99

    def test_second_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(4999.99, 'physical') == 6044.97

    def test_second_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, 'magical') == 4244.99

    def test_second_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(4999.99, 'magical') == 5244.98
        