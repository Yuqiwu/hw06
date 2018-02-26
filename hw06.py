from flask import Flask, render_tempalte, url_for
import json
import pymongo

app = Flask(__name__)

s = open("s", "r")
doc = s.read()

dic = json.loads(doc)

final = []
for episode in dic["_embedded"]["episodes"]:
    final.append(episode)
    

connection = pymongo.MongoClient("149.89.150.100")
db.notwalylime.drop()
db = connection.notwalylime

for each in final:
    print each
    db.rick_and_morty.insert( each )

@app.route("/")
def root():
    return render_templates("form.html")

@app.route("/result", methods=["GET","POST"])
def result():
    season = request.form['value']
    return render_templates("list.html")


