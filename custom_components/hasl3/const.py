""" SL Platform Constants """
from enum import IntEnum

from homeassistant.const import CONF_NAME, STATE_OFF, STATE_ON

HASL_VERSION = "3.1.1"
SCHEMA_VERSION = "4"
DOMAIN = "hasl3"
NAME = "Swedish Public Transport Sensor (HASL)"

DEVICE_NAME = "HASL API Communications Device"
DEVICE_MANUFACTURER = "hasl.sorlov.com"
DEVICE_MODEL = "Software device"
DEVICE_GUID = (
    "10ba5386-5fad-49c6-8f03-c7a047cd5aa5-6a618956-520c-41d2-9a10-6d7e7353c7f5"
)
SL_TRAFIK_DEVICE_GUID = "feb117a9-c5cb-4f0c-b08e-331d5c081bfc"
SL_TRAFIK_DEVICE_NAME = "SL Traffic"

SENSOR_RRDEP = "Resrobot Departures"
SENSOR_RRARR = "Resrobot Arrivals"
SENSOR_RRROUTE = "Resrobot Route Sensor"
SENSOR_STATUS = "status_v2"
SENSOR_VEHICLE_LOCATION = "SL Vehicle Locations"
SENSOR_ROUTE = "SL Route Sensor"
SENSOR_DEPARTURE = "departure_v2"

CONF_RP3_KEY = "rp3key"
CONF_RR_KEY = "rrkey"

CONF_SITE_ID = "siteid"
CONF_SITE_IDS = "siteids"
CONF_DEBUG = "debug"
CONF_FP_PT = "fppt"
CONF_FP_RB = "fprb"
CONF_FP_TVB = "fptvb"
CONF_FP_SB = "fpsb"
CONF_FP_LB = "fplb"
CONF_FP_SPVC = "fpspvc"
CONF_FP_TB1 = "fptb1"
CONF_FP_TB2 = "fptb2"
CONF_FP_TB3 = "fptb3"
CONF_SENSOR = "sensor"
CONF_SENSOR_PROPERTY = "property"
CONF_LINE = "line"
CONF_LINES = "lines"
CONF_TRANSPORT = "transport"
CONF_TRANSPORTS = "transports"
CONF_TRIPS = "trips"
CONF_ENABLED = "enabled"
CONF_DIRECTION = "direction"
CONF_DIRECTION_ANY = 0
CONF_DIRECTION_LEFT = 1
CONF_DIRECTION_RIGHT = 2
CONF_TIMEWINDOW = "timewindow"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_SENSOR_PROPERTY_MIN = "min"
CONF_SENSOR_PROPERTY_TIME = "time"
CONF_SENSOR_PROPERTY_DEVIATIONS = "deviations"
CONF_SENSOR_PROPERTY_UPDATED = "updated"
CONF_SENSOR_PROPERTY_ORIGIN = "origin"
CONF_INTEGRATION_TYPE = "type"
CONF_INTEGRATION_ID = "id"
CONF_SOURCE = "from"
CONF_DESTINATION = "to"
CONF_SOURCE_ID = "fromid"
CONF_DESTINATION_ID = "toid"

CONF_METRO = "metro"
CONF_TRAIN = "train"
CONF_LOCAL = "local"
CONF_TRAM = "tram"
CONF_BUS = "bus"
CONF_FERRY = "ferry"

CONF_DIRECTION_LIST = [CONF_DIRECTION_ANY, CONF_DIRECTION_LEFT, CONF_DIRECTION_RIGHT]
CONF_DEPARTURE_SENSOR_PROPERTY_LIST = [
    CONF_SENSOR_PROPERTY_MIN,
    CONF_SENSOR_PROPERTY_TIME,
    CONF_SENSOR_PROPERTY_UPDATED,
]
CONF_SENSOR_PROPERTY_LIST = [
    CONF_SENSOR_PROPERTY_MIN,
    CONF_SENSOR_PROPERTY_TIME,
    CONF_SENSOR_PROPERTY_DEVIATIONS,
    CONF_SENSOR_PROPERTY_UPDATED,
]
CONF_INTEGRATION_LIST = [
    SENSOR_DEPARTURE,
    SENSOR_STATUS,
    SENSOR_RRDEP,
    SENSOR_RRARR,
    SENSOR_RRROUTE,
    SENSOR_VEHICLE_LOCATION,
    SENSOR_ROUTE,
]
CONF_RRARR_PROPERTY_LIST = [
    CONF_SENSOR_PROPERTY_MIN,
    CONF_SENSOR_PROPERTY_TIME,
    CONF_SENSOR_PROPERTY_UPDATED,
    CONF_SENSOR_PROPERTY_ORIGIN,
]
CONF_RRDEP_PROPERTY_LIST = [
    CONF_SENSOR_PROPERTY_MIN,
    CONF_SENSOR_PROPERTY_TIME,
    CONF_SENSOR_PROPERTY_UPDATED,
]

DEFAULT_DIRECTION = CONF_DIRECTION_ANY
DEFAULT_SENSOR_PROPERTY = CONF_SENSOR_PROPERTY_MIN
DEFAULT_INTEGRATION_TYPE = SENSOR_RRDEP
DEFAULT_SCAN_INTERVAL = 300
DEFAULT_TIMEWINDOW = 6


class DirectionType(IntEnum):
    """Direction type."""

    ANY = 0
    LEFT = 1
    RIGHT = 2
