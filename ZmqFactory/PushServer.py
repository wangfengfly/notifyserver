import zmq
from Server import Server
import threading

class PushServer(Server):
	__instance = None
	__lock = threading.Lock()
	
	def __new__(self):
		if(PushServer.__instance == None):
			PushServer.__lock.acquire()
			if(PushServer.__instance == None):
				PushServer.__instance = object.__new__(self)
				self.c = zmq.Context()
				self.s = self.c.socket(zmq.PUSH)
				self.s.bind("tcp://*:10001")
			PushServer.__lock.release()
		return PushServer.__instance
	
	def __init__(self):
		pass
		
	def send(self, msg):
		self.s.send(msg)
	
	def __del__(self):
		self.s.close()

	
