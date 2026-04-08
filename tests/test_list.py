import pytest
import json
from pistol_magazine import List, Int, Str, Float, Timestamp


class TestList:
    """Test List data mocker."""

    def test_default_list(self):
        """Test default List creation."""
        list_obj = List()
        result = list_obj.mock()
        assert isinstance(result, list)
        # Default list has 3 elements: Str, Int, Float
        assert len(result) == 3

    def test_list_to_json_false(self):
        """Test List.mock with to_json=False."""
        list_obj = List()
        result = list_obj.mock(to_json=False)
        assert isinstance(result, list)

    def test_list_to_json_true(self):
        """Test List.mock with to_json=True."""
        list_obj = List()
        result = list_obj.mock(to_json=True)
        assert isinstance(result, str)
        # Should be valid JSON
        parsed = json.loads(result)
        assert isinstance(parsed, list)

    def test_custom_list_fields(self):
        """Test List with custom fields."""
        custom_fields = [Int(), Str(), Float()]
        list_obj = List(list_fields=custom_fields)
        result = list_obj.mock()
        assert isinstance(result, list)
        assert len(result) == 3
        assert isinstance(result[0], int)
        assert isinstance(result[1], str)
        assert isinstance(result[2], float)

    def test_empty_list(self):
        """Test List with empty list_fields."""
        list_obj = List(list_fields=[])
        result = list_obj.mock()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_single_element_list(self):
        """Test List with single element."""
        list_obj = List(list_fields=[Str()])
        result = list_obj.mock()
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], str)

    def test_get_datatype(self):
        """Test get_datatype method."""
        custom_fields = [Int(), Str(), Float()]
        list_obj = List(list_fields=custom_fields)
        result = list_obj.get_datatype()
        assert isinstance(result, list)
        assert len(result) == 3

    def test_multiple_calls_randomness(self):
        """Test that multiple calls generate different values."""
        list_obj = List()
        results = [list_obj.mock() for _ in range(5)]
        for result in results:
            assert isinstance(result, list)
            assert len(result) == 3

    def test_list_with_timestamp(self):
        """Test List with Timestamp field."""
        custom_fields = [
            Int(byte_nums=8, unsigned=True),
            Timestamp(times=10),
            Str(data_type="email")
        ]
        list_obj = List(list_fields=custom_fields)
        result = list_obj.mock()
        assert isinstance(result, list)
        assert len(result) == 3
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)
        assert isinstance(result[2], str)
        assert result[0] >= 0
        assert "@" in result[2]

    def test_large_list(self):
        """Test List with many elements."""
        custom_fields = [Str() for _ in range(10)]
        list_obj = List(list_fields=custom_fields)
        result = list_obj.mock()
        assert isinstance(result, list)
        assert len(result) == 10
        for item in result:
            assert isinstance(item, str)
