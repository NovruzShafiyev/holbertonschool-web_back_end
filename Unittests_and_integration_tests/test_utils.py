#!/usr/bin/env python3

"""
Module with utility functions.
"""

from typing import Any, Dict, List, Union
from parameterized import parameterized
import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any) -> None:
        """
        Test access_nested_map function with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()
