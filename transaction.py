import requests

class transaction(object):
    def list(self):
        resp = requests.get("https://api.tronscan.org/api/transaction")
