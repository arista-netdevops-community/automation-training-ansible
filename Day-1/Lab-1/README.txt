For this lab, your goal is to connect to all switches in your topology via eAPI, extract data, and print it to the console in a nice format.

1) Using the python requests library, connect to each switch in your topology and run commands, except for CVX. 
   Management IPs for each switch can be found from CVP device listing.
2) For each switch, print the hostname, serial number, and system MAC address.

Example:

spine1.atd.lab is a vEOS-lab with serial number 5DECFFE9E33961213DAD5BB7D9BA6437 and system MAC address 00:1c:73:9c:29:c3
spine2.atd.lab is a vEOS-lab with serial number 7D732D47D86526B5F9C082C0D145F822 and system MAC address 00:1c:73:10:33:5d
leaf1.atd.lab is a vEOS-lab with serial number 074AA04A4AD394420D5D5A500E582163 and system MAC address 00:1c:73:76:1b:6b
leaf2.atd.lab is a vEOS-lab with serial number FBC252D3EB5B5B2C4EF0AF4F11AFB6CC and system MAC address 00:1c:73:fd:a9:d8
leaf3.atd.lab is a vEOS-lab with serial number 34C8BC0FF034FF78ED21590EA5DE9B22 and system MAC address 00:1c:73:b8:26:81
leaf4.atd.lab is a vEOS-lab with serial number C99F0B2F8EA5266C3A6B8F055C050506 and system MAC address 00:1c:73:f1:7b:f6
host1.atd.lab is a vEOS-lab with serial number 8D4F5D212044DFE59C6513AB6551F70F and system MAC address 00:1c:73:7b:2d:91
host2.atd.lab is a vEOS-lab with serial number BA1FD7044639B542FE4792462666CC5F and system MAC address 00:1c:73:4b:97:ec