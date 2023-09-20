import json
from counter import ResettableCounter

from generator import MessageGenerator

hello = {
    "mess": "chat",
    "data": {"text": "{text}"},
}

pong = {"mess": "pong", "data": {"from": "money", "imAlive": "1231231"}}

join = {
    "mess": "join",
    "data": {
        "extended": {
            "birth": "2005-02-01",
            "city": "20317",
            "height": "null",
            "relat": "null",
            "sex": "m",
            "text": "null",
            "weight": "null",
        },
        "room": "{room_id}",
    },
}

leave = {
    "mess": "leave",
    "data": {
        "extended": {
            "birth": "2005-02-01",
            "city": "20317",
            "height": "null",
            "relat": "null",
            "sex": "m",
            "text": "null",
            "weight": "null",
        },
        "room": "{room_id}",
    },
}


class Messenger:
    def __init__(self):
        self.message_generator = MessageGenerator(None)

    def join_room(self, message):
        room_id = message["response"]["room"]["alias"]
        return json.dumps(join).replace('"{room_id}"', f'"{room_id}"')

    def handle_message(self, message, counter: ResettableCounter):
        print(counter.get_value())
        json_message = json.loads(message)
        if json_message["mess"] == "money":
            return json.dumps(pong)

        if json_message["response"]["type"] == "publish":
            return self.join_room(json_message)

        if (json_message["response"]["type"] == "add") and counter.get_value() <= 1:
            counter.increment()
            return json.dumps(hello).replace(
                '"{text}"',
                f'"{self.message_generator.generate_random_phase_from_json()}"',
            )
        return None
