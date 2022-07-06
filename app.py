from flask import Flask
from flask_restful import Resource, Api

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import json
import random

file_path = "./phrdase.json"

with open(file_path, 'r', encoding='UTF-8') as file:
    data = json.load(file)

app = Flask(__name__)
api = Api(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5000 per day", "50 per minute"]
)

class KoreanPhrase(Resource):
    def get(self):
        return {"phrase": "%s" %data[str(random.randint(1, len(data)))]}

api.add_resource(KoreanPhrase, '/korean/phrase')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)