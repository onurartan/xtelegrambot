from dotenv import load_dotenv
import os
load_dotenv()

class Env:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    # API_KEY = os.getenv("TWITTER_API_KEY")
    # API_KEY_SECRET = os.getenv("TWITTER_API_KEY_SECRET")
    # ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    # ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
    # BEARER_TOKEN = os.getenv("BEARER_TOKEN")