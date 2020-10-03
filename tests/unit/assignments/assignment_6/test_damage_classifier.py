from assignments.assignment_6.damage_classifier import RPGDamageClassifier

damage_classifier = RPGDamageClassifier()


class TestRPGDamageClassifier:
    def test_first_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(2000.0, "physical") == 2245.00

    def test_first_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(2000.00, "magical") == 2245.00

    def test_second_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, "physical") == 4890.0

    def test_second_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, "magical") == 4490.0

    def test_third_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(6000.0, "physical") == 7439.99

    def test_third_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(6000.0, "magical") == 6640.0
