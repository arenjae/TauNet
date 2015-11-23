# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import socket
import protocol
import threading
import select

messages = []
password = str.encode('password')

PORT = 6283
host = 'localhost'
#host = '192.168.1.141'

class server (threading.Thread):
    def run(self):

        print("Server Started...")
        self.host_pair = (host, PORT)

        try:
            print("Listening on {}:{}.".format(*self.host_pair))
            conn = None
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind(self.host_pair)
            listener.listen(10)

            while True:
                conn, sender = listener.accept()
                threading.Thread(target=getMessage, args=(conn,)).start()

        except KeyboardInterrupt:
            print("Killed.")

        except:
            print("Lol you dieded")

        finally:
            print("Closing socket.")
            if conn:
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()



def getMessage(conn):
    readable, writable, exceptional = select.select([conn], [], [])
    buffer = b""
    for s in readable:
        while True:
            temp = s.recv(256)
            if temp:
                buffer += temp
            else:
                s.close()
                break;
    messages.append(protocol.decrypt(buffer, password).decode('ascii') + '\n')

