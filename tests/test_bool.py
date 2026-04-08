import pytest
from pistol_magazine import Bool


class TestBool:
    """Test Bool data mocker."""

    def test_bool_returns_bool(self):
        """Test that Bool.mock returns a boolean."""
        bool_obj = Bool()
        result = bool_obj.mock()
        assert isinstance(result, bool)

    def test_bool_multiple_calls(self):
        """Test that multiple calls generate booleans."""
        bool_obj = Bool()
        results = [bool_obj.mock() for _ in range(20)]
        for result in results:
            assert isinstance(result, bool)
            assert result in [True, False]

    def test_bool_can_be_true(self):
        """Test that Bool can generate True."""
        bool_obj = Bool()
        results = [bool_obj.mock() for _ in range(100)]
        assert True in results  # At least one True in 100 attempts

    def test_bool_can_be_false(self):
        """Test that Bool can generate False."""
        bool_obj = Bool()
        results = [bool_obj.mock() for _ in range(100)]
        assert False in results  # At least one False in 100 attempts


class TestBoolMatch:
    """Test Bool.match classmethod."""

    @pytest.mark.parametrize("test_input,expected", [
        (True, True),
        (False, True),
        (1, False),
        (0, False),
        ("?", False),
        ("True", False),
        ("", False),
        (None, False)
    ], ids=["bool_true", "bool_false", "int_1", "int_0", "str_qmark", "str_true", "str_empty", "none"])
    def test_match_classmethod(self, test_input, expected):
        """Test Bool.match classmethod."""
        assert Bool().match(test_input) is expected
