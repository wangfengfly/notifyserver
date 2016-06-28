import sys
import zmq

class ZmqClient:
	
	def __init__(self, port):
		self.port = port
		self.context = zmq.Context()
		self.s = self.context.socket(zmq.PULL)
		self.s.connect("tcp://127.0.0.1:%s" % self.port)
		
	def recv(self, topic):
		#self.s.setsockopt(zmq.SUBSCRIBE, topic)
		msg = self.s.recv()
		return msg
	
	def __del__(self):
		self.s.close()


zmq_c = ZmqClient('10001')
for i in range(0, 100):
	msg = zmq_c.recv("sender")
	print msg