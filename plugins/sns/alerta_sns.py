
import boto3
import logging
import os

try:
    from alerta.plugins import app  # alerta >= 5.0
except ImportError:
    from alerta.app import app  # alerta < 5.0
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.sns')

DEFAULT_AWS_REGION = 'eu-west-1'

AWS_REGION = os.environ.get('AWS_REGION') or app.config.get(
    'AWS_REGION', DEFAULT_AWS_REGION)
AWS_SNS_TOPIC_ARN = os.environ.get('AWS_SNS_TOPIC_ARN') or app.config.get(
    'AWS_SNS_TOPIC_ARN', "")


class SnsTopicPublisher(PluginBase):

    def __init__(self, name=None):

        self.client = boto3.client('sns')

        super(SnsTopicPublisher, self).__init__(name)

        LOG.info('Configured SNS publisher on topic "%s"', AWS_SNS_TOPIC_ARN)

    def pre_receive(self, alert):
        return alert

    def post_receive(self, alert):

        LOG.info('Sending message %s to SNS topic "%s"',
                 alert.get_id(), AWS_SNS_TOPIC_ARN)
        LOG.debug('Message: %s', alert.raw_data)

        response = self.client.publish(
            TopicArn=AWS_SNS_TOPIC_ARN, message=alert.raw_data)
        LOG.debug('Response: %s', response)

    def status_change(self, alert, status, text):
        return
