-module(afile_server).
-export([start/1, loop/1]).

start(Dir) ->
    spawn(afile_server, loop, [Dir]).

%%% erlang中无限循环的一般写法
loop(Dir) ->
    receive
        {Client, list_dir} ->
            Client ! {self(), file:list_dir(Dir)};
        {Client, {get_file, File}} ->
            Full = filename:join(Dir, File),
            Client ! {self(), file:read_file(Full)}
    end,
    loop(Dir).
