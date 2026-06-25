import pytest

from src.app import activities, get_activity


def test_get_activity_returns_valid_activity():
    activity = get_activity("Chess Club")

    assert activity["description"] == "Learn strategies and compete in chess tournaments"
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert activity["max_participants"] == 12
    assert isinstance(activity["participants"], list)


def test_get_activity_raises_for_missing_activity():
    with pytest.raises(ValueError, match="Activity not found"):
        get_activity("Nonexistent Club")
