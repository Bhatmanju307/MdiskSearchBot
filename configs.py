# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "AQASswiLtbujU0PO9L-Cu3N3PQsYfrsdvzfmtLLB3_YC8a")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001831635652))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1158419686"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/serials_funda'>serial Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/ded_eye'>dead eye</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/ded_eye'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm serial Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @serials_funda</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm serials Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @serials_funda</a></b>
"""


