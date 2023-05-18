from post import app

test_case = {
    "date": 1684327767.923629,
    "bot": {
        "id": "3490",
        "username": "IAmBot",
        "first_name": "MyNameIsBot"},
    "chat": {
        "id": "001",
        "type": "channel",
        "first_name": "SuperNews",
        "title": "super_news",
        "username": "super_news",
        "member_count": 3000},
    "user": {
        "id": "1010101",
        "first_name": "Kate",
        "last_name": "Solovev",
        "username": "kate_solv",
        "is_bot": False,
        "category_name": "NoBot"},
    "message": "News subscription",
    "type_subscribe_event": "any_message",
    "name": "News"}

expected_test_result = {
    "date": '2023-05-17T15:49:27.923629',
    "bot": {
        "id": "3490",
        "username": "IAmBot",
        "first_name": "MyNameIsBot"},
    "chat": {
        "id": "001",
        "type": "channel",
        "first_name": "SuperNews",
        "title": "super_news",
        "username": "super_news",
        "member_count": 3000},
    "user": {
        "id": "1010101",
        "first_name": "Kate",
        "last_name": "Solovev",
        "username": "kate_solv",
        "is_bot": False,
        "category_name": "NoBot"},
    "message": "News subscription",
    "type_subscribe_event": "any_message",
    "name": "News"}


def test_post_route():
    with app.test_client() as client:
        response = client.post('/post', json=test_case)
        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == expected_test_result


def test_date_format():
    with app.test_client() as client:
        response = client.post('/post', json=test_case)
        date_json_response = response.get_json()['date']
        assert response.status_code == 200
        assert date_json_response == '2023-05-17T15:49:27.923629'
