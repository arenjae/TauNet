import socket
from tcpTools import set_name, set_conn, log, pp_host, send, receive


# HOST_PAIR = ('localhost', 2001)



class client:
    def __init__(self, target,message):
        self.set_name("Client")
        self.target = target
        self.message = message

    def clientStart(self, target,message):

        self.message = message
        try:
            log("Connecting on {}.".format(pp_host(target)))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            set_conn(sock)
            sock.connect(target)
            send(self.message)
            data = receive()
            if data:
                log("Message successfully received")
        except KeyboardInterrupt:
            log("Killed.")
        finally:
            log("Closing socket.")
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
