// TODO: not finished
var Hello = {
  connection: null,
  start_time: null,

  log: function (msg){
    $('#log').append("<p>" + msg + "</p>");
  },

  send_ping: function (to){
    var ping = $iq({
      to: to,
      type: "get",
      id: "ping1"
    }).c("ping", {xmlns: "urn:xmpp:ping"});

    Hello.log("sending ping to " + to + ".");
    Hello.start_time = (new Date()).getTime();
    Hello.connection.send(ping);
  },

  handle_pong: function (iq){
    var elapsed = (new Date()).getTime() - Hello.start_time;
    Hello.log("Received pong from server in " + elapsed + "ms.");

    Hello.connection.disconnect();

    return false;
  },
};

$(document).ready(function (){
  $('#login_dialog').dialog({
    autoOpen: true,
    draggable: false,
    moda1: true,
    title: 'Connect to XMPP',
    buttons: {
      "Connect": function (){
        $(document).trigger('connect', {
          jid: $('#jid').val(),
          password: $('#password').val()
        });

        $('#password').val('');
        $(this).dialog('close');
      }
    }
  });
});


$(document).bind('connect', function (en, data){
  var conn = new Strophe.Connection("http://localhost:5280/http-bind");
  conn.connect(data.jid, data.password, function(status){
    if (status == Strophe.Status.CONNECTED){
      $(document).trigger('connected');
    }else if (status == Strophe.Status.DISCONNECTED){
      $(document).trigger('disconnected');
    }
  });
  Hello.connections = conn;
});


$(document).bind('connected', function (){
  Hello.log("connection established");
  Hello.connnection.addHandler(Hello.handle_pong,
    null, "iq", "ping1");

  var domain = Strophe.getDomainFromJid(Hello.connection.jid);

  Hello.send_ping(domain);
});


$(document).bind('disconnected', function (){
  Hello.log("Connection terminal");

  Hello.connection = null;
});
