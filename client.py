import socket

from tcp_toolsScratch import set_name, set_conn, log, pp_host, send, receive

#HOST_PAIR = ('localhost', 2001)


class client:

    set_name("Client")

    def __init__(self, target):

        self.target = target

    def clientStart(self, target):
        try:
            log("Connecting on {}.".format(pp_host(target)))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            set_conn(sock)
            sock.connect(target)
            send("Hi!")
            data = receive()
            send("FLAGPLS")
            data = receive()
            if data:
                log("Got the flag!")
        except KeyboardInterrupt:
            log("Killed.")
        finally:
            log("Closing socket.")
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
