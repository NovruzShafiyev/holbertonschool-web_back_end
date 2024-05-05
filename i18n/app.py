#!/usr/bin/env python3
"""Base flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
import pytz
import datetime

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Setups"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
# babel = Babel(app)


def get_user() -> Union[dict, None]:
    """ Get the user of the dict

        Return User
    """
    login_user = request.args.get('login_as', None)

    if login_user is None:
        return None

    user: dict = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]


# @babel.localeselector
def get_locale():
    """Get locale"""
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang

    lang = request.headers.get("locale", None)
    if lang in app.config["LANGUAGES"]:
        return lang

    return Config.BABEL_DEFAULT_LOCALE

# @babel.timezoneselector
def get_timezone() -> str:
    try:
        timezone = request.args.get("timezone")
        if timezone:
            pytz.timezone(timezone)
            print("REQ")
        elif g.user:
            timezone = g.user["timezone"]
            print("USER")
            pytz.timezone(timezone)
        else:
            timezone = Config.BABEL_DEFAULT_TIMEZONE
            print("DEF")
            pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        timezone = 'UTC'

    return datetime.datetime.now(pytz.timezone(timezone)).strftime("%B %d, %Y %I:%M:%S %p")
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)

@app.route('/')
def home():
    """ Home Page
    """
    return render_template('index.html')


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()
    g.current_time = get_timezone()
    print(g.current_time)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
