from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

with open("./loona-data.json") as loona_data:
    loona_members = json.load(loona_data)


class Member(Resource):
    def get(self, id=0):
        if id == 0:
            return loona_members, 200

        for member in loona_members:
            if member["id"] == id:
                return member, 200
        return "Member not found", 404


api.add_resource(Member, "/", "/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
