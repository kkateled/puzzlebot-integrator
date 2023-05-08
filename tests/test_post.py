from post import app


def test_home_route():
    with app.test_client() as c:
        response = c.post('/post', json={
            "date": "01.02.2023"
        })
        json_response = response.get_json()
        assert json_response == {"date": "01.02.2023"}
        assert response.status_code == 200
        print()

