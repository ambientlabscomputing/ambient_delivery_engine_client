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

from delivery_engine_client.models.validation_error_loc_inner import ValidationErrorLocInner

class TestValidationErrorLocInner(unittest.TestCase):
    """ValidationErrorLocInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationErrorLocInner:
        """Test ValidationErrorLocInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationErrorLocInner`
        """
        model = ValidationErrorLocInner()
        if include_optional:
            return ValidationErrorLocInner(
            )
        else:
            return ValidationErrorLocInner(
        )
        """

    def testValidationErrorLocInner(self):
        """Test ValidationErrorLocInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()