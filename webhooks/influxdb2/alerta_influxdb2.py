from typing import Any, Dict
from flask import current_app

from alerta.models.alarms.alerta import SEVERITY_MAP
from alerta.models.alert import Alert

from . import WebhookBase


class InfluxDB2Webhook(WebhookBase):
    def incoming(self, path, query_string, payload):
        notification = payload
        id = notification['_check_id']
        metric = notification['_source_measurement']
        alert_name = notification['_check_name']
        message = notification['_message']
        timestamp = notification['_time']
        group = notification['_notification_rule_name']

        if notification['_level'] == 'crit':
            severity = 'critical'
        elif notification['_level'] == 'warn':
            severity = 'warning'
        elif notification['_level'] == 'info':
            severity = 'ok'

        return Alert(
            resource=alert_name,
            event=alert_name,
            environment='Production',
            severity=severity,
            service=[alert_name],
            group=group,
            value='0',
            text=message,
            tags=['{}:{}'.format("source", "influxdbv2"), '{}:{}'.format("metric", metric)],
            attributes={
                'incidentKey': id
            },
            origin=notification['_notification_rule_id'],
            event_type='influxdbdv2Alarm',
            raw_data=notification
        )
