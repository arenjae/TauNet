# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import protocol
import socket

logMessage = []
logTarget = []
def clientFunc(target, message):
    try:
        print("Connecting on {}:{}.".format(*target))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect(target)
        sock.send(message)
        sock.shutdown(socket.SHUT_RDWR)

    except KeyboardInterrupt:
        print("Killed.")

    except:
        print("TauNet node {}:{}".format(*target) + " is offline.")
        print("Saving Message in Log...")
        logMessage.append(protocol.decrypt(message,str.encode('password')))
        logTarget.append(target)

    finally:
        sock.close()
