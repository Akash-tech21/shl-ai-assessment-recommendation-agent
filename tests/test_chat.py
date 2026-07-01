from tests.conftest import client


def test_chat():

    response = client.post(
        "/chat",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Recommend Python assessments"
                }
            ]
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "reply" in body
    assert "recommendations" in body
    assert "end_of_conversation" in body