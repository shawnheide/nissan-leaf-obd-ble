"""Constants for Nissan Leaf OBD BLE."""

# Base component constants
NAME = "Nissan Leaf OBD BLE"
DOMAIN = "nissan_leaf_obd_ble"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1.0"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/pbutterworth/nissan-leaf-obd-ble/issues"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
# PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]
PLATFORMS = [BINARY_SENSOR, SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
