import multiprocessing
from time import sleep
from bot import Bot
from auth import Auth

LIVACHA_URL = "https://livacha.com"

bot_names = ["Bot1", "Bot2", "Bot3"]


def run_bot(bot_name):
    auth_instance = Auth(LIVACHA_URL)
    bot = Bot(
        bot_name,
        "wss://livacha.com:8443",
        auth_instance.get_token_and_cookies(),
    )
    bot.start()


if __name__ == "__main__":
    processes = []

    for bot_name in bot_names:
        process = multiprocessing.Process(target=run_bot, args=(bot_name,))
        processes.append(process)

    for process in processes:
        process.start()
        sleep(10)

    for process in processes:
        process.join()
