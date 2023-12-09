import json

import pytest

from hello_world import app


@pytest.fixture()
def test_event():
    return {
        "message": "Test Event"
    }


def test_lambda_handler(test_event):

    ret = app.lambda_handler(test_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "Test Event"
