import pytest
import json
from pistol_magazine import Dict, Int, Str, Float, Timestamp


class TestDict:
    """Test Dict data mocker."""

    def test_default_dict(self):
        """Test default Dict creation."""
        dict_obj = Dict()
        result = dict_obj.mock()
        assert isinstance(result, dict)
        assert "a" in result
        assert "b" in result
        assert "c" in result

    def test_custom_dict_fields(self):
        """Test Dict with custom fields."""
        custom_fields = {
            "name": Str(data_type="name"),
            "age": Int(byte_nums=8, unsigned=True),
            "score": Float(left=1, right=2, unsigned=True)
        }
        dict_obj = Dict(dict_fields=custom_fields)
        result = dict_obj.mock()
        assert isinstance(result, dict)
        assert "name" in result
        assert "age" in result
        assert "score" in result
        assert isinstance(result["name"], str)
        assert isinstance(result["age"], int)
        assert isinstance(result["score"], float)

    def test_dict_to_json_false(self):
        """Test Dict.mock with to_json=False."""
        dict_obj = Dict()
        result = dict_obj.mock(to_json=False)
        assert isinstance(result, dict)

    def test_dict_to_json_true(self):
        """Test Dict.mock with to_json=True."""
        dict_obj = Dict()
        result = dict_obj.mock(to_json=True)
        assert isinstance(result, str)
        # Should be valid JSON
        parsed = json.loads(result)
        assert isinstance(parsed, dict)

    def test_get_datatype(self):
        """Test get_datatype method."""
        custom_fields = {
            "int_field": Int(),
            "str_field": Str(),
            "float_field": Float()
        }
        dict_obj = Dict(dict_fields=custom_fields)
        result = dict_obj.get_datatype()
        assert isinstance(result, dict)
        assert "int_field" in result
        assert "str_field" in result
        assert "float_field" in result

    def test_empty_dict_fields(self):
        """Test Dict with empty dict_fields."""
        dict_obj = Dict(dict_fields={})
        result = dict_obj.mock()
        assert isinstance(result, dict)
        assert len(result) == 0

    def test_nested_dict(self):
        """Test Dict with nested structures."""
        from pistol_magazine import List

        custom_fields = {
            "simple": Int(),
            "nested": List([Str(), Float()])
        }
        dict_obj = Dict(dict_fields=custom_fields)
        result = dict_obj.mock()
        assert isinstance(result, dict)
        assert isinstance(result["simple"], int)
        assert isinstance(result["nested"], list)

    def test_multiple_calls_randomness(self):
        """Test that multiple calls generate different values."""
        dict_obj = Dict()
        results = [dict_obj.mock() for _ in range(5)]
        for result in results:
            assert isinstance(result, dict)

    def test_dict_with_timestamp(self):
        """Test Dict with Timestamp field."""
        custom_fields = {
            "id": Int(byte_nums=8, unsigned=True),
            "created_at": Timestamp(times=10)
        }
        dict_obj = Dict(dict_fields=custom_fields)
        result = dict_obj.mock()
        assert isinstance(result, dict)
        assert isinstance(result["id"], int)
        assert isinstance(result["created_at"], int)
        assert result["id"] >= 0
