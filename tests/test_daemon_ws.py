from config.module import TESTNET_NODE_WS
from daemon.websocket import DaemonWS
import daemon.classes as classes

TESTNET_ADDR = "xet:rsdm79np9eqar7cg5jy9sdhwas74l4ml5enaasmae8jtjcvpr3vqqnlpysy"

def test_daemon():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getInfo()
  print(data)
  daemon.close()
  
def test_getVersion():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getVersion()
  print(data)
  daemon.close()
    
def test_getHeight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getHeight()
  print(data)
  daemon.close()
    
def test_getTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getTopoheight()
  print(data)
  daemon.close()
    
def test_getStableheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getStableheight()
  print(data)
  daemon.close()
    
def test_getBlockTemplate():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlockTemplate(address=TESTNET_ADDR)
  print(data)
  daemon.close()
    
def test_getBlockAtTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlockAtTopoheight(classes.GetBlockAtTopoheightParams(topoheight=0, include_txs=False))
  print(data)
  daemon.close()
    
def test_getBlocksAtHeight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlocksAtHeight(classes.GetBlocksAtHeightParams(height=0, include_txs=False))
  print(data)
  daemon.close()