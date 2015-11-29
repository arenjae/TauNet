# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import socket

def clientFunc(target, message):
    try:
        print("Connecting on {}:{}.".format(*target))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect(target)
        sock.send(message)

    except KeyboardInterrupt:
        print("Killed.")
    finally:
        pass
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
