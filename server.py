# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com

import socket
import protocol
import threading
import select
import datetime

messages = []
lastDay = str


# Change this to whatever your local network ip address is
# (if you have port forwarding enabled)
# host = '192.168.1.141'


class server(threading.Thread):
	def __init__(self, host, port, password):
		super().__init__()
		self.host_pair = (host, port)
		self.password = password

	def run(self):
		print("Server Started...")

		host2 = "localhost"
		PORT = 6283

		try:
			print("Listening on {}:{}.".format(*self.host_pair))
			conn = None
			listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			listener.bind(self.host_pair)
			listener.listen(10)

			while True:
				conn, sender = listener.accept()
				threading.Thread(target=getMessage, args=(conn, self.password)).start()

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


def getMessage(conn, password):
	readable, writable, exceptional = select.select([conn], [], [], 5)
	buffer = b""
	for s in readable:
		buffer = s.recv(1024)
		s.close()
		break

	if len(buffer) > 0:
		newDay()
		messages.append(parseMessage(protocol.decrypt(buffer, password)))


def stripMessage(decryptedMessage):
	if len(str.split(decryptedMessage, "\r\n")) < 4:
		return decryptedMessage

	decryptedMessage = str.split(decryptedMessage, "\r\n")
	strMessage = ""

	for i in range(4, len(decryptedMessage)):
		strMessage += '\n' + str(decryptedMessage[i])

	return strMessage


def stripFrom(decryptedMessage):
	if len(str.split(decryptedMessage, "\r\n")) < 4:
		return ""

	decryptedMessage = str.split(decryptedMessage, "\r\n")
	strFrom = str((decryptedMessage[1]).rsplit(":")[1])
	strFrom = strFrom.strip()
	lenStrFrom = len(strFrom)
	for i in range(12 - lenStrFrom):
		strFrom = " " + strFrom

	return strFrom


def parseMessage(decryptedMessage):
	# if strMessage has multiple lines, create extra lines for it
	timestamp = datetime.datetime.now().strftime("%I:%M%p: ")
	strMessage = stripMessage(decryptedMessage)
	strFrom = stripFrom(decryptedMessage)

	strMessageList = str.split(strMessage, '\n')

	parsedMessage = timestamp + strFrom + "| " + str(strMessageList[1])
	blankSpace = ""

	for i in range(len(timestamp) + len(strFrom)):
		blankSpace += " "

	if len(strMessageList) > 1:
		for i in range(2, len(strMessageList)):
			parsedMessage += '\n' + blankSpace + '| ' + str(strMessageList[i])

	return parsedMessage


def newDay():
	global lastDay
	today = '{:-^100}'.format(datetime.datetime.now().strftime("%A, %B %d, %Y"))

	if lastDay != today:
		lastDay = today
		messages.append(today)
