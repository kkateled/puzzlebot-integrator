from flask import Flask, request, jsonify
from metadata import AnyMessage

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def add_message():
    content = request.get_json()
    app.logger.info(content)
    message = AnyMessage(**content)
    return jsonify(message.dict())


if __name__ == '__main__':
    app.run(debug=True)
