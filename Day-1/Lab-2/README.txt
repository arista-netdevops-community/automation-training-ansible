Taking the techniques you developed in the last lab, we're now going to clean up the output you print to terminal, using Jinja.

1) Using the API, collect the hostname, serial number, and ARP table from each device
2) Create an appropriate data structure to hold your device responses and feed your Jinja template
3) Create your Jinja template
4) Using your Jinja template, print output to the console after contacting your switch APIs that looks like this:

8 devices contacted in total
-------------------------------------------------

spine1 (serial number 5DECFFE9E33961213DAD5BB7D9BA6437)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

spine2 (serial number 7D732D47D86526B5F9C082C0D145F822)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

leaf1 (serial number 074AA04A4AD394420D5D5A500E582163)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

leaf2 (serial number FBC252D3EB5B5B2C4EF0AF4F11AFB6CC)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

leaf3 (serial number 34C8BC0FF034FF78ED21590EA5DE9B22)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

leaf4 (serial number C99F0B2F8EA5266C3A6B8F055C050506)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

host1 (serial number 8D4F5D212044DFE59C6513AB6551F70F)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1

host2 (serial number BA1FD7044639B542FE4792462666CC5F)
Total of 2 entries found in ARP table
- 192.168.0.1 (MAC fe1c.73a0.c601) learned on Management1
- 192.168.0.5 (MAC 001c.73a0.c601) learned on Management1