import zmq
from Server import Server

class PushServer(Server):

    def __init__(self):
		self.c = zmq.Context()
		self.s = self.c.socket(zmq.PUSH)
		self.s.bind("tcp://*:10001")
		
    def send(self, msg):
		self.s.send(msg)
	
    def __del__(self):
		self.s.close()

	
