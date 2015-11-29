TauNet
=============
##Connecting Pies together since 2015
###Copyright (c) 2015 Rachael Johnson
TauNet is a simple protocol to send and receive encrypted messages over a private network anywhere in the world.

###To Use
Download all files (excluding docs)
In your raspberryPi Terminal, type
```
python3 TauNet.py
```

####Current Settings
- Keyscheduler runs 20 times (CipherSaber2)
- Password (universal for a network) - "password"

###Current Compatibility
This program is currently compatible with the following TauNet implementations
| username | address | 
| ----------- | -------- |
| tdulcet | tealdulcet.ddns.net |
| chupacabra | chupa-cabra.ddns.net |
| paolo2 | pirr.ddns.net |
| cort | wyeast.ddns.net |
   
   
##Bugs
 - Need error handling when a connection has an error (error 111)
 - Need to make sure sockets are being closed after a connection is done