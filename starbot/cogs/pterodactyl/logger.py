from red_commons import logging
from red_commons.logging import getLogger

logger = getLogger('red.SeaCogs.Pterodactyl')
websocket_logger = getLogger('red.SeaCogs.Pterodactyl.websocket')
if logger.level >= logging.VERBOSE:
    websocket_logger.setLevel(logging.logging.INFO)
elif logger.level < logging.VERBOSE:
    websocket_logger.setLevel(logging.logging.DEBUG)
