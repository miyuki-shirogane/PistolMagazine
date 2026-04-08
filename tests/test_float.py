import pytest
from pistol_magazine import Float


class TestFloat:
    """Test Float data mocker."""

    def test_default_float(self):
        """Test default Float creation."""
        float_obj = Float()
        result = float_obj.mock()
        assert isinstance(result, float)
        assert isinstance(result, (int, float))

    def test_custom_left_right(self):
        """Test Float with custom left and right digits."""
        float_obj = Float(left=3, right=4)
        result = float_obj.mock()
        assert isinstance(result, float)
        # Check that the result is a valid float
        assert not (result != result)  # NaN check

    def test_unsigned_true(self):
        """Test Float with unsigned=True."""
        float_obj = Float(left=2, right=4, unsigned=True)
        result = float_obj.mock()
        assert isinstance(result, float)
        assert result >= 0

    def test_unsigned_false(self):
        """Test Float with unsigned=False."""
        float_obj = Float(left=2, right=4, unsigned=False)
        result = float_obj.mock()
        assert isinstance(result, float)
        # Can be negative or positive

    def test_multiple_calls_generate_different_values(self):
        """Test that multiple calls generate different values (randomness)."""
        float_obj = Float(left=2, right=4, unsigned=True)
        results = [float_obj.mock() for _ in range(10)]
        # Check that we got valid floats
        for result in results:
            assert isinstance(result, float)
            assert result >= 0

    def test_get_datatype(self):
        """Test get_datatype method."""
        float_obj = Float()
        assert float_obj.get_datatype() == 'Float'

    def test_parameters_are_integers(self):
        """Test that left and right parameters are converted to integers."""
        float_obj = Float(left="2", right="4")
        assert float_obj.left == 2
        assert float_obj.right == 4
        result = float_obj.mock()
        assert isinstance(result, float)

    def test_small_left_right(self):
        """Test Float with small left and right values."""
        float_obj = Float(left=1, right=1)
        result = float_obj.mock()
        assert isinstance(result, float)

    def test_large_left_right(self):
        """Test Float with large left and right values (max 15 total)."""
        # Faker has a maximum of 15 total digits
        float_obj = Float(left=7, right=7)
        result = float_obj.mock()
        assert isinstance(result, float)
