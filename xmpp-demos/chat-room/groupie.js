var Groupie = {
  connectioin: null,
  room: null,
  nickname: null,
  NS_MUC: "http://jabber.org/protocol/muc",
  joined: null,
  participants: null,

  on_presence: function (presence){
    var from = $(presence).attr('from');
    var room = Strophe.getBareJidFromJid(from);

    // make sure this presence is for the right room
    if(room == Groupie.room){
      var nick = Strophe.getResourceFromJid(from);

      if($(presence).attr('type') == 'error' && !Groupie.joined){
        // error joining room; reset app
        Groupie.connection.disconnected();
      }else if(!Groupie.participants[nick] && $(presence).attr(type) !== 'unavailable'){
        // add to participant list
        Groupie.participants[nick] = true;
        $('#participant-list').append('<li>' + nick + '</li>');
      }

      if($(presence).attr('type') !== 'error' && !Groupie.joined){
        // check for status 110 to see if it's our own presence
        if($(presence).find("status[code='110']").length > 0){
          // check if server changed our nick
          if($(presence).find("status[code='210']").length > 0){
            Groupie.nickname = Strophe.getResourceFromJid(from);
          }

          // room join complete
          $(document).trigger('room_joined');
        }
      }
    }
    return true;
  },

  on_public_message: function (message){
    var from = $(message).attr('from');
    var room = Strophe.getBareJidFromJid(from);
    var nick = Strophe.getResourceFromJid(from);

    // make sure message is from the right place
    if (room == Groupie.room){
      // is message from a user or the room itself?
      var notice = !nick;

      // message from ourself will be styled differently
      var nick_class = "nick";
      if (nick == Groupie.nickname){
        nick_class += " self";
      }

      var body = $(message).children('body').text();

      if(!notice){
        Groupie.add_message("<div class='message'>" +
            "&lt;<span class='" + nick_class + "'>" +
            nick + "</span>&gt; <span class='body'>" +
            body + "</span></div>");
      }else{
        Groupie.add_message("<div class='notice'>*** " + body + "</div>");
      }
    }
    return true;
  }
};

Groupie.connection.addHandler(Groupie.on_public_message, null, "message", "groupchat")


$(document).ready(function (){
  $('#login_dialog').dialog({
    autoOpen: true,
    draggable: false,
    modal: true,
    title: 'Join a Room',
    buttons: {
      "Join": function (){
        Groupie.room = $('#room').val();
        Groupie.nickname = $('#nickname').val();

        $(document).trigger('connect', {
          jid: $('#jid').val,
          password: $('#password').val()
        });

        $('#password').val('');
        $(this).dialog('close');
      }
    }
  });
});

$(document).bind('connect', function (ev, data){
  Groupie.connection = new Strophe.Connection(
    'http://localhost:5280/http-bind');
  Groupie.connection.connect(data.jid, data.password,
    function (status){
      if (status == Strophe.Status.CONNECTED){
        $(document).trigger('connected');
      }else if(status == Strophe.Status.DISCONNECTED){
        $(document).trigger('disconnected');
      }
  });
});


$(document).bind('connected', function (){
  // nothing here yet
  alert("connected");

  Groupie.joined = false;
  Groupie.participants = {};

  Groupie.connection.send($press().c('priority').t('-1'));
  Groupie.connection.addHandler(Groupie.on_presence, null, "presence");

  Groupie.connection.send(
    $press({to: Groupie.room + "/" + Groupie.nickname}).c('x', {xmlns: Groupie.NS_MUC}));
});

$(document).bind('disconnected', function (){
  // nothing here yet
  alert("disconnected");

  Groupie.connection = null;
  $('#participant-list').empty();
  $('#room-name').empty();
  $('#room-topic').empty();
  $('#chat').empty();
  $('#login_dialog').dialog('open');
});


$(document).bind('room_joined', function (){
  Groupie.joined = true;

  $('#leave').removeAttr('disabled');
  $('#room-name').text('Groupie.room');

  $('#chat').append("<div class='notice'>*** Room joined.</div>");
});

$('#leave').click(function (){
  Groupie.connection.send(
    $pres({
      to: Groupie.room + "/" + Groupie.nickname,
      type: "unavailable",
    }));
  Groupie.connection.disconnect();
});
