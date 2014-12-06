%% getty.erl
-module(getty).
-export([start/0, start/1, start/2]).
-export([init/2, l/2]).


%% interface: start(Port, {Mod, Fun})
%% start a 'getty' process that listen on tcp port Port, 
%% and spawns {Mod, Fun, [self]} after accepting a connection on that port
start(PortNo, MF) ->
    spawn(?MODULE, init, [PortNo, MF]).


%% defaults  start {user, server} on prot 7788
start() ->
    start(7788).

start(PortNo) when integer(PortNo) ->
    start(PortNo, {user, server}).


%% --------------------------------------------------------
init(PortNo, MF) ->
    process_flag(trap_exit, true),
    {ok, LS} = gen_tcp:listen(PortNo, [{reuseaddr, true}, {packet, 0},
                                       {active, false}]),
    g_loop(LS, MF).


%% main loop
g_loop(S, MF) ->
    {ok, NS} = gen_tcp:accept(S),
    Pid = spawn(?MODULE, l, [NS, MF]),
    gen_tcp:controlling_process(NS, Pid),
    Pid ! go_ahead,
    g_loop(S, MF).

%% --------------------------------------------------------
l(S, {UMod, UFun}) ->
    process_flag(trap_exit, true),
    receive
        go_ahead ->
            inet:setopts(S, [{active, true}])
    end,

    gen_tcp:send(S, "\nWelcome to Erlang!\n\n"),
    U = spawn_link(UMod, UFun, [self()]),
    ll(S, U).

%% child loop, passes the data between the user process and socket
ll(S, U) ->
    receive
        {tcp, S, Bytes} ->
            U ! {self(), {data, Bytes}},
            ll(S, U);
        {tcp_closed, S} ->
            io:format("getty:ll(~p, ~p) socket closed~n", [S, U]),
            exit(closed);
        {tcp_error, S, Reason} ->
            io:format("getty:ll(~p, ~p) socket error ~p~n", [S, U, Reason]),
            exit(Reason);
        {U, {command, Bytes}} ->
            gen_tcp:send(S, Bytes),
            ll(S, U);
        {'EXIT', U, Why} ->
            io:format("getty:ll(~p, ~p) user died ~p~n", [S, U, Why]),
            gen_tcp:close(S),
            exit(Why);
        Other ->
            io:format("getty:ll(~p, ~p) got msg ~p~n", [S, U, Other]),
            ll(S, U)
    end.
