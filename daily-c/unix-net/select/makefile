PROGS = strcliselect01.o strcliselect02.o tcpservselect01

all: ${PROGS}

strcliselect01.o: strcliselect01.c
	gcc -c strcliselect01.c

strcliselect02.o: strcliselect02.c
	gcc -c strcliselect02.c

tcpservselect01: tcpservselect01.c
	gcc -o $@ tcpservselect01.c ../libunp.a
