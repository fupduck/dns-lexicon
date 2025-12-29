from unittest import TestCase
"""Integration tests for Hetzner"""

from integration_tests import IntegrationTestsV2


class HetznerProviderTests(TestCase, IntegrationTestsV2):
    """TestCase for Hetzner"""
    provider_name = "hetzner"
    domain = "devcoop.de"

    def _filter_headers(self):
        return ["Authorization"]
