"""Tests for refoss_rpc utils."""

from unittest.mock import Mock

import pytest

from homeassistant.components.refoss_rpc.utils import (
    get_device_uptime,
    get_host,
    get_input_triggers,
    get_refoss_channel_name,
)
from homeassistant.util import dt as dt_util


@pytest.mark.freeze_time("2024-01-10 18:43:00+00:00")
async def test_get_device_uptime() -> None:
    """Test block test get device uptime."""
    assert get_device_uptime(
        55, dt_util.as_utc(dt_util.parse_datetime("2024-01-10 18:42:00+00:00"))
    ) == dt_util.as_utc(dt_util.parse_datetime("2024-01-10 18:42:00+00:00"))

    assert get_device_uptime(
        50, dt_util.as_utc(dt_util.parse_datetime("2024-01-10 18:42:00+00:00"))
    ) == dt_util.as_utc(dt_util.parse_datetime("2024-01-10 18:42:10+00:00"))


async def test_get_rpc_channel_name(mock_rpc_device) -> None:
    """Test get RPC channel name."""
    assert get_refoss_channel_name(mock_rpc_device, "input:1") == "test input"


@pytest.mark.parametrize(
    ("component", "expected"),
    [
        ("input", "Input"),
        ("switch", "Switch"),
    ],
)
async def test_get_rpc_channel_name_multiple_components(
    mock_rpc_device: Mock,
    monkeypatch: pytest.MonkeyPatch,
    component: str,
    expected: str,
) -> None:
    """Test get RPC channel name when there is more components of the same type."""
    config = {
        f"{component}:1": {"name": None},
    }
    monkeypatch.setattr(mock_rpc_device, "config", config)
    assert (
        get_refoss_channel_name(mock_rpc_device, f"{component}:1")
        == f"Test name {expected} 1"
    )


async def test_get_rpc_input_triggers(
    mock_rpc_device: Mock, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test get RPC input triggers."""
    monkeypatch.setattr(mock_rpc_device, "config", {"input:1": {"type": "button"}})
    assert set(get_input_triggers(mock_rpc_device)) == {
        ("btn_down", "button1"),
        ("btn_up", "button1"),
        ("single_push", "button1"),
        ("double_push", "button1"),
        ("triple_push", "button1"),
        ("long_push", "button1"),
    }

    monkeypatch.setattr(mock_rpc_device, "config", {"input:1": {"type": "switch"}})
    assert not get_input_triggers(mock_rpc_device)


@pytest.mark.parametrize(
    ("host", "expected"),
    [
        ("10.10.10.12", "10.10.10.12"),
        (
            "1010:1010:1010:1010:1010:1010:1010:1010",
            "[1010:1010:1010:1010:1010:1010:1010:1010]",
        ),
    ],
)
def test_get_host(host: str, expected: str) -> None:
    """Test get_host function."""
    assert get_host(host) == expected
