#!/usr/bin/python
#coding:utf-8

import threading
import time

class BeatHeart(threading.Thread):
	def __init__(self, seconds, logger):
		threading.Thread.__init__(self)
		self.seconds = seconds
		self.logger = logger
		self.daemon = True
		
	def run(self):
		while True:
			#发送心跳包到zmq
			self.logger.info("after sleeping (%d)", self.seconds)
			time.sleep(self.seconds)