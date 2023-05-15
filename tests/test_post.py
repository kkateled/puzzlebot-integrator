from post import app


def test_post_route():
    with app.test_client() as client:
        response = client.post('/post', json={
            "date": "01.02.2023"
        })
        json_response = response.get_json()
        assert json_response == {"date": "01.02.2023"}
        assert response.status_code == 200
