import zmq
from PushServer import PushServer

class ServerFactory:
	@staticmethod
	def getServer(mode):
		if(mode.lower() == "push"):
			return PushServer()
		else:
			return None

s = ServerFactory.getServer("push")
for i in range(0, 10000):
	s.send("sending " + str(i))