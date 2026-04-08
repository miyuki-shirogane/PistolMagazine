import pytest
from pistol_magazine import Int, Int8, Int16, Int32, UInt, UInt8, UInt16, UInt32


class TestInt:
    """Test Int data mocker."""

    def test_default_int(self):
        """Test default Int creation (64-bit signed)."""
        int_obj = Int()
        result = int_obj.mock()
        assert isinstance(result, int)

    def test_int8_range(self):
        """Test Int8 range (-128 to 127)."""
        int8_obj = Int8()
        for _ in range(100):
            result = int8_obj.mock()
            assert isinstance(result, int)
            assert -128 <= result <= 127

    def test_int16_range(self):
        """Test Int16 range (-32768 to 32767)."""
        int16_obj = Int16()
        for _ in range(100):
            result = int16_obj.mock()
            assert isinstance(result, int)
            assert -32768 <= result <= 32767

    def test_int32_range(self):
        """Test Int32 range."""
        int32_obj = Int32()
        result = int32_obj.mock()
        assert isinstance(result, int)
        # Int32: -2^31 to 2^31 - 1
        assert -2147483648 <= result <= 2147483647

    def test_uint8_range(self):
        """Test UInt8 range (0 to 255)."""
        uint8_obj = UInt8()
        for _ in range(100):
            result = uint8_obj.mock()
            assert isinstance(result, int)
            assert 0 <= result <= 255

    def test_uint16_range(self):
        """Test UInt16 range (0 to 65535)."""
        uint16_obj = UInt16()
        for _ in range(100):
            result = uint16_obj.mock()
            assert isinstance(result, int)
            assert 0 <= result <= 65535

    def test_uint32_range(self):
        """Test UInt32 range."""
        uint32_obj = UInt32()
        result = uint32_obj.mock()
        assert isinstance(result, int)
        # UInt32: 0 to 2^32 - 1
        assert 0 <= result <= 4294967295

    def test_custom_byte_nums_signed(self):
        """Test custom byte_nums with signed=False."""
        # 4 bits signed: -8 to 7
        int_obj = Int(byte_nums=4, unsigned=False)
        for _ in range(100):
            result = int_obj.mock()
            assert isinstance(result, int)
            assert -8 <= result <= 7

    def test_custom_byte_nums_unsigned(self):
        """Test custom byte_nums with unsigned=True."""
        # 4 bits unsigned: 0 to 15
        int_obj = Int(byte_nums=4, unsigned=True)
        for _ in range(100):
            result = int_obj.mock()
            assert isinstance(result, int)
            assert 0 <= result <= 15

    def test_multiple_calls_randomness(self):
        """Test that multiple calls generate different values."""
        int_obj = Int()
        results = [int_obj.mock() for _ in range(20)]
        # Check all are integers
        for result in results:
            assert isinstance(result, int)

    def test_uint_default(self):
        """Test default UInt (64-bit unsigned)."""
        uint_obj = UInt()
        result = uint_obj.mock()
        assert isinstance(result, int)
        assert result >= 0

    def test_int_args_attribute(self):
        """Test that args attribute is correctly set."""
        int_obj = Int(byte_nums=8, unsigned=False)
        assert int_obj.args == [-128, 127]

        uint_obj = Int(byte_nums=8, unsigned=True)
        assert uint_obj.args == [0, 255]

    def test_large_byte_nums(self):
        """Test with large byte_nums values."""
        int_obj = Int(byte_nums=16)
        result = int_obj.mock()
        assert isinstance(result, int)
