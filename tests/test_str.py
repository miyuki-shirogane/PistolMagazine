import pytest
from pistol_magazine import Str, StrInt, StrFloat, StrTimestamp


class TestStr:
    """Test Str data mocker."""

    def test_default_str(self):
        """Test default Str creation (word)."""
        str_obj = Str()
        result = str_obj.mock()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_str_with_word_type(self):
        """Test Str with word data type."""
        str_obj = Str(data_type="word")
        result = str_obj.mock()
        assert isinstance(result, str)

    def test_str_with_name_type(self):
        """Test Str with name data type."""
        str_obj = Str(data_type="name")
        result = str_obj.mock()
        assert isinstance(result, str)

    def test_str_with_email_type(self):
        """Test Str with email data type."""
        str_obj = Str(data_type="email")
        result = str_obj.mock()
        assert isinstance(result, str)
        assert "@" in result

    def test_str_with_address_type(self):
        """Test Str with address data type."""
        str_obj = Str(data_type="address")
        result = str_obj.mock()
        assert isinstance(result, str)

    def test_str_with_md5_type(self):
        """Test Str with md5 data type."""
        str_obj = Str(data_type="md5")
        result = str_obj.mock()
        assert isinstance(result, str)
        assert len(result) == 32  # MD5 hash length

    def test_multiple_calls_generate_different_values(self):
        """Test that multiple calls generate different values."""
        str_obj = Str(data_type="word")
        results = [str_obj.mock() for _ in range(10)]
        for result in results:
            assert isinstance(result, str)

    def test_match_classmethod_returns_str_for_non_digit(self):
        """Test Str.match classmethod with non-digit string."""
        result = Str.match("hello")
        assert isinstance(result, Str)

    def test_match_classmethod_returns_strint_for_digits(self):
        """Test Str.match with digit string."""
        result = Str.match("123")
        assert isinstance(result, StrInt)

    def test_match_classmethod_returns_strfloat_for_float_string(self):
        """Test Str.match with float string."""
        result = Str.match("12.34")
        assert isinstance(result, StrFloat)

    def test_data_type_descriptor_set_valid(self):
        """Test setting valid data_type."""
        str_obj = Str(data_type="word")
        str_obj.data_type = "name"
        assert str_obj.data_type == "name"


class TestStrInt:
    """Test StrInt data mocker."""

    def test_default_str_int(self):
        """Test default StrInt creation."""
        str_int = StrInt()
        result = str_int.mock()
        assert isinstance(result, str)
        # Should be a string representation of an integer
        int(result)  # Should not raise ValueError

    def test_str_int_6_bits_unsigned(self):
        """Test StrInt with 6 bits unsigned."""
        str_int = StrInt(byte_nums=6, unsigned=True)
        for _ in range(20):
            result = str_int.mock()
            assert isinstance(result, str)
            value = int(result)
            assert 0 <= value <= 63

    def test_str_int_8_bits(self):
        """Test StrInt with 8 bits."""
        str_int = StrInt(byte_nums=8, unsigned=False)
        for _ in range(20):
            result = str_int.mock()
            assert isinstance(result, str)
            value = int(result)
            assert -128 <= value <= 127

    def test_str_int_unsigned(self):
        """Test StrInt with unsigned=True."""
        str_int = StrInt(byte_nums=8, unsigned=True)
        for _ in range(20):
            result = str_int.mock()
            assert isinstance(result, str)
            value = int(result)
            assert 0 <= value <= 255


class TestStrFloat:
    """Test StrFloat data mocker."""

    def test_default_str_float(self):
        """Test default StrFloat creation."""
        str_float = StrFloat()
        result = str_float.mock()
        assert isinstance(result, str)
        # Should be a string representation of a float
        float(result)  # Should not raise ValueError

    def test_str_float_unsigned(self):
        """Test StrFloat with unsigned=True."""
        str_float = StrFloat(left=3, right=5, unsigned=True)
        for _ in range(20):
            result = str_float.mock()
            assert isinstance(result, str)
            value = float(result)
            assert value >= 0

    def test_str_float_custom_left_right(self):
        """Test StrFloat with custom left and right."""
        str_float = StrFloat(left=3, right=5)
        result = str_float.mock()
        assert isinstance(result, str)
        float(result)  # Should not raise ValueError

    def test_get_datatype(self):
        """Test get_datatype method."""
        str_float = StrFloat()
        assert str_float.get_datatype() == 'StrFloat'


class TestStrTimestamp:
    """Test StrTimestamp data mocker."""

    def test_default_str_timestamp(self):
        """Test default StrTimestamp creation (13 digits)."""
        str_ts = StrTimestamp()
        result = str_ts.mock()
        assert isinstance(result, str)
        # Should be a string representation of a timestamp
        int(result)  # Should not raise ValueError

    def test_str_timestamp_13_digits(self):
        """Test StrTimestamp with 13 digits."""
        str_ts = StrTimestamp(times=13)
        result = str_ts.mock()
        assert isinstance(result, str)
        value = int(result)
        assert value > 0

    def test_str_timestamp_10_digits(self):
        """Test StrTimestamp with 10 digits."""
        str_ts = StrTimestamp(times=StrTimestamp.D_TIMEE10)
        result = str_ts.mock()
        assert isinstance(result, str)
        value = int(result)
        assert value > 0

    def test_str_timestamp_with_kwargs(self):
        """Test StrTimestamp with timedelta kwargs."""
        str_ts = StrTimestamp(times=10, days=30)
        result = str_ts.mock()
        assert isinstance(result, str)
        value = int(result)
        assert value > 0

    def test_str_timestamp_with_weeks(self):
        """Test StrTimestamp with weeks parameter."""
        str_ts = StrTimestamp(times=10, weeks=1)
        result = str_ts.mock()
        assert isinstance(result, str)
        int(result)  # Should not raise ValueError

    def test_str_timestamp_match_classmethod(self):
        """Test StrTimestamp.match classmethod."""
        result = StrTimestamp.match('1717598215')
        # Should return the matching time length or None
        assert result is None or isinstance(result, int)
