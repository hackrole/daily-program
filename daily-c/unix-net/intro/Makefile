PROGS =  daytimecpcli

all: ${PROGS}


daytimecpcli: daytimecpcli.o
	gcc -o $@ daytimecpcli.o ${LIBS}


clean:
	rm -f ${PROGS} *.o
