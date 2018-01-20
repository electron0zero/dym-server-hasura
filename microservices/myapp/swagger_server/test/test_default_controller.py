# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_dym_get(self):
        """
        Test case for dym_get

        does spell correction and word segmentation on payload.
        """
        query_string = [('payload', 'payload_example'),
                        ('spell', true),
                        ('segment', true)]
        response = self.client.open('/v1/dym',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_dym_post(self):
        """
        Test case for dym_post

        does spell correction and word segmentation on payload.
        """
        data = dict(payload='payload_example',
                    spell=true,
                    segment=true)
        response = self.client.open('/v1/dym',
                                    method='POST',
                                    data=data,
                                    content_type='application/x-www-form-urlencoded')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
