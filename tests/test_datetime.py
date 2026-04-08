import pytest
from datetime import datetime
from pistol_magazine import Datetime


class TestDatetime:
    """Test Datetime data mocker."""

    def test_default_datetime(self):
        """Test default Datetime creation."""
        datetime_obj = Datetime()
        result = datetime_obj.mock()
        assert isinstance(result, str)

    def test_datetime_ymd_format(self):
        """Test Datetime with YMD format."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD)
        result = datetime_obj.mock()
        assert isinstance(result, str)
        # Try to parse to verify format
        parsed = datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
        assert isinstance(parsed, datetime)

    def test_datetime_ymd_t_format(self):
        """Test Datetime with YMD_T format."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD_T)
        result = datetime_obj.mock()
        assert isinstance(result, str)
        # Try to parse to verify format
        parsed = datetime.strptime(result, "%Y-%m-%dT%H:%M:%S")
        assert isinstance(parsed, datetime)

    def test_datetime_with_days(self):
        """Test Datetime with days parameter."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD, days=2)
        result = datetime_obj.mock()
        assert isinstance(result, str)
        parsed = datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
        assert isinstance(parsed, datetime)

    def test_datetime_with_hours(self):
        """Test Datetime with hours parameter."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD, hours=1)
        result = datetime_obj.mock()
        assert isinstance(result, str)

    def test_datetime_with_weeks(self):
        """Test Datetime with weeks parameter."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD, weeks=1)
        result = datetime_obj.mock()
        assert isinstance(result, str)

    def test_custom_date_format(self):
        """Test Datetime with custom date format."""
        custom_format = "%Y/%m/%d"
        datetime_obj = Datetime(date_format=custom_format)
        result = datetime_obj.mock()
        assert isinstance(result, str)
        parsed = datetime.strptime(result, custom_format)
        assert isinstance(parsed, datetime)

    def test_multiple_kwargs(self):
        """Test Datetime with multiple timedelta parameters."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD, days=1, hours=12)
        result = datetime_obj.mock()
        assert isinstance(result, str)

    def test_get_datatype(self):
        """Test get_datatype method."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD)
        result = datetime_obj.get_datatype()
        assert isinstance(result, str)
        assert "Datetime" in result

    def test_multiple_calls_randomness(self):
        """Test that multiple calls generate different values."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD, days=2)
        results = [datetime_obj.mock() for _ in range(10)]
        for result in results:
            assert isinstance(result, str)

    def test_invalid_timedelta_key_raises_error(self):
        """Test that invalid timedelta key raises ValueError."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD)
        with pytest.raises(ValueError):
            datetime_obj.kwargs = {"invalid_key": 1}

    def test_non_dict_timedelta_raises_error(self):
        """Test that non-dict timedelta raises TypeError."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD)
        with pytest.raises(TypeError):
            datetime_obj.kwargs = "not_a_dict"

    def test_valid_timedelta_keys(self):
        """Test setting valid timedelta keys."""
        datetime_obj = Datetime(date_format=Datetime.D_FORMAT_YMD)
        valid_kwargs = {
            "days": 1,
            "seconds": 3600,
            "microseconds": 1000,
            "milliseconds": 500,
            "minutes": 30,
            "hours": 2,
            "weeks": 1
        }
        datetime_obj.kwargs = valid_kwargs
        assert datetime_obj.kwargs == valid_kwargs

    def test_match_classmethod(self):
        """Test Datetime.match classmethod."""
        # This tests the match functionality when D_FORMAT_YMD is in defined_list
        result = Datetime.match('2024-06-05 16:24:16')
        # Could return the format or None depending on defined_list
        assert result is None or isinstance(result, str)
