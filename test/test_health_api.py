# coding: utf-8

"""
    delivery_engine API

     This is the delivery_engine API. It is a FastAPI application that provides a RESTful API. 

    The version of the OpenAPI document: 0.1.0
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from delivery_engine_client.api.health_api import HealthApi


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthApi()

    def tearDown(self) -> None:
        pass

    def test_health_check_health_get(self) -> None:
        """Test case for health_check_health_get

        Health Check
        """


if __name__ == '__main__':
    unittest.main()
