from flask import Flask
from flask_restful import Resource, Api

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import json
import random

file_path = "./phrase.json"

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
        num = random.randint(1, (len(data)/2)-1)
        return {"phrase": "%s" %data["phrase%d" %num], 
                "writer": "%s" %data["writer%d" %num]}

api.add_resource(KoreanPhrase, '/korean/phrase')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
