"""Constants for the Refoss RPC integration."""

from __future__ import annotations

from logging import Logger, getLogger
from typing import Final

DOMAIN: Final = "refoss_rpc"

LOGGER: Logger = getLogger(__package__)


# Refresh interval for polling
REFOSS_SENSORS_POLLING_INTERVAL: Final = 60

# Reconnect interval for  devices
REFOSS_RECONNECT_INTERVAL = 60


# Button Click events for devices
EVENT_REFOSS_CLICK: Final = "refoss.click"

ATTR_CLICK_TYPE: Final = "click_type"
ATTR_CHANNEL: Final = "channel"
ATTR_DEVICE: Final = "device"
CONF_SUBTYPE: Final = "subtype"

INPUTS_EVENTS_TYPES: Final = {
    "btn_down",
    "btn_up",
    "single_push",
    "double_push",
    "triple_push",
    "long_push",
}

INPUTS_EVENTS_SUBTYPES: Final = {
    "button1": 1,
}

UPTIME_DEVIATION: Final = 5

# Time to wait before reloading entry when device config change
ENTRY_RELOAD_COOLDOWN = 60


OTA_BEGIN = "ota_begin"
OTA_ERROR = "ota_error"
OTA_PROGRESS = "OTA_PROGRESS"
OTA_SUCCESS = "ota_success"
