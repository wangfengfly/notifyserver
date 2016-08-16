#!/usr/bin/python
#coding:utf-8

import threading
import time
import ctypes as ct

#from ZmqFactory.ServerFactory import ServerFactory

class BeatHeart(threading.Thread):
	def __init__(self, seconds, logger):
		threading.Thread.__init__(self)
		self.seconds = seconds
		self.logger = logger
		self.daemon = True
		
	def run(self):
		while True:
			msg = "<L><DataFinder><L><" + str(time.time()) + ">"
                        ll = ct.cdll.LoadLibrary 
                        lib = ll("/home/soft/msgsend_lib/libmsgsend.so")   
                        lib.SetConnect("192.168.60.27", "6677")
                        lib.MsgSend("DataFinder", "Alive")
                        lib.MsgSend("DataFinder", msg)
#			ServerFactory.getServer("push").send(msg)
			time.sleep(self.seconds)
