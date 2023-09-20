from bot import Bot
from auth import Auth


LIVACHA_URL = "https://livacha.com"


if __name__ == "__main__":
    auth_instance = Auth(LIVACHA_URL)

    bot1 = Bot(
        "bot1",
        "wss://livacha.com:8443",
        auth_instance.get_token_and_cookies(),
    )

    bot1.start()
