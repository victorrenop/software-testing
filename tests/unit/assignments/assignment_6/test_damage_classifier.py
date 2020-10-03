from assignments.assignment_6.damage_classifier import RPGDamageClassifier

damage_classifier = RPGDamageClassifier()


class TestRPGDamageClassifier:
    def test_first_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(1000.00, "physical") == 1000.00

    def test_first_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(2999.99, "physical") == 3244.99

    def test_first_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(1000.00, "magical") == 1000.00

    def test_first_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(2999.99, "magical") == 3244.99

    def test_second_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, "physical") == 4645.00

    def test_second_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(4999.99, "physical") == 6044.98

    def test_second_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(4000.0, "magical") == 4245.0

    def test_second_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(4999.99, "magical") == 5244.99

    def test_third_physical_damage_range_1(self):
        assert damage_classifier.damage_dealt(5000.01, "physical") == 6045.01

    def test_third_physical_damage_range_2(self):
        assert damage_classifier.damage_dealt(6000.0, "physical") == 7194.99

    def test_third_magical_damage_range_1(self):
        assert damage_classifier.damage_dealt(5000.01, "magical") == 5245.01

    def test_third_magical_damage_range_2(self):
        assert damage_classifier.damage_dealt(6000.0, "magical") == 6395.0
