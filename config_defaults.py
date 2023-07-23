#!/usr/bin/env python
import logging

# Default configuration.
# Do not edit this.  Copy config_sample.py to config.py and edit that.

# Logging
LOGGING_LEVEL_CONSOLE = logging.INFO
LOGGING_LEVEL_FILE = logging.ERROR
LOGGING_FILE = None  # or set to file path LOGGING_FILE="/var/log/paradox_mqtt.log"

# MQTT
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_CLIENT_ID = "tuya_mqtt"

# Homie Standard Items
# https://homieiot.github.io/specification/spec-core-v4_0_0/
HOMIE_BASE_TOPIC = "homie"
HOMIE_DEVICE_VERSION = "4.0.0"
HOMIE_DEVICE_EXTENSIONS = ""
HOMIE_INIT_SECONDS = 3600 * 24  # Daily
HOMIE_MQTT_QOS = 1
HOMIE_MQTT_RETAIN = True
HOMIE_PUBLISH_ALL_SECONDS = 60
HOMIE_IMPLEMENTATION = "tuya_mqtt"

# tinytuya
DEVICE_FILE = "devices.json"
DEVICE_RECONNECT_SECONDS = 15

# Threads
DEVICE_THREAD_START_GAP_SECONDS = 5
