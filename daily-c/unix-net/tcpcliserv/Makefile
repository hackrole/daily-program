PROGS = tcpserv01 tcpcli01

all: ${PROGS}

tcpserv01: tcpserv01.c
	gcc -o $@ tcpserv01.c ../libunp.a

tcpcli01: tcpcli01.c
	gcc -o $@ tcpcli01.c ../libunp.a
