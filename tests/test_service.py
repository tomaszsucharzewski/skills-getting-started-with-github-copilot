import pytest

from src.app import activities, signup_activity, remove_participant


def test_signup_activity_adds_participant():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activity = signup_activity(activity_name, email)

    assert email in activity["participants"]
    assert activities[activity_name]["participants"][-1] == email


def test_signup_activity_rejects_duplicate():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    with pytest.raises(ValueError, match="Student already signed up"):
        signup_activity(activity_name, email)


def test_remove_participant_removes_existing_email():
    activity_name = "Programming Class"
    email = "emma@mergington.edu"

    activity = remove_participant(activity_name, email)

    assert email not in activity["participants"]
    assert email not in activities[activity_name]["participants"]


def test_remove_participant_rejects_missing_email():
    activity_name = "Programming Class"
    email = "unknown@mergington.edu"

    with pytest.raises(ValueError, match="Participant not found"):
        remove_participant(activity_name, email)
