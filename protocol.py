from os import urandom
password = str.encode('password')
REPS = 200


def swap(l, a, b):
    """Swap entries a and b in list l."""
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def rc4(message, password):
    i = 0
    state = list(range(256))
    key = list(range(256))
    cipher = b""
    for a in range(REPS):
        while i < 256:
            ctmp = password[i % len(password):(i % len(password)) + 1]
            key[i] = ord(ctmp)
            state[i] = i
            i += 1
    i = j = 0
    while i < 256:
        j = (j + state[i] + key[i]) % 256
        swap(state, i, j)
        i += 1
    a = 1
    while a <= len(message):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        swap(state, i, j)
        k = state[(state[i] + state[j]) % 256]
        ctmp = message[a-1:a]
        itmp = ord(ctmp)
        cipherbyte = itmp ^ k
        cipherbyte = bytes([cipherbyte]) #change to byte
        cipher += cipherbyte
        a += 1
    return cipher


def encrypt(message, password):
    iv = urandom(10)
    password += iv
    cipher = rc4(message, password)
    IVmessage = iv + cipher #concatenate cipher to iv
    return IVmessage


def decrypt(message, password):
    l = message.__len__()
    iv = message[0:10]
    password += iv
    message = message[10:l]
    return rc4(message, password)
