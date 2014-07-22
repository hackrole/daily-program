// TODO: not finished
var Hello = {
  connection: null,
  start_time: null,

  log: function(msg){
    $('#log').append("<p>" + msg + "</p>");
  },

  send_ping: function(to){
    var ping = $iq({
      to: to,
      type: "get",
      id: "ping1"
    }).c("ping", {xmlns: "urn:xmpp:ping"});

    Hello.log("sending ping to " + to + ".");
    Hello.start_time = (new Date()).getTime();
    Hello.connection.send(ping);
  },

  handle_pong: function(iq){
    var elapsed = (new Date()).getTime() - Hello.start_time;
    Hello.log("Received pong from server in " + elapsed + "ms.");

    Hello.connection.disconnect();

    return false;
  },
};

$(document).ready(function(){
  $('#login_dialog').dialog({
    autoOpen: true,
    draggable: false,
    moda1: true,
    title: 'Connect to XMPP',
  })
})
