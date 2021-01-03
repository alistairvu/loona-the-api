from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

loona_members = [
    {
        "id": 1,
        "name": "Heejin",
        "fullName": "Jeon Heejin",
        "birth": "001019",
        "solo": "ViViD",
        "subunit": "1/3",
        "colour": "bright pink",
        "animal": "rabbit",
        "colourHex": "#ed008e",
    },
    {
        "id": 2,
        "name": "Hyunjin",
        "fullName": "Kim Hyunjin",
        "birth": "001115",
        "solo": "Around You",
        "subunit": "1/3",
        "colour": "yellow",
        "animal": "cat",
        "colourHex": "#ffca14",
    },
    {
        "id": 3,
        "name": "Haseul",
        "fullName": "Jo Haseul",
        "birth": "970818",
        "solo": "Let Me In",
        "subunit": "1/3",
        "colour": "green",
        "animal": "white bird",
        "colourHex": "#03a233",
    },
    {
        "id": 4,
        "name": "Yeojin",
        "fullName": "Im Yeojin",
        "birth": "021111",
        "solo": "Kiss Later",
        "subunit": "N/A",
        "colour": "orange",
        "animal": "frog",
        "colourHex": "#fe9702",
    },
    {
        "id": 5,
        "name": "ViVi",
        "fullName": "Wong Gaahei",
        "birth": "961209",
        "solo": "Everyday I Love You",
        "subunit": "1/3",
        "colour": "pastel rose",
        "animal": "deer",
        "colourHex": "#ffc5c8",
    },
    {
        "id": 6,
        "name": "Kim Lip",
        "fullName": "Kim Jungeun",
        "birth": "190210",
        "solo": "Eclipse",
        "subunit": "ODD EYE CIRCLE",
        "colour": "red",
        "animal": "owl",
        "colourHex": "#d90011",
    },
    {
        "id": 7,
        "name": "Jinsoul",
        "fullName": "Jung Jinsoul",
        "birth": "970613",
        "solo": "Singing In The Rain",
        "subunit": "ODD EYE CIRCLE",
        "colour": "royal blue",
        "animal": "betta fish",
        "colourHex": "#0801d5",
    },
    {
        "id": 8,
        "name": "Choerry",
        "fullName": "Choi Yerim",
        "birth": "010604",
        "solo": "Love Cherry Motion",
        "subunit": "ODD EYE CIRCLE",
        "colour": "purple",
        "animal": "fruit bat",
        "fruit": "cherry",
        "colourHex": "#ba01de",
    },
    {
        "id": 9,
        "name": "Yves",
        "fullName": "Ha Sooyoung",
        "birth": "970524",
        "solo": "new",
        "subunit": "yyxy",
        "colour": "burgundy",
        "animal": "swan",
        "fruit": "apple",
        "colourHex": "#790105",
    },
    {
        "id": 10,
        "name": "Chuu",
        "fullName": "Kim Jiwoo",
        "birth": "991020",
        "solo": "Heart Attack",
        "subunit": "yyxy",
        "colour": "peach",
        "animal": "penguin",
        "fruit": "strawberry",
        "colourHex": "#fea87d",
    },
    {
        "id": 11,
        "name": "Go Won",
        "fullName": "Park Chaewon",
        "birth": "001119",
        "solo": "One & Only",
        "subunit": "yyxy",
        "colour": "eden green",
        "animal": "butterfly",
        "fruit": "pineapple",
        "colourHex": "#02bca1",
    },
    {
        "id": 12,
        "name": "Olivia Hye",
        "fullName": "Son Hyejoo",
        "birth": "011113",
        "solo": "Egoist",
        "subunit": "yyxy",
        "colour": "silver",
        "animal": "wolf",
        "fruit": "blood plum",
        "colourHex": "#c0c0c0",
    }
]


class Member(Resource):
    def get(self, id=0):
        if id == 0:
            return loona_members, 200

        for member in loona_members:
            if member["id"] == id:
                return member, 200
        return "Member not found", 404


api.add_resource(Member, "/loona-api", "/loona-api/", "/loona-api/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
