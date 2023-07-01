import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB_FILE = BASE_DIR.joinpath('db.sqlite3')
TEMPLATES_DIR = BASE_DIR.joinpath('templates')

DATE_FORMAT = "%d.%m.%Y"

EVENTLIST_CALLBACK_PATTERN = "eventlist_"
EVENT_PROFILE_CALLBACK_PATTERN = "eventprofile_"
USERLIST_CALLBACK_PATTERN = "userlist_"
USER_PROFILE_CALLBACK_PATTERN = "userprofile_"
TOP_MENU_CALLBACK_PATTERN = "top_"
TOP_SUBMENU_CALLBACK_PATTERN = "topsubmenu_"
RULES_CALLBACK_PATTERN = "rules_"
RULETYPE_CALLBACK_PATTERN = "ruletype_"
ROLE_CALLBACK_PATTERN = "role_"


EVENTLIST_PAGE_LENGTH = 2
TOP_PAGE_LENGTH = 10
