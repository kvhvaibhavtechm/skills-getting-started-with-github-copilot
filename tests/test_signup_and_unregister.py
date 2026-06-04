import urllib.parse


def test_signup_success(client):
    # Arrange
    activity = "Science Club"
    email = "tester@example.com"
    path = urllib.parse.quote(activity, safe="")

    # Act
    resp = client.post(f"/activities/{path}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    data = client.get("/activities").json()
    assert email in data[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Science Club"
    email = "dup@example.com"
    path = urllib.parse.quote(activity, safe="")

    # Act - first signup
    r1 = client.post(f"/activities/{path}/signup", params={"email": email})
    # Assert first succeeded
    assert r1.status_code == 200

    # Act - duplicate signup
    r2 = client.post(f"/activities/{path}/signup", params={"email": email})
    # Assert duplicate rejected
    assert r2.status_code == 400


def test_signup_activity_not_found_returns_404(client):
    # Arrange
    activity = "NoSuchActivity"
    email = "x@y.com"
    path = urllib.parse.quote(activity, safe="")

    # Act
    resp = client.post(f"/activities/{path}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404


def test_unregister_success_and_not_found(client):
    # Arrange
    activity = "Science Club"
    existing = "mia@mergington.edu"
    path = urllib.parse.quote(activity, safe="")

    # Act - unregister existing participant
    resp = client.delete(f"/activities/{path}/signup", params={"email": existing})
    # Assert removal succeeded
    assert resp.status_code == 200
    assert existing not in client.get("/activities").json()[activity]["participants"]

    # Act - unregister again (should be not found)
    resp2 = client.delete(f"/activities/{path}/signup", params={"email": existing})
    # Assert 404
    assert resp2.status_code == 404
