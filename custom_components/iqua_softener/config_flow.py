import logging
from typing import Any, Dict, Optional

from homeassistant import config_entries, core
import voluptuous as vol

from .const import DOMAIN, CONF_USERNAME, CONF_PASSWORD, CONF_DEVICE_SERIAL_NUMBER

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA_USER = vol.Schema(
    {
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
        vol.Required(CONF_DEVICE_SERIAL_NUMBER): str,
    }
)


class IquaSoftenerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        errors: Dict[str, str] = {}
        if user_input is not None:
            self.data = user_input
            return self.async_create_entry(
                title=f"iQua {self.data[CONF_DEVICE_SERIAL_NUMBER]}", data=self.data
            )

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA_USER)
