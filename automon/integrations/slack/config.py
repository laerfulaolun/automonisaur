import os
import slack

from automon.logger import Logging

log = Logging('config')


class ConfigSlack:
    slack_webhook = os.getenv('SLACK_WEBHOOK')
    slack_proxy = os.getenv('SLACK_PROXY')
    slack_token = os.getenv('SLACK_TOKEN')

    if not slack_token:
        log.debug(f'SLACK_TOKEN not set')

    def __init__(self, slack_name='Automon Slack bot'):
        self.slack = slack
        self.slack_name = slack_name
        self.slack_webhook = os.getenv('SLACK_WEBHOOK')
        self.slack_proxy = os.getenv('SLACK_PROXY')
        self.slack_token = os.getenv('SLACK_TOKEN')