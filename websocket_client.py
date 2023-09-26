import ssl
import websocket


class WebSocketClient:
    def __init__(
        self,
        url,
        headers,
        on_message_callback=None,
        on_error_callback=None,
        on_open_callback=None,
        on_close_callback=None,
    ):
        self.url = url
        self.headers = headers
        self.on_message_callback = on_message_callback
        self.on_error_callback = on_error_callback
        self.on_open_callback = on_open_callback
        self.on_close_callback = on_close_callback
        self.ws = None

    def start(self):
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.url,
            header=self.headers,
            on_open=self.on_open_callback,
            on_message=self.on_message_callback,
            on_error=self.on_error_callback,
            on_close=self.on_close_callback,
        )
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        