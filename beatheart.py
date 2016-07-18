#!/usr/bin/python
#coding:utf-8

import threading
import time
from ZmqFactory.ServerFactory import ServerFactory

class BeatHeart(threading.Thread):
	def __init__(self, seconds, logger):
		threading.Thread.__init__(self)
		self.seconds = seconds
		self.logger = logger
		self.daemon = True
		
	def run(self):
		while True:
			msg = "<L><DataFinder><L><" + str(time.time()) + ">"
			ServerFactory.getServer("push").send(msg)
			time.sleep(self.seconds)