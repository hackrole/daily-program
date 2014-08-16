PROGS = udpserv01 udpcli01

all: ${PROGS}

udpserv01: udpserv01.c
	gcc -o $@ udpserv01.c ../libunp.a

udpcli01: udpcli01.c
	gcc -o $@ udpcli01.c ../libunp.a
