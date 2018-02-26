import json
import pymongo

s = open("s", "r")
doc = s.read()

dic = json.loads(doc)

final = []
for episode in dic["_embedded"]["episodes"]:
    final.append(episode)
    

connection = pymongo.MongoClient("149.89.150.100")
db = connection.notwalylime
#db.create_collection("rick_and_morty")

for each in final:
    print each
    db.rick_and_morty.insert( each )
