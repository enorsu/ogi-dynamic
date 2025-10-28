import flask
from flask import request
from markupsafe import escape
import json
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
# functions
def loadJsonFile(filename, raw = False):
    with open("./data/" + filename, "r") as s:
        if raw:
            return s.read()
        else:
            return json.loads(s.read())
def refreshGamesJson():
    global games
    global passkey
    games = loadJsonFile("games.json")
    passkey = loadJsonFile("config.json")["passkey"]

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

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


# pages
@app.route("/")
def index():
    return flask.redirect("/static/index.html", code=200)

@app.route("/pages/downloads")
def downloads():
    temp = games
    try:
        temp.pop("counter")
    except KeyError:
        pass
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
    if not data["passkey"] == passkey:
        return flask.render_template("message.html", message="You are not authorized.")

    gm = generateGame(title=data["title"], desc=data["desc"], dl_en=data["dl-en"], dl_fi=data["dl-fi"], cover=data["cover"], label=data["label"])
    addgame(gm)
    return flask.render_template("message.html", message="Succesfully added the game.")

@app.route("/admin/gamemanager", methods=['POST', 'GET'])
def gamemanager():
    if flask.request.method == "GET":
        return flask.render_template("gamemanager.html", game=generateGame("", "", "", "", "", ""))
    elif flask.request.method == "POST":
        try:
            game = games[flask.request.form["game"]]
        except KeyError as err:
            return flask.render_template("message.html", message=f"Game {err} not found", url="/admin/gamemanager")
        return flask.render_template("gamemanager.html", game=game, url="/admin/gamemanager")

@app.route("/api/update", methods=["POST"])
def update():
    
    payload = str(flask.request.json)
    if "https://github.com/enorsu" in payload:
        print("success, updating")
        return "", 202
    else:
        return "fail", 400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return flask.render_template('404.html'), 404



