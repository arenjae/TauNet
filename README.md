TauNet
=============
###Connecting Pies together since 2015
####Copyright (c) 2015 Rachael Johnson
-----------------------

TauNet is a simple protocol to send and receive encrypted messages over a private network anywhere in the world.

###To Use
Download all files.
In your raspberryPi Terminal, type
```
python3 TauNet.py
```

Note: When running program for the first time, you will be asked to enter a password for your network. This password must be the same for all other nodes in your network.

####Current Settings
- Keyscheduler runs 20 times (CipherSaber2)
- Default Password (universal for a network) - "password"
- Client/Server sends and receives on Port 6283

###Preview
![alt text](https://github.com/earthshine0/TauNet/blob/master/Capture.JPG "TauNet Preview")
   
##Bugs
- Choosing an number not in range of the address book when picking an address breaks program...
