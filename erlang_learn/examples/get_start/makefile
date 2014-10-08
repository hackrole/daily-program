all: hello afile_server afile_client
	echo "build successfully"

hello: hello.erl
	erlc hello.erl

afile_server: afile_server.erl
	erlc afile_server.erl

afile_client: afile_client.erl
	erlc afile_client.erl

run_hello:
	erl -noshell -s hello start -s init stop

clean:
	rm -f *.beam
