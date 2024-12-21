"""Different constants for this cog"""

from typing import Any, Dict

_config_structure: Dict[str, Dict[str, Any]] = {
    "global": {
        "blacklist": {},
        "whitelist": {},
        "schema_v1": 1,
        "log_channel": None,
    },
    "guild": {
        "blacklist": {},
        "whitelist": {},
    },
}

