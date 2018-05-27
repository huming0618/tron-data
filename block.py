import requests

class block(object):
    def list(self):
        resp = requests.get("https://api.tronscan.org/api/block")

    def last(self):
        None