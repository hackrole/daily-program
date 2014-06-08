PROGS =  daytimetcpcli daytimetcpcli6 daytimetcpcli6_debug \
       daytimetcpsrv

all: ${PROGS}


daytimetcpcli: daytimetcpcli.c
	gcc -o $@ daytimetcpcli.c ../libunp.a

daytimetcpcli6 : daytimetcpcli6.c
	gcc -o $@ daytimetcpcli6.c ../libunp.a

daytimetcpcli6_debug: daytimetcpcli6.c
	gcc -g -o $@ daytimetcpcli6.c ../libunp.a

daytimetcpsrv: daytimetcpsrv.c
	gcc -g -o $@ daytimetcpsrv.c ../libunp.a

clean:
	rm -f ${PROGS} *.o
