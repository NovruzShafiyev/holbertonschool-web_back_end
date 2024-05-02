#!/usr/bin/env python3

"""
Module with tests for GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method of GithubOrgClient class.
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        expected_result = {"key": "value"}  # Adjust expected result as per your implementation
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == "__main__":
    unittest.main()
