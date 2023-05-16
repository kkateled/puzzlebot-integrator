from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def add_message():
    content = request.get_json()
    app.logger.info(content)
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True)
