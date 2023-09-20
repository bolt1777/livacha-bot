import threading


class ResettableCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
        self.reset_timer = None

    def increment(self):
        with self.lock:
            self.value += 1

    def get_value(self):
        with self.lock:
            return self.value

    def start_reset_timer(self, interval=300):
        if self.reset_timer:
            self.reset_timer.cancel()
        self.reset_timer = threading.Timer(interval, self.reset)
        self.reset_timer.daemon = True
        self.reset_timer.start()

    def reset(self):
        with self.lock:
            self.value = 0
            self.start_reset_timer()
