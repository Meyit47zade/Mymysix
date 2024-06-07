from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAGbSM0AVNfkcDhD1Ywy9H9RpUsq2vR-M3D0PFr_rSUe8EdejcNA7k3nHRTwrFhBd9CO6ppdlGBG6Khkbn4EjUCruD7CFpqYGTJdY3Vdb8EWViL1SClwc5_eoT44x6bgvLoKfWD7L2IJdOqLjl_WvKwHSUOALuERVVN-W3tYg0lUYS0zxxn_I0ic10ToxV1lii-WVQTHbp-GE7RaM7Pter9k2RdAkONMtI1Ey2hhZQKZxbW0APnJ1nFsFrqV0sX2NakjcmovtIeuRpML5-2uNcRW98SEivr94G7hP214iyphhZuO6m5s5oGVwH0QRlJXwQAXfK-3NXODEMKfg9LaePy2x3k4BQAAAAGD4cIEAA")
API_ID = int(getenv("API_ID", "22467439"))
API_HASH = getenv("API_HASH", "cec47ae9c153dcf1aa74999a389b3341")
BOT_TOKEN = getenv("BOT_TOKEN", "7218232167:AAHiNANcjt6PggG-92Hijy2Jx5GMUW7BCqo")
BOT_NAME = getenv("BOT_NAME", "kyctepkibot") 
BOT_USERNAME = getenv("BOT_USERNAME", "kyctepki_bot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "hayalhanemkanal")
ASS_USERNAME = getenv("ASS_USERNAME", "meyit01")
OWNER = getenv("OWNER", "6510559004")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6510559004").split()))
