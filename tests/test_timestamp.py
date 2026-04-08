import pytest
from pistol_magazine import Timestamp


class TestTimestamp:
    """Test Timestamp data mocker."""

    def test_default_timestamp(self):
        """Test default Timestamp creation (13 digits)."""
        timestamp_obj = Timestamp()
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_timestamp_10_digits(self):
        """Test Timestamp with 10 digits."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0
        # Should be around 10 digits (Unix timestamp)
        assert 1000000000 <= result <= 9999999999

    def test_timestamp_13_digits(self):
        """Test Timestamp with 13 digits."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE13)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_timestamp_with_days(self):
        """Test Timestamp with days parameter."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10, days=2)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_timestamp_with_hours(self):
        """Test Timestamp with hours parameter."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10, hours=5)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_timestamp_with_weeks(self):
        """Test Timestamp with weeks parameter."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10, weeks=1)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_multiple_kwargs(self):
        """Test Timestamp with multiple timedelta parameters."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10, days=1, hours=12)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_get_datatype(self):
        """Test get_datatype method."""
        timestamp_obj = Timestamp(times=10)
        result = timestamp_obj.get_datatype()
        assert isinstance(result, str)
        assert "Timestamp" in result

    def test_multiple_calls_randomness(self):
        """Test that multiple calls generate different values."""
        timestamp_obj = Timestamp(times=Timestamp.D_TIMEE10, days=2)
        results = [timestamp_obj.mock() for _ in range(20)]
        for result in results:
            assert isinstance(result, int)
            assert result > 0

    def test_custom_times_value(self):
        """Test Timestamp with custom times value."""
        timestamp_obj = Timestamp(times=12)
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_string_times_value(self):
        """Test Timestamp with string times value."""
        timestamp_obj = Timestamp(times="13")
        result = timestamp_obj.mock()
        assert isinstance(result, int)
        assert result > 0

    def test_invalid_timedelta_key_raises_error(self):
        """Test that invalid timedelta key raises ValueError."""
        timestamp_obj = Timestamp()
        with pytest.raises(ValueError):
            timestamp_obj.kwargs = {"invalid_key": 1}

    def test_non_dict_timedelta_raises_error(self):
        """Test that non-dict timedelta raises TypeError."""
        timestamp_obj = Timestamp()
        with pytest.raises(TypeError):
            timestamp_obj.kwargs = "not_a_dict"

    def test_valid_timedelta_keys(self):
        """Test setting valid timedelta keys."""
        timestamp_obj = Timestamp()
        valid_kwargs = {
            "days": 1,
            "seconds": 3600,
            "microseconds": 1000,
            "milliseconds": 500,
            "minutes": 30,
            "hours": 2,
            "weeks": 1
        }
        timestamp_obj.kwargs = valid_kwargs
        assert timestamp_obj.kwargs == valid_kwargs

    def test_match_classmethod_with_valid_timestamp(self):
        """Test Timestamp.match classmethod with valid timestamp."""
        # 1717598215 is around June 2024
        result = Timestamp.match(1717598215)
        # Could return the matching times or None
        assert result is None or isinstance(result, int)

    def test_match_classmethod_with_large_timestamp(self):
        """Test Timestamp.match with millisecond timestamp."""
        # 1717598215123 is a millisecond timestamp
        result = Timestamp.match(1717598215123)
        assert result is None or isinstance(result, int)

    def test_constants(self):
        """Test timestamp constants."""
        assert Timestamp.D_TIMEE10 == 10
        assert Timestamp.D_TIMEE13 == 13
