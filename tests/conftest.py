import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Snapshot initial activities once
_INITIAL_ACTIVITIES = copy.deepcopy(activities)

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: restore initial state before each test
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
    yield
    # Cleanup: ensure consistent state after test
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
