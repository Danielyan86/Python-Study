import socket
import socketserver as SocketServer


class PortForwardingRequestHandler(SocketServer.BaseRequestHandler):
    '''处理端口转发请求
    '''

    def handle(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.server)  # self.server是在动态创建类时传入的
        # 连接目标服务器，并转发数据
        # 以下代码省略...


def gen_cls(server):
    '''动态创建子类
    '''
    return type('%s_%s' % (ProxyRequestHandler.__name__, server), (PortForwardingRequestHandler, object),
                {'server': server})


server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8080), gen_cls(('www.qq.com', 80)))
server.serve_forever()
