from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_endpoint_returns_activities():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_endpoint_adds_participant():
    email = "testuser@mergington.edu"
    response = client.post("/activities/Chess%20Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"


def test_signup_endpoint_rejects_duplicate_signup():
    email = "daniel@mergington.edu"
    response = client.post("/activities/Chess%20Club/signup", params={"email": email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_remove_participant_endpoint():
    email = "sophia@mergington.edu"
    response = client.delete("/activities/Programming%20Class/participants", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Programming Class"


def test_remove_participant_not_found():
    email = "missing@mergington.edu"
    response = client.delete("/activities/Programming%20Class/participants", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
