import zmq
from PushServer import PushServer

class ServerFactory:
	@staticmethod
	def getServer(mode):
		if(mode.lower() == "push"):
			return PushServer()
		else:
			return None
