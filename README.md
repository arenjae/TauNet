TauNet
=============
###Connecting Pies together since 2015

TauNet is a simple protocol to send and receive encrypted messages over a private network anywhere in the world.


####Outline
- RC4 <- algorithm to output a stream of random numbers (run key scheduler 20 times after each message received / and transmitted)
- Password (universal for a network) - "password"
- IV thing (10 randomly chosen bytes that are appended to the password)
- Address Book
- Log (to store unsent messages)


####Address Book
| IP Address      | Port  | Name     |
| --------------- | ----- | -------- |
| 71.236.233.214  | 22    | Rachael  |
| 131.252.211.245 | 22    | Nathan   |



####Notes
- Scapy (to send a package)
    - search for python socket example

#####Basic Code Outline:
- 