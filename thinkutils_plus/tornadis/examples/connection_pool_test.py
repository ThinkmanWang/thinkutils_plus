
import tornado
import tornado.gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options

from thinkutils.tornadis.client import *
from thinkutils.tornadis.pool import *
from thinkutils.config.Config import *
from CPATCPServer.CPATCPServer import *

g_tornadis_pool = ClientPool(max_size=512, host=g_config.get("redis", "host"), db=1, port=int(g_config.get("redis", "port")), password=g_config.get("redis", "password"), autoconnect=True)

@tornado.gen.coroutine
def main():
    # client = g_tornadis_pool.get_client_nowait()
    # if client is not None:
    with (yield g_tornadis_pool.connected_client()) as client:
        try:
            yield client.call("SET", "2017-08-01", "Hello World!!!!")
            szTxt = yield client.call("GET", "2017-04-17")
            print szTxt

            szRet = yield client.call("SISMEMBER", "tcpserver_client_info_saved_2017-07-26", "123")
            print szRet
        finally:
            g_tornadis_pool.release_client(client)

    # client = g_tornadis_pool.get_client_nowait()
    # if client is not None:
    with (yield g_tornadis_pool.connected_client()) as client:
        try:
            yield client.call("SET", "2017-08-01", "Hello World!!!!")
            szTxt = yield client.call("GET", "2017-04-17")
            print szTxt

            szRet = yield client.call("SISMEMBER", "tcpserver_client_info_saved_2017-07-26", "123")
            print szRet
        finally:
            g_tornadis_pool.release_client(client)

    ip = yield TCPConnection.get_distribute_config("14785884078949750928105", "14949283188503311770553")
    print ip
    if ip is None or 0 == len(ip):
        g_logger.debug("FXXK")

# if __name__ == '__main__':
#     loop = tornado.ioloop.IOLoop.current()
#     loop.run_sync(main)