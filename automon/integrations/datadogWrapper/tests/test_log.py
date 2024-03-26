import asyncio
import unittest

from automon.integrations.datadogWrapper import DatadogClientRest
from automon.integrations.openTelemetryWrapper import OpenTelemetryClient


class MyTestCase(unittest.TestCase):
    client = DatadogClientRest()
    client_tracer = OpenTelemetryClient()

    def test_log(self):
        if asyncio.run(self.client.is_ready()):

            asyncio.run(self.client_tracer.config.test())

            spans = asyncio.run(self.client_tracer.to_datadog())
            for span in spans:
                asyncio.run(
                    self.client.log(
                        ddsource=span['datadog']['ddsource'],
                        ddtags=span['datadog']['ddtags'],
                        hostname=span['datadog']['hostname'],
                        service=span['datadog']['service'],
                        message=span['datadog']['message'],
                    ))

            pass

    if __name__ == '__main__':
        unittest.main()
