# notifyserver
This project is used for monitoring file system state changing, using python language and factory pattern. Zeromq supports Pub/Sub, PUSH/PULL, 
req/rep etc. So with factory pattern, we can add new server without changing existing code, in this way, the code is more extensible.
Also the beatheart is sent by child threads.
