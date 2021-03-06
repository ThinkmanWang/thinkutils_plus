# Let's import tornado and tornadis
import tornado
from thinkutils.tornadis.client import *
from thinkutils.tornadis.exceptions import *


@tornado.gen.coroutine
def talk_to_redis():
    # let's (re)connect (autoconnect mode), call the ping redis command
    # and wait the reply without blocking the tornado ioloop
    # Note: call() method on Client instance returns a Future object (and
    # should be used as a coroutine).
    result = yield client.call("PING")
    if isinstance(result, TornadisException):
        # For specific reasons, tornadis nearly never raises any exception
        # they are returned as result
        print "got exception: %s" % result
    else:
        # result is already a python object (a string in this simple example)
        print "Result: %s" % result


# Build a tornadis.Client object with some options as kwargs
# host: redis host to connect
# port: redis port to connect
# autoconnect=True: put the Client object in auto(re)connect mode
client = Client(host="localhost", port=6379, autoconnect=True)

# Start a tornado IOLoop, execute the coroutine and end the program
loop = tornado.ioloop.IOLoop.current()
loop.run_sync(talk_to_redis)
