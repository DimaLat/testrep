from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27018,
                         username='root',
                         password='pass',
                         authSource="admin")
    db = client["test_db"]
    return db


@app.route('/')
def index():
    return "Info"


@app.route('/test')
def get_test():
    db = get_db()
    _tests = db.tets_tb.find()
    tests = [{"id": test["id"], "name": test["name"], "type": test["type"]} for test in _tests]
    return jsonify({"tests": tests})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
