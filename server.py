import socket
import protocol
from tcpTools import set_name, set_conn, log, pp_host, send, receive

password = str.encode('password')

PORT = 6283
host = 'pi.arenjae.com'
host = 'localhost'

class server:
    def __init__(self):
        set_name("Server")
        self.host_pair = ('localhost', PORT)
        print("Server Initialized...")

    def startServer(self):

        set_name("Server")
        log("Server Started...")
        self.host_pair = (host, PORT)

        try:
            log("Listening on {}.".format(pp_host(self.host_pair)))
            conn = None
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listener.bind(self.host_pair)

            while True:
                listener.listen(10)

                conn, sender = listener.accept()
                set_conn(conn)
                log("Got a connection from {}.".format(pp_host(sender)))
                data = receive()
                if data:
                    send(str.encode("Message received by Rachael"))
                    log("Message successfully received")
                    log("Message decrypted")
                    log("Message: " + str(protocol.decrypt(data, password)))
                else:
                    log("Lost client.")

        except KeyboardInterrupt:
            log("Killed.")

        finally:
            log("Closing socket.")
            if conn:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
