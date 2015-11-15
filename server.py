import socket
import protocol

from tcp_toolsScratch import set_name, set_conn, log, pp_host, send, receive

password = str.encode('password')

class server:

    def __init__(self):
        set_name("Server")
        self.host_pair = ('localhost',6031)
        print("Server Initialized...")

    def startServer(self):
        print("Server Started...")
        set_name("Server")
        self.host_pair = ('localhost',6031)

        try:
            log("Listening on {}.".format(pp_host(self.host_pair)))
            conn = None
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listener.bind(self.host_pair)
            listener.listen(10)

            conn, sender = listener.accept()
            set_conn(conn)
            log("Got a connection from {}.".format(pp_host(sender)))
            data = receive()
            if data:
                send(str.encode("Message received by Rachael"))
                log("Message successfully received")
                print(protocol.decrypt(data, password))
            else:
                log("Lost client.")
        except KeyboardInterrupt:
            log("Killed.")
        finally:
            log("Closing socket.")
            if conn:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
