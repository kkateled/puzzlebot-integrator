import csv
import logging

import pytest

from api.main import app
import sqlite3
from fastapi.testclient import TestClient

client = TestClient(app)

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
    "chat_title": "super_news",
    "chat_username": "super_news",
    "user_id": "1010101",
    "user_username": "kate_solv",
    "message": "News subscription"}

expected_names_columns = ['date', 'message', 'type_subscribe_event', 'name', 'chat_id', 'chat_type', 'chat_first_name',
                          'chat_title', 'chat_username', 'chat_member_count', 'user_id', 'user_first_name',
                          'user_last_name', 'user_username', 'user_is_bot', 'user_category_name']
expected_values_lines = ['2023-05-17T15:49:27.923629', 'News subscription', 'any_message', 'News', '001', 'channel',
                         'SuperNews', 'super_news', 'super_news', '3000', '1010101', 'Kate', 'Solovev', 'kate_solv',
                         'False', 'NoBot']


def must_successful_test_post():
    response = client.post('/api/v1/any_message', json=test_case)
    json_response = response.json()
    logging.info(json_response)
    assert response.status_code == 200
    assert json_response == expected_test_result


@pytest.mark.skip
def test_date_format():
    with app.test_client() as client:
        response = client.post('/post', json=test_case)
        date_json_response = response.get_json()['date']
        assert response.status_code == 200
        assert date_json_response == '2023-05-17T15:49:27.923629'


@pytest.mark.skip
def test_csv():
    with app.test_client() as client:
        response = client.post('/post', json=test_case)
        with open("any_message.csv") as csvfile:
            reader = csv.reader(csvfile)
            csv_result = [row for row in reader]
            csv_names_columns = csv_result[0]
            csv_values_lines = csv_result[1]
        assert response.status_code == 200
        assert sorted(csv_names_columns) == sorted(expected_names_columns)
        assert sorted(csv_values_lines) == sorted(expected_values_lines)


@pytest.mark.skip
def test_db():
    with app.test_client() as client:
        response = client.post('/post', json=test_case)
        connect_db = sqlite3.connect('any_message.db')
        cursor = connect_db.cursor()
        cursor.execute("SELECT * FROM any_message")
        result_db = list(cursor.fetchall()[0])
        for i, x in enumerate(result_db):
            if x == 0:
                result_db[i] = 'False'
            elif x == 1:
                result_db[i] = 'True'
            elif isinstance(x, int):
                result_db[i] = str(x)
        connect_db.close()
        assert response.status_code == 200
        assert sorted(result_db) == sorted(expected_values_lines)
