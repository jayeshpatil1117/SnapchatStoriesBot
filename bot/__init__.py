import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "35930308"))
    API_HASH = os.environ.get("API_HASH","a1f668b2b94e47e56ad23a116b0bbec8" )
    BOT_TOKEN = os.environ.get("BOT_TOKEN" ,"8590980373:AAEo8ca9mUyzfoaAq8GlvD7vk1Fl0_CQJ4c")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" ,"ggemma_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
