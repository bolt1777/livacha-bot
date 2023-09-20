import os
import requests
import json
import re

payload = {
    "login": os.environ.get("LIVACHA_USER"),
    "password": os.environ.get("LIVACHA_PASS"),
    "remember": "1",
    "_v2": "1",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Accept": "application/json",
}


class Auth:
    def __init__(self, livacha_url):
        self.livacha_url = livacha_url

    def get_token_and_cookies(self):
        """Auth section to get cookies"""

        session = requests.Session()
        r = session.get(self.livacha_url, headers=headers)
        pattern = r"window\.__app_settings = (.*?);"
        match = re.search(pattern, r.text)
        if match:
            js_object_str = match.group(1)
            js_object = json.loads(js_object_str)
            payload["_token"] = js_object.get("token")
        else:
            print("JavaScript object not found on the page.")

        r = session.post(self.livacha_url + "/login", data=payload, headers=headers)
        cookies = session.cookies.get_dict()
        headers["Cookie"] = "; ".join(["%s=%s" % (i, j) for i, j in cookies.items()])
        return headers
