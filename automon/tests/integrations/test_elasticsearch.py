import unittest

from automon.integrations.elasticsearch.config import ElasticsearchConfig, SnapshotBot, JVMBot
from automon.integrations.elasticsearch.cleanup import Cleanup


class ElasticsearchTest(unittest.TestCase):

    def test_ElasticsearchConnect(self):
        self.assertFalse(
            Cleanup(
                'elasticsearch.0000000', use_ssl=False, request_timeout=1).elasticsearch.ping())

    def test_ElasticsearchConfig(self):
        self.assertTrue(ElasticsearchConfig())

    def test_SnapshotBot(self):
        self.assertTrue(SnapshotBot())

    def test_JVMBot(self):
        self.assertTrue(JVMBot())

    def test_ElasticsearchConnect(self):
        self.assertTrue(Cleanup())

# if __name__ == '__main__':
#     unittest.main()
