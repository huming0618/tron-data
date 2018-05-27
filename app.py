import requests
from Node import Node

# {"ip":"43.242.174.228","port":500051,"nodeType":2,"hostname":"43.242.174.228","lastSeen":1527086355957,"permanent":false,"lastBlock":244,"grpcEnabled":true,"grpcResponseTime":1520,"country":"Hong Kong","city":"San Po Kong","lat":22.3333,"lng":114.2}
nodeAPI = Node()
for item in nodeAPI.list():
    print(item["ip"])