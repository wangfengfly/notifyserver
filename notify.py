#!/usr/bin/python
#coding:utf-8

import logging
import inotify.adapters
import fnmatch
import thread
import time
import sys
from beatheart import BeatHeart
import ConfigParser
	
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
dict = {}

def parse_config():
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	if config.has_option('default', 'rootdir'):
		dict["dir"] = config.get("default", "rootdir")
	else:
		print('请在config.ini中配置要扫描的根目录rootdir')
		sys.exit(1)
	if config.has_option('default', 'seconds'):
		dict["seconds"] = float(config.get("default", "seconds"))
	else:
		dict['seconds'] = 30
	if config.has_option('default', 'postfixes'):
		dict["suffixes"] = config.get("default", "postfixes").split()
	else:
		dict['suffixes'] = []

def configure_logger():
	logger.setLevel(logging.INFO)
	ch = logging.StreamHandler()
	formatter = logging.Formatter(LOG_FORMAT)
	ch.setFormatter(formatter)
	logger.addHandler(ch)

def postfix_filter(fn):
	if not dict['suffixes']:
		return True
	for suffix in dict['suffixes']:
		if fnmatch.fnmatch(fn, suffix):
			return True
	return False

def main():
	i = inotify.adapters.InotifyTree(dict['dir'])
	for event in i.event_gen():
		if event is not None:
			(hd, tn, wp, fn) = event
			if postfix_filter(fn):
				logger.info("WD=(%d) MASK=(%d) COOKIE=(%d) LEN=(%d) MASK->NAMES=%s "
					"WATCH-PATH=[%s] FILENAME=[%s]", 
					hd.wd, hd.mask, hd.cookie, hd.len, tn, wp, fn)

		
if __name__ == '__main__':
	parse_config()
	beatHeart = BeatHeart(dict['seconds'], logger)
	beatHeart.start()
	
	configure_logger()
	main()
	
	