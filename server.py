# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import socket
import protocol
import threading
import select
import datetime

messages = []
password = str.encode('password')

PORT = 6283
host = 'localhost'


# Change this to whatever your local network ip address is
# (if you have port forwarding enabled)
# host = '192.168.1.141'


class server(threading.Thread):
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
			print("(Check to make sure you have the right host entered)")

		finally:
			print("Closing socket.")
			if conn:
				conn.shutdown(socket.SHUT_RDWR)
				conn.close()


def getMessage(conn):
	readable, writable, exceptional = select.select([conn], [], [], 5)
	buffer = b""
	for s in readable:
		buffer = s.recv(1024)
		s.close()
		break

	if len(buffer) > 0:
		messages.append(parseMessage(protocol.decrypt(buffer, password)) + '\n')


def stripMessage(decryptedMessage):
	if len(str.split(decryptedMessage, "\r\n")) < 4:
		return decryptedMessage

	decryptedMessage = str.split(decryptedMessage, "\r\n")
	strMessage = ""

	for i in range(len(decryptedMessage) - 3):
		strMessage += str(decryptedMessage[3 + i])

	return strMessage

def stripFrom(decryptedMessage):
	if len(str.split(decryptedMessage, "\r\n")) < 4:
		return ""

	decryptedMessage = str.split(decryptedMessage, "\r\n")
	strFrom = str((decryptedMessage[1]).rsplit(":")[1])
	strFrom = strFrom.strip()
	lenStrFrom = len(strFrom)
	for i in range(12-lenStrFrom):
		strFrom= " " + strFrom

	return  strFrom

def parseMessage(decryptedMessage):

	# if strMessage has multiple lines, create extra lines for it
	timestamp = datetime.datetime.now().strftime("%m/%d/%Y at %I:%M%p: ")
	strMessage = stripMessage(decryptedMessage)
	strFrom = stripFrom(decryptedMessage)

	strMessageList = str.split(strMessage, '\n')

	parsedMessage = timestamp + strFrom + "> " + str(strMessageList[0])
	blankSpace = ""

	for i in range(len(timestamp)+len(strFrom)):
		blankSpace += " "

	if len(strMessageList) > 1:
		for i in range(1,len(strMessageList)):
			parsedMessage += '\n' + blankSpace + str(strMessageList[i])

	return parsedMessage
