import os.path
from flask import request, jsonify
from flask_api import FlaskAPI
import csv
from utils.metadata import AnyMessage
from models.sql_any_message import any_message_table, engine
from utils.converters import to_model

app = FlaskAPI(__name__)


@app.route('/post', methods=['POST'])
def add_message():
    content = request.get_json()
    if content['type_subscribe_event'] == 'any_message':
        app.logger.info(content)
        try:
            message = AnyMessage(**content)
            dict_message = message.dict(exclude_none=True)
            converter_model = to_model(message)
            writer_db(any_message_table, converter_model)
            writer_csv('any_message.csv', converter_model)
            response = jsonify(dict_message)
            return response
        except BaseException as error:
            app.logger.error(error)
            return "Internal exception", 500
    else:
        app.logger.warning("Incorrect input message")
        return "Internal exception", 400


def writer_csv(file_name, message: dict):
    if os.path.exists(file_name):
        with open(file_name, "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(message.values())
    else:
        with open(file_name, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(message.keys())
        writer_csv(file_name, message)


def writer_db(table, message):
    with engine.connect() as connection:
        insertion_query = table.insert().values(**message)
        connection.execute(insertion_query)
        connection.commit()


if __name__ == '__main__':
    app.run(debug=True)
