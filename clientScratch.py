import socket

from tcp_toolsScratch import set_name, set_conn, log, pp_host, send, receive

HOST_PAIR = ("localhost", 2001)

set_name("Client")

try:
    log("Connecting on {}.".format(pp_host(HOST_PAIR)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    set_conn(sock)
    sock.connect(HOST_PAIR)
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
