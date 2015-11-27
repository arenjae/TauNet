# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

from os import urandom

REPS = 20


def swap(l, a, b):
	"""Swap entries a and b in list l."""
	temp = l[a]
	l[a] = l[b]
	l[b] = temp


def rc4(messageLen, password):
	passLen = len(password)
	S = list(range(256))
	j = 0
	for r in range(REPS):
		for i in range(256):
			j = (j + S[i] + password[i % passLen]) % 256
			swap(S, i, j)

	keystream = list(range(messageLen))

	j = 0
	for i in range(messageLen):
		tempi = (i + 1) % 256
		j = (j + S[tempi]) % 256
		swap(S, tempi, j)
		keystream[i] = S[(S[tempi] + S[j]) % 256]

	return keystream


def encrypt(message, password):
	messageLen = len(message)
	iv = urandom(10)
	keystream = rc4(messageLen, password + iv)
	ciphertext = list(range(messageLen + 10))
	for i in range(10):
		ciphertext[i] = iv[i]
	for i in range(messageLen):
		ciphertext[i + 10] = ord(message[i]) ^ keystream[i]
	return bytes(ciphertext)


def decrypt(message, password):
	iv = message[0:10]
	passIV = password + bytes(iv)

	message = message[10:len(message)]
	keystream = rc4(len(message), passIV)
	plaintext = ""
	for i in range(len(message)):
		plaintext += chr(message[i] ^ keystream[i])
	return str(plaintext)
