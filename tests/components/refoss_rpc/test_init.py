"""Test cases for the refoss_rpc component."""

from unittest.mock import Mock

from homeassistant.config_entries import ConfigEntryState
from homeassistant.const import STATE_ON, STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant

from . import set_integration


async def test_entry_unload(
    hass: HomeAssistant,
    mock_rpc_device: Mock,
) -> None:
    """Test entry unload."""
    entity_id = "switch.test_switch"
    entry = await set_integration(hass)

    assert entry.state is ConfigEntryState.LOADED
    assert hass.states.get(entity_id).state is STATE_ON

    await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.state is ConfigEntryState.NOT_LOADED
    assert hass.states.get(entity_id).state is STATE_UNAVAILABLE
