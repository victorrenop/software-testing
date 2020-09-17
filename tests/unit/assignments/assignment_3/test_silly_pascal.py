from assignments.assignment_3.silly_pascal import SillyPascal
import pytest


class TestSillyPascal:
    @pytest.mark.parametrize("identifier", [("a12"), ("a"), ("abcde1")])
    def test_valid_identifier(self, identifier):
        assert SillyPascal.is_valid(identifier) is True

    def test_not_starts_with_letter(self):
        assert SillyPascal.is_valid("12") is False

    def test_contains_not_alphanumeric(self):
        assert SillyPascal.is_valid("a12#") is False

    def test_null_string(self):
        assert SillyPascal.is_valid(None) is False

    def test_empty_string(self):
        assert SillyPascal.is_valid("") is False

    def test_string_too_long(self):
        assert SillyPascal.is_valid("abcdef1") is False
