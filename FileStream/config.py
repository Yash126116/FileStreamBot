from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID"))
    API_HASH = str(env.get("API_HASH"))
    BOT_TOKEN = str(env.get("BOT_TOKEN"))
    OWNER_ID = int(env.get('OWNER_ID', '1237293986'))
    WORKERS = int(env.get("WORKERS", "6"))
    DATABASE_URL = str(env.get('DATABASE_URL'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Cs_bots"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = int(env.get('FORCE_SUB_ID', -1002213031850))
    FORCE_SUB = str(env.get('FORCE_SUB', 'False')).lower() == "true"
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", None))
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", None))
    MODE = env.get("MODE", "primary")
    SECONDARY = MODE.lower() == "secondary"
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = "0.0.0.0"
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = True  # Explicitly set NO_PORT to True to avoid adding port in the URL
    FQDN = str(env.get("FQDN", "filetogwye-67556444e345.herokuapp.com"))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "",
        FQDN,
        "" if NO_PORT else ":" + str(PORT)
    )
