import threading
from counter import ResettableCounter
from messenger import Messenger

from websocket_client import WebSocketClient


class Bot:
    def __init__(self, name, url, headers):
        self.name = name
        self.websocket = WebSocketClient(
            url,
            headers,
            on_message_callback=self.on_message,
            on_error_callback=self.on_error,
            on_open_callback=self.on_open,
            on_close_callback=self.on_close,
        )
        self.thread = threading.Thread(target=self.websocket.start)
        self.thread.daemon = False
        self.message_handler = Messenger()
        self.counter = ResettableCounter()
        self.counter.start_reset_timer()

    def start(self):
        self.thread.start()

    def on_message(self, ws, message):
        print(f"{self.name} received a message: {message}")
        response = self.message_handler.handle_message(message, self.counter)
        if response != None:
            self.websocket.send_message(response)

    def on_error(self, ws, error):
        print(f"{self.name} encountered an error: {error}")

    def on_open(self, ws):
        print(f"{self.name} opened connection")

    def on_close(self, ws, close_status_code, close_msg):
        print(
            f"{self.name} closed connection: {close_msg} (status code: {close_status_code})"
        )
