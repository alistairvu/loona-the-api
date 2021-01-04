from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

with open("./loona-data.json") as loona_data:
    loona_members = json.load(loona_data)


class Members(Resource):
    @app.route("/", methods=["GET"])
    def getAll():
        return jsonify(loona_members), 200

    @app.route("/<int:id>", methods=["GET"])
    def getOne(id):
        for member in loona_members:
            if member["id"] == id:
                return jsonify(member), 200
        return "Member not found", 404


if __name__ == '__main__':
    app.run(debug=True)
