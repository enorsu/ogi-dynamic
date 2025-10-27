import flask
from flask import request
from markupsafe import escape
import json
import logging

# functions
def loadJsonFile(filename, raw = False):
    with open("./data/" + filename, "r") as s:
        if raw:
            return s.read()
        else:
            return json.loads(s.read())
def refreshGamesJson():
    global games
    games = loadJsonFile("games.json")

def initlogging():
    logging.basicConfig(format = "{asctime} - {levelname} - {message}", style = "{", datefmt = "%Y-%m-%d %H:%M", filename="app.log", encoding="utf-8",  filemode="a", level=logging.DEBUG)

def initialize():
    refreshGamesJson()

def generateGame(title, label, cover, desc, dl_fi, dl_en):
    item =  {
        "title": title,
        "label": label,
        "cover": cover,
        "description": desc,
        "downloads": {
            "fi": dl_fi,
            "en": dl_en
        }
    }
    return item
def addgame(game: dict):
    with open("./data/games.json", "r") as i:
        js = json.loads(i.read())
    js.update({"counter": js["counter"] + 1})
    js.update({str(js["counter"]): game})
    with open("./data/games.json", "w") as s:
        s.write(json.dumps(js, indent=4))
    refreshGamesJson()

def replaceGames(g: dict):
    with open("./data/games.json", "w") as file:
        file.write(json.dumps(g, indent=4))





# init app
initialize()

app = flask.Flask(__name__)


# pages
@app.route("/")
def index():
    return flask.redirect("/static/index.html", code=200)

@app.route("/pages/downloads")
def downloads():
    temp = games
    print(temp)
    temp.pop("counter") 
    print(temp)
    return flask.render_template("dl.html", games=temp)

@app.route("/form")
def form():
    return flask.render_template("form.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    return flask.render_template("shark.html")

# API
@app.route("/api/downloads/raw")
def downloadsraw():
    return games

@app.route('/api/addgame', methods=['POST'])
def addgames():
    data = flask.request.form
    gm = generateGame(title=data["title"], desc=data["desc"], dl_en=data["dl-en"], dl_fi=data["dl-fi"], cover=data["cover"], label=data["label"])
    addgame(gm)
    return "done"

@app.route("/admin/gamemanager")
def gamemanager():
    return flask.render_template("gamemanager.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return flask.render_template('404.html'), 404



app.run(port=8000)