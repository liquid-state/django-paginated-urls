#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-paginated-urls
------------

Tests for `django-paginated-urls` models module.
"""

from django.test import TestCase
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

from paginated_urls.utils import add_page_to_url
from django.contrib.auth.models import User

class TestPaginated_urls(TestCase):

    def setUp(self):
        self.request = MagicMock()
        self.request.user.is_authenticated = MagicMock(return_value=True)
        self.request.session = dict()

        self.viewname = 'homepage'
        self.url = '/'

    def test_unauthenticated_user_returns_passed_url(self):
        self.request.user.is_authenticated = MagicMock(return_value=False)
        result = add_page_to_url(self.request, self.viewname, self.url)
        self.assertEqual(result, self.url)