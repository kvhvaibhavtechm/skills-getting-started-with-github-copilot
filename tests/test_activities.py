def test_get_activities_returns_200(client):
    # Arrange: client fixture provided
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_has_activity_fields(client):
    # Arrange: client fixture provided
    # Act
    resp = client.get("/activities")
    data = resp.json()
    # Assert: each activity has required fields
    for activity_name, activity_info in data.items():
        assert "description" in activity_info
        assert "schedule" in activity_info
        assert "max_participants" in activity_info
        assert "participants" in activity_info
        assert isinstance(activity_info["participants"], list)
