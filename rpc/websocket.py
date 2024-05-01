import json
from websockets.sync.client import connect, ClientConnection
import daemon.methods as methods
import daemon.classes as classes

class RPCWS:
  id: int
  client: ClientConnection

  def __init__(self, url: str, headers = {}) -> None:
    self.id = 0
    self.client = connect(url, additional_headers=headers)
    
  def __createRequestMethod(self, method: str, params = None):
    self.id += 1
    data = { "id": self.id, "jsonrpc": "2.0", "method": method }
    if params is not None:
      data["params"] = params
    
    return json.dumps(data)

  def send(self, method, params = None):
    sendData = self.__createRequestMethod(method=method, params=params)
    self.client.send(sendData)
    
    recvData = self.client.recv()
    data = json.loads(recvData)
    if "error" in data:
      raise ValueError(data["error"]["message"])
    
    return data["result"]
  
  def close(self):
    self.client.close()
  