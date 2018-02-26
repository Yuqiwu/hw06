from flask import Flask, render_template, redirect, request
import json
import pymongo
import notwalylime

app = Flask(__name__)

s = open("s", "r")
doc = s.read()

dic = json.loads(doc)

final = []
for episode in dic["_embedded"]["episodes"]:
    final.append(episode)
    

connection = pymongo.MongoClient("149.89.150.100")
db = connection.notwalylime
db.rick_and_morty.drop()

for each in final:
    db.rick_and_morty.insert( each )

@app.route("/")
def root():
    s1 = []
    s2 = []
    s3 = []
    for episode in notwalylime.find_season(1):
        s1.append(episode["number"])
    for episode in notwalylime.find_season(2):
        s2.append(episode["number"])
    for episode in notwalylime.find_season(3):
        s3.append(episode["number"])
    return render_template("form.html", season1=s1,season2=s2,season3=s3)

@app.route("/result", methods=["GET","POST"])
def result():
    season = 0
    if "1episode" in request.form:
        season = 1
        episode = int( request.form['1episode'])

    elif  "2episode" in request.form:
        season = 2
        episode = int( request.form['2episode'] )

    else:
        season = 3
        episode = int(request.form['3episode'])
        
    print season
    print episode

    result = notwalylime.find_season_episode(season, episode)
    url = result['url']
    return redirect(url)

if __name__ == "__main__":
    app.debug = True
    app.run()
