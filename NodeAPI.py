import requests
import json

# "ip":"43.242.174.228","port":500051,"nodeType":2,"hostname":"43.242.174.228","lastSeen":1527086355957,"permanent":false,"lastBlock":244,"grpcEnabled":true,"grpcResponseTime":1520,"country":"Hong Kong","city":"San Po Kong","lat":22.3333,"lng":114.2}
class Node(object):
    ip:str
    port:int
    nodeType:int
    hostname:str
    

class NodeAPI(object):
    def list(self):
        result = None
        resp = requests.get("https://api.tronscan.org/api/node")
        if resp.status_code == 200:
            data = json.loads(resp.text)
            result = data["nodes"]
            node = Node()
            for item in data["nodes"]:
                node.ip = item['ip']
                node.port = item['port']
                node.hostname = item['hostname']
            
        return result