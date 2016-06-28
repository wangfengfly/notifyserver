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
			#self.logger.info("after sleeping (%d)", self.seconds)
			ServerFactory.getServer("push").send("after sleeping " + str(self.seconds))
			time.sleep(self.seconds)